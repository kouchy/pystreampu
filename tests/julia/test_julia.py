"""Tests of the Julia modules (spu.Stateless_Julia, spu.Stateful_Julia, spu.julia).

They are skipped when pyStreamPU is not compiled with Julia
(pip install . -C cmake.define.SPU_LINK_JULIA=ON). The Julia functions are defined in the
`Main` module of Julia, shared by the whole process: each test uses its own names.
"""

import subprocess
import sys
import textwrap

import numpy as np
import pytest

import streampu as spu

pytestmark = pytest.mark.skipif(not spu.julia.available(), reason="pyStreamPU is not compiled with Julia")

N = 8


def make_stateless(name, code, n=N, dtype=spu.int32, constants=()):
    """Julia module with one task `name`: socket `in`, socket `out`, then the constants."""
    mdl = spu.Stateless_Julia()
    tsk = mdl.create_task(name)
    mdl.create_socket_in(tsk, "in", n, dtype)
    mdl.create_socket_out(tsk, "out", n, dtype)
    for value, cst_dtype in constants:
        mdl.create_constant(tsk, value, cst_dtype)
    mdl.create_codelet(tsk, code)
    return mdl


def test_runtime():
    spu.julia.init()
    assert spu.julia.is_init()
    assert spu.Julia.get_n_proxies() > 0
    spu.julia.eval("t_runtime_double(x) = 2x")
    with pytest.raises(spu.exceptions.RuntimeError, match="t_runtime_undefined"):
        spu.julia.eval("t_runtime_undefined()")


def test_stateless_immediate_execution():
    code = """
    function t_inc(sck_in, sck_out, step, rnt_frame_id, rnt_n_frames_per_wave)
        @inbounds for i in eachindex(sck_in)
            sck_out[i] = sck_in[i] + step
        end
        return 0
    end"""
    mdl = make_stateless("t_inc", code, constants=[(3, spu.int32)])
    assert isinstance(mdl, spu.Module) and isinstance(mdl, spu.Module_Julia)
    assert not mdl.is_eval()
    y = mdl.t_inc(spu.array(np.arange(N, dtype=np.int32)))  # evaluated automatically
    assert mdl.is_eval()
    np.testing.assert_array_equal(y.numpy, [np.arange(N) + 3])


@pytest.mark.parametrize(
    "value, cst_dtype, julia_type",
    [
        (True, None, "Bool"),
        (7, None, "Int64"),
        (2.5, None, "Float64"),
        (np.float32(1.5), None, "Float32"),
        (np.uint8(3), None, "UInt8"),
        (5, spu.int8, "Int8"),
        (5, spu.int16, "Int16"),
        (5, spu.int32, "Int32"),
        (5, spu.uint16, "UInt16"),
        (5, spu.uint32, "UInt32"),
        (5, spu.uint64, "UInt64"),
        (5, spu.float32, "Float32"),
    ],
)
def test_constant_types(value, cst_dtype, julia_type):
    name = f"t_cst_{julia_type}_{'auto' if cst_dtype is None else 'dtype'}"
    code = f"""
    function {name}(sck_in, sck_out, cst, rnt_frame_id, rnt_n_frames_per_wave)
        sck_out[1] = typeof(cst) == {julia_type} ? 1 : 0
        sck_out[2] = Int32(round(cst))
        return 0
    end"""
    mdl = make_stateless(name, code, n=2, constants=[(value, cst_dtype)])
    y = getattr(mdl, name)(spu.array(np.zeros(2, dtype=np.int32)))
    assert y.numpy[0][0] == 1, f"the constant is not a {julia_type}"
    assert y.numpy[0][1] == round(float(value))


def test_codelet_file_function_name_and_frames(tmp_path):
    path = tmp_path / "codelets.jl"
    path.write_text(
        "function t_double!(sck_fwd, rnt_frame_id, rnt_n_frames_per_wave)\n sck_fwd .*= 2\n return 0\nend\n"
    )
    mdl = spu.Stateless_Julia()
    tsk = mdl.create_task("dbl")
    mdl.create_socket_fwd(tsk, "fwd", 3, spu.float64)
    mdl.create_codelet_file(tsk, path, function_name="t_double!")
    mdl.n_frames = 2
    x = spu.array(np.arange(6, dtype=np.float64).reshape(2, 3))
    mdl.dbl(x)
    np.testing.assert_array_equal(x.numpy, np.arange(6).reshape(2, 3) * 2)


