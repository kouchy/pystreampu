"""The Module* returned to Python keep their type (Module_downcast.hpp).

The registry itself is exercised by the extensions (e.g. pyaff3ct registers its abstract bases); here: the hook
keeps the default pybind11 behavior for the classes registered by pystreampu.
"""

import streampu


def test_registry_is_available():
    assert streampu._ext.HAS_MODULE_DOWNCAST_REGISTRY is True


def test_registered_dynamic_types_are_kept():
    src = streampu.source_random(8, dtype=streampu.int32)
    inc = streampu.incrementer(8, dtype=streampu.int32)
    out = inc.increment(src.generate()[0])
    seq = streampu.Sequence(out, n_threads=2)
    for modules in seq.get_modules_per_threads():
        names = sorted(type(m).__name__ for m in modules)
        assert names == sorted([type(src).__name__, type(inc).__name__]), names
