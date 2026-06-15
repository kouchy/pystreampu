#ifndef BIND_MODULE_HPP_
#define BIND_MODULE_HPP_

#include "wrapper/Common/pybind11_common.h"
#include <streampu.hpp>
#include <string>

namespace py = pybind11;


namespace spu
{
namespace module
{
class Module_Trampoline : public Module
{
  public:
    using Module::Module;
    Module* clone() const override
    {
        PYBIND11_OVERRIDE(
          Module*, // return type
          Module,  // parent C++ class
          clone    // method name
        );
    }
};
} // namespace module
} // namespace spu


namespace pyspu
{
namespace wrapper
{
void wrap_module(py::handle scope);
} // namespace wrapper
} // namespace pyspu

#endif // BIND_MODULE_HPP_