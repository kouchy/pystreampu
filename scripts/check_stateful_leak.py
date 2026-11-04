"""Check whether destroying modules leaks memory, for Stateful_core and Stateless modules.

Each measure runs in its own process: create and destroy N modules one by one, and compare
the current memory (RSS) of the process before and after. A leak gives the same number of
bytes lost per module whatever N; no leak gives about 0.

Two sizes of socket are measured: if the loss per module does not depend on the size, the
buffers are freed and only the objects themselves leak.

Usage:
    python scripts/check_stateful_leak.py              # measure
    python scripts/check_stateful_leak.py --diagnose   # and look for the cause
"""

import gc
import os
import subprocess
import sys

N_WARMUP = 2_000


def current_rss_kb() -> int:
    """Current resident memory of this process, in KB (macOS and Linux)."""
    out = subprocess.run(["ps", "-o", "rss=", "-p", str(os.getpid())], capture_output=True, text=True)
    return int(out.stdout.strip())


def child(kind: str, n: int, size: int) -> None:
    import streampu as spu
    from streampu._ext.sfl import Stateful_core

    class Dummy(Stateful_core):
        def __init__(self):
            super().__init__()
            task = self.create_task("noop")
            self.create_socket_out(task, "out", size, spu.int32)
            self.create_codelet(task, lambda mdl, tsk, fid: 0)

        def clone(self):
            other = Dummy.__new__(Dummy)
            Stateful_core.__init__(other)
            return other

    class Empty(Stateful_core):
        """Subclass without any task."""

        def clone(self):
            other = Empty.__new__(Empty)
            Stateful_core.__init__(other)
            return other

    def _noop(mdl, tsk, fid):
        return 0

    class Partial(Stateful_core):
        """Subclass that only does some of the steps of Dummy (see `steps`)."""

        def __init__(self, steps):
            super().__init__()
            task = self.create_task("noop")
            if "socket" in steps:
                self.create_socket_out(task, "out", size, spu.int32)
            if "codelet" in steps:
                self.create_codelet(task, _noop)

        def clone(self):
            other = Partial.__new__(Partial)
            Stateful_core.__init__(other)
            return other

    def make_base():
        """Stateful_core itself, without Python subclass."""
        mdl = Stateful_core()
        task = mdl.create_task("noop")
        mdl.create_socket_out(task, "out", size, spu.int32)
        mdl.create_codelet(task, lambda m, t, f: 0)
        return mdl

    def make_stateless():
        mdl = spu.Stateless()
        task = mdl.create_task("noop")
        mdl.create_socket_out(task, "out", size, spu.int32)
        mdl.create_codelet(task, lambda m, t, f: 0)
        return mdl

    makers = {
        "Stateful_core": Dummy,
        "Stateless": make_stateless,
        "base": make_base,
        "empty": Empty,
        "task": lambda: Partial(()),
        "task+socket": lambda: Partial(("socket",)),
        "task+codelet": lambda: Partial(("codelet",)),
    }
    make = makers[kind]

    for _ in range(N_WARMUP):
        make()
    gc.collect()
    before = current_rss_kb()
    for _ in range(n):
        make()
    gc.collect()
    after = current_rss_kb()
    alive = sum(1 for o in gc.get_objects() if type(o).__name__ in ("Dummy", "Empty", "Partial"))
    print(f"{(after - before) * 1024 / n} {alive}")


def main() -> None:
    configs = [
        ("Stateful_core", 1),
        ("Stateless", 1),
        ("Stateful_core", 1000),
        ("Stateless", 1000),
    ]
    counts = [20_000, 80_000]
    print(f"{'module':14s} {'socket size':>11s} " + " ".join(f"{f'N={n}':>12s}" for n in counts) + "   (bytes lost per module)")
    for kind, size in configs:
        results = []
        for n in counts:
            out = subprocess.run([sys.executable, __file__, "--child", kind, str(n), str(size)], capture_output=True, text=True)
            if out.returncode != 0:
                results.append("crash")
                print(out.stderr[-2000:], file=sys.stderr)
            else:
                results.append(f"{float(out.stdout.strip().splitlines()[-1].split()[0]):.0f}")
        print(f"{kind:14s} {size:>11d} " + " ".join(f"{r:>12s}" for r in results))
    print(f"\n(a socket of 1000 int32 is {1000 * 4} bytes)")
    if "--diagnose" in sys.argv:
        diagnose()


def diagnose() -> None:
    n = 20_000
    print(f"\nDiagnosis, N={n}, socket size 1:")
    print(f"{'variant':52s} {'bytes/module':>12s} {'Python objects still alive':>27s}")
    variants = [
        ("Stateful_core", "Python subclass, with a task and a socket"),
        ("empty", "Python subclass, without task"),
        ("task", "Python subclass, task only"),
        ("task+socket", "Python subclass, task and socket, no codelet"),
        ("task+codelet", "Python subclass, task and codelet, no socket"),
        ("base", "Stateful_core itself (no subclass), with a task"),
        ("Stateless", "Stateless (control)"),
    ]
    for kind, label in variants:
        out = subprocess.run([sys.executable, __file__, "--child", kind, str(n), "1"], capture_output=True, text=True)
        if out.returncode != 0:
            print(f"{label:52s} {'crash':>12s}")
            print(out.stderr[-2000:], file=sys.stderr)
            continue
        loss, alive = out.stdout.strip().splitlines()[-1].split()
        print(f"{label:52s} {float(loss):12.0f} {alive:>27s}")


if __name__ == "__main__":
    if len(sys.argv) >= 5 and sys.argv[1] == "--child":
        child(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    else:
        main()
