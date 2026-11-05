#ifndef WRAPPER_JULIA_HPP_
#define WRAPPER_JULIA_HPP_

#include "wrapper/Common/pybind11_common.h"
#include <streampu.hpp>

#ifdef SPU_JULIA
#include <julia.h>
#endif

namespace py = pybind11;

namespace pyspu
{
namespace wrapper
{
#ifdef SPU_JULIA
// Bindings of the Julia support of StreamPU (compiled with -DSPU_LINK_JULIA=ON), in the
// submodule `streampu._ext.jl`
void
wrap_julia(py::handle scope);
void
wrap_module_julia(py::handle scope);
void
wrap_stateless_julia(py::handle scope);
void
wrap_stateful_julia(py::handle scope);

// Throw a Python RuntimeError if the last call to the Julia C API raised a Julia exception
// (the C API does not throw: it returns NULL and keeps the exception).
void
check_julia_exception(const std::string& context);

// Representation of a Julia value, as `repr` gives it in Julia
std::string
julia_repr(jl_value_t* value);
#endif
} // namespace wrapper
} // namespace pyspu

#endif // WRAPPER_JULIA_HPP_
