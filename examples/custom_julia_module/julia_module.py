"""Modules written in Julia, chained with C++ modules, in a multithreaded sequence.

It needs pyStreamPU compiled with Julia (see README.md in this folder):

    python examples/custom_julia_module/julia_module.py

The graph is: input -> Julia `increment` (stateless, constant) -> C++ `* 2` ->
Julia `accumulate` (stateful, states defined in codelets.jl) -> output.
"""

import os
import sys

import numpy as np

import streampu as spu
from streampu import _ext

if not _ext.has_julia:
    sys.exit(
        "This pyStreamPU is not compiled with Julia: reinstall it with\n"
        "    pip install . -C cmake.define.SPU_LINK_JULIA=ON\n"
        "(see examples/custom_julia_module/README.md)"
    )

from streampu._ext.jl import Julia, Stateful_Julia, Stateless_Julia  # noqa: E402

N = 8  # number of samples per frame
HERE = os.path.dirname(os.path.abspath(__file__))

Julia.init()  # optional: the first Julia module starts Julia anyway

# --- Stateless module: add a constant to each sample --------------------------
inc = Stateless_Julia()
t_inc = inc.create_task("increment")
inc.create_socket_in(t_inc, "in", N, spu.int32)
inc.create_socket_out(t_inc, "out", N, spu.int32)
inc.create_constant(t_inc, 3, spu.int32)  # -> argument `step` (Int32)
inc.create_codelet(
    t_inc,
    """
function increment(sck_in, sck_out, step, rnt_frame_id, rnt_n_frames_per_wave)
    @inbounds for i in eachindex(sck_in)
        sck_out[i] = sck_in[i] + step
    end
    return 0
end
""",
)

# --- Stateful module: states and codelet in codelets.jl ---------------------
acc = Stateful_Julia()
acc.create_state_file("Accumulator(0, 0)", os.path.join(HERE, "codelets.jl"))  # one copy per thread
acc.create_state("Gain(Int32(10))", shared=True)  # type already defined by codelets.jl
t_acc = acc.create_task("accumulate")
acc.create_socket_in(t_acc, "in", N, spu.int32)
acc.create_socket_out(t_acc, "out", N, spu.int32)
acc.create_codelet(t_acc)  # the Julia function `accumulate` of codelets.jl

# For now, a Julia module must be evaluated before an immediate execution
# (a Sequence or a Pipeline evaluates its modules itself)
inc.eval()
acc.eval()

# --- Immediate execution: each call runs the task ------------------------------
x = spu.array(np.arange(N, dtype=np.int32))
y = inc.increment(x)  # Julia
z = y * 2  # C++
w = acc.accumulate(z)  # Julia
print("input              :", x.numpy[0])
print("after increment    :", y.numpy[0])
print("after * 2 (C++)    :", z.numpy[0])
print("after accumulate   :", w.numpy[0])
print("states of acc      :", acc.get_states())
expected = (np.arange(N) + 3) * 2 * 10
assert np.array_equal(w.numpy[0], expected), "unexpected output"

# --- Sequence on 4 threads: each thread runs its own clone of the modules ------
seq = spu.Sequence(w, 4)
seq.exec_n_times(1000)
clones = seq.get_cloned_modules(acc)
print(f"\nsequence: {len(clones)} clones of acc")
for i, clone in enumerate(clones):
    print(f"  thread {i}:", clone.get_states())
print("output of thread 0 :", w.numpy[0])
assert np.array_equal(w.numpy[0], expected), "unexpected output in the sequence"
print("\nOK")
