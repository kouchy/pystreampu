"""Toy example: destruction of Python modules derived from Stateful_core.

It checks three scenarios where `Stateful_core::operator delete` may misbehave (see
include/wrapper/Module/Stateful/Stateful/Stateful.hpp):

1. an original module (not a clone) destroyed by Python: double destruction?
2. many modules created and destroyed: memory never released?
3. a sequence with clones destroyed: double destruction of the clones?

Usage:
    python -X faulthandler scripts/toy_stateful_delete.py

A crash (segmentation fault, "Fatal Python error"...) shows which scenario fails. No
crash does not prove that everything is fine: a double destruction may go unnoticed.
"""

import faulthandler
import gc
import resource
import sys

import streampu as spu
from streampu import Stateful_core

faulthandler.enable()


class Dummy(Stateful_core):
    """Minimal stateful module with one task that does nothing."""

    def __init__(self):
        super().__init__()
        task = self.create_task("noop")
        self.create_socket_out(task, "out", 1, spu.int32)
        self.create_codelet(task, lambda mdl, tsk, fid: 0)

    def clone(self):
        other = Dummy.__new__(Dummy)
        Stateful_core.__init__(other)
        return other


def rss_mb() -> float:
    """Return the maximum resident memory of the process, in MB."""
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return rss / 2**20 if sys.platform == "darwin" else rss / 2**10


# 1. An original module, without clone, destroyed by Python
d = Dummy()
del d
gc.collect()
print("1. original destroyed without crash", flush=True)

# 2. Memory: create and destroy many original modules
before = rss_mb()
for _ in range(200_000):
    Dummy()
gc.collect()
print(f"2. max memory: {before:.0f} MB -> {rss_mb():.0f} MB", flush=True)

# 3. Clones: a sequence on 4 threads, then destruction
d = Dummy()
out = d.noop()
seq = spu.Sequence(out, 4)
seq.exec_n_times(10)
del seq
gc.collect()
print("3. sequence with clones destroyed without crash", flush=True)

del d, out
gc.collect()
print("4. end of the script", flush=True)