def test_codelet_already_defined():
    spu.julia.eval("t_defined(sck_in, sck_out, f, n) = (sck_out .= sck_in .* 10; 0)")
    mdl = make_stateless("t_defined", "")
    y = mdl.t_defined(spu.array(np.ones(N, dtype=np.int32)))
    np.testing.assert_array_equal(y.numpy, np.full((1, N), 10))


def test_julia_exception_in_codelet():
    mdl = make_stateless("t_boom", 't_boom(sck_in, sck_out, f, n) = error("t_boom failed")')
    assert mdl.jl_safe
    with pytest.raises(spu.exceptions.RuntimeError, match="t_boom failed"):
        mdl.t_boom(spu.array(np.zeros(N, dtype=np.int32)))
    mdl.jl_safe = False
    assert not mdl.jl_safe


def test_errors():
    with pytest.raises(TypeError):
        spu.Module_Julia()
    mdl = make_stateless("t_err", "t_err(sck_in, sck_out, f, n) = 0")
    with pytest.raises(spu.exceptions.RuntimeError):  # no constant after the codelet
        mdl.create_constant(mdl.tasks[0], 1)
    with pytest.raises(TypeError):
        mdl.create_constant(mdl.tasks[0], "not a number")


def make_accumulator(name, n=N):
    """Stateful module: `Acc` is cloned (one per thread), `Gain` is shared."""
    acc = spu.Stateful_Julia()
    acc.create_state("TAcc(0, 0)", code="mutable struct TAcc\n total::Int64\n calls::Int64\nend")
    acc.create_state("TGain(Int32(10))", shared=True, code="struct TGain\n factor::Int32\nend")
    tsk = acc.create_task(name)
    acc.create_socket_in(tsk, "in", n, spu.int32)
    acc.create_socket_out(tsk, "out", n, spu.int32)
    acc.create_codelet(
        tsk,
        f"""
    function {name}(acc::TAcc, gain::TGain, sck_in, sck_out, rnt_frame_id, rnt_n_frames_per_wave)
        acc.calls += 1
        @inbounds for i in eachindex(sck_in)
            acc.total += sck_in[i]
            sck_out[i] = sck_in[i] * gain.factor
        end
        return 0
    end""",
    )
    return acc


def calls_of(state):
    return int(state.split("(")[1].rstrip(")").split(",")[1])


def test_stateful_states_in_sequence():
    acc = make_accumulator("t_acc")
    x = spu.array(np.ones(N, dtype=np.int32))
    y = acc.t_acc(x + 1)  # C++ module, then Julia
    np.testing.assert_array_equal(y.numpy, np.full((1, N), 20))
    assert acc.get_states() == ["TAcc(16, 1)", "TGain(10)"]

    seq = spu.Sequence(y, 4)
    seq.exec_n_times(200)
    clones = seq.get_cloned_modules(acc)
    assert len(clones) == 4
    assert all(isinstance(c, spu.Stateful_Julia) for c in clones)
    # each clone has its own copy of TAcc, made from the original (1 call before)
    assert sum(calls_of(c.get_states()[0]) for c in clones) == 200 + 4
    assert {c.get_states()[1] for c in clones} == {"TGain(10)"}
    np.testing.assert_array_equal(y.numpy, np.full((1, N), 20))


def python_module(name, func, n=N, dtype=spu.int32):
    mdl = spu.Stateless()
    tsk = mdl.create_task(name)
    mdl.create_socket_in(tsk, "in", n, dtype)
    mdl.create_socket_out(tsk, "out", n, dtype)
    mdl.create_codelet(tsk, func)
    return mdl


GC_STRESS = """
const {name}_counter = Threads.Atomic{{Int}}(0)
function {name}(sck_in, sck_out, rnt_frame_id, rnt_n_frames_per_wave)
    tmp = [rand(64) for _ in 1:10]  # allocations
    if Threads.atomic_add!({name}_counter, 1) % 20 == 0
        GC.gc(false)  # the GC must wait for all the threads adopted by Julia
    end
    sck_out .= sck_in .+ (length(tmp) - 10)
    return 0
end"""


def test_sequence_python_julia_gc():
    """Python codelets and Julia codelets that run the GC, on 4 threads: no deadlock."""
    jl_inc = make_stateless("t_seq_inc", "t_seq_inc(i, o, f, n) = (o .= i .+ 1; 0)")

    def py_double(mdl, tsk, frame_id):
        tsk["out"].numpy[:] = tsk["in"].numpy * 2
        return 0

    py = python_module("py_double", py_double)
    jl_gc = make_stateless("t_seq_gc", GC_STRESS.format(name="t_seq_gc"))
    z = jl_gc.t_seq_gc(py.py_double(jl_inc.t_seq_inc(spu.array(np.arange(N, dtype=np.int32)))))
    seq = spu.Sequence(z, 4)
    seq.exec_n_times(1000)
    np.testing.assert_array_equal(z.numpy, [(np.arange(N) + 1) * 2])


@pytest.mark.parametrize("n_threads", [1, 3])
def test_pipeline_python_julia_gc(tmp_path, n_threads):
    """Pipeline whose middle stage mixes Julia (with GC) and Python: the file is unchanged."""
    length = 512
    in_path, out_path = tmp_path / "in.bin", tmp_path / "out.bin"
    data = np.random.default_rng(0).integers(0, 256, length * 200, dtype=np.uint8)
    data.tofile(in_path)

    jl_inc = make_stateless(
        f"t_pip_inc{n_threads}", f"t_pip_inc{n_threads}(i, o, f, n) = (o .= i .+ UInt8(1); 0)", length, spu.uint8
    )

    def py_dec(mdl, tsk, frame_id):
        tsk["out"].numpy[:] = tsk["in"].numpy - 1
        return 0

    py = python_module("py_dec", py_dec, length, spu.uint8)
    name = f"t_pip_gc{n_threads}"
    jl_gc = make_stateless(name, GC_STRESS.format(name=name), length, spu.uint8)

    auto_exec = spu.Task.call_auto_exec
    spu.Task.call_auto_exec = False
    try:
        src = spu.source_user_binary(length, str(in_path), auto_reset=False, dtype=spu.uint8)
        snk = spu.sink_user_binary(length, str(out_path), dtype=spu.uint8)
        data_out, count = src.generate()
        data_out = getattr(jl_gc, name)(py.py_dec(getattr(jl_inc, f"t_pip_inc{n_threads}")(data_out)))
        snk.send_count(data_out, count)
        pipeline = spu.Pipeline(
            [src.generate],
            [snk.send_count],
            [
                [[src.generate], [src.generate], []],
                [[getattr(jl_inc, f"t_pip_inc{n_threads}")], [getattr(jl_gc, name)], []],
                [[snk.send_count], [snk.send_count], []],
            ],
            [1, n_threads, 1],
            [16, 16],
            [False, False],
        )
        pipeline.exec()
        del pipeline, snk  # flush the output file
    finally:
        spu.Task.call_auto_exec = auto_exec
    np.testing.assert_array_equal(np.fromfile(out_path, dtype=np.uint8), data)


def run_python(code, cwd):
    """Run Python code in a new process (Julia is stopped at its exit): (return code, output).

    It runs in `cwd`: from the root of the repository, `import streampu` would load the
    `streampu/` folder of the sources instead of the installed package.
    """
    proc = subprocess.run(
        [sys.executable, "-c", textwrap.dedent(code)], cwd=cwd, capture_output=True, text=True, timeout=120
    )
    return proc.returncode, proc.stdout + proc.stderr


def test_exit_hooks(tmp_path):
    """At the exit of Python, the atexit functions and the finalizers of Julia run."""
    code, out = run_python(
        """
        import sys
        import streampu as spu
        spu.julia.eval('''
            atexit(() -> println("julia atexit"))
            mutable struct Resource; x::Int; end
            r = Resource(1); finalizer(_ -> println("julia finalizer"), r); r = nothing
        ''')
        print("end of script", flush=True)
        sys.exit(3)
        """,
        tmp_path,
    )
    assert code == 3, out
    assert "end of script" in out and "julia atexit" in out and "julia finalizer" in out, out


def test_exit_sequence_alive(tmp_path):
    """A sequence of Julia modules still alive at the exit of Python: no deadlock."""
    code, out = run_python(
        """
        import numpy as np
        import streampu as spu
        spu.julia.eval('atexit(() -> println("julia atexit"))')
        mdl = spu.Stateless_Julia()
        tsk = mdl.create_task("t_exit_inc")
        mdl.create_socket_in(tsk, "in", 8, spu.int32)
        mdl.create_socket_out(tsk, "out", 8, spu.int32)
        mdl.create_codelet(tsk, "t_exit_inc(i, o, f, n) = (o .= i .+ Int32(1); 0)")
        x = spu.array(np.arange(8, dtype=np.int32))
        y = mdl.t_exit_inc(x)
        seq = spu.Sequence(y, 4)
        seq.exec_n_times(100)
        print("end of script", flush=True)
        """,
        tmp_path,
    )
    assert code == 0, out
    assert "end of script" in out and "julia atexit" in out, out
