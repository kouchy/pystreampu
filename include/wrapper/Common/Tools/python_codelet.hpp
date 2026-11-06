#ifndef WRAPPER_PYTHON_CODELET_HPP_
#define WRAPPER_PYTHON_CODELET_HPP_

#include <functional>
#include <memory>

#include "wrapper/Common/pybind11_common.h"
#include "wrapper/Julia/gc_region.hpp"
#include <streampu.hpp>

namespace pyspu
{
namespace wrapper
{
// C++ codelet that calls a Python function `codelet(module, task, frame_id) -> int`.
//
// It replaces the conversion of pybind11 (which only takes the GIL) to enter a GC-safe region
// of Julia first, when the thread is adopted by Julia (see gc_region.hpp): a Python codelet can
// then run in the same Sequence or Pipeline as Julia modules. The Python function is released
// with the GIL, whichever thread deletes the last copy of the codelet.
inline std::function<int(spu::module::Module&, spu::runtime::Task&, const size_t)>
python_codelet(const pybind11::function& codelet)
{
    namespace py = pybind11;
    auto function = std::shared_ptr<py::function>(new py::function(codelet),
                                                  [](py::function* f)
                                                  {
                                                      py::gil_scoped_acquire gil;
                                                      delete f;
                                                  });
    return [function](spu::module::Module& m, spu::runtime::Task& t, const size_t frame_id) -> int
    {
        pyspu::wrapper::Julia_gc_safe_region gc_safe;
        py::gil_scoped_acquire gil;
        py::object result = (*function)(py::cast(&m, py::return_value_policy::reference),
                                        py::cast(&t, py::return_value_policy::reference),
                                        frame_id);
        return result.cast<int>();
    };
}
} // namespace wrapper
} // namespace pyspu

#endif // WRAPPER_PYTHON_CODELET_HPP_
