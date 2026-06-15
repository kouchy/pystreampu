#ifndef WRAPPER_STATEFUL_HPP_
#define WRAPPER_STATEFUL_HPP_

#include "wrapper/Common/pybind11_common.h"
#include <streampu.hpp>

namespace py = pybind11;

namespace spu
{
namespace module
{
// Stateful_core is the class that will contain the 'core' of python stateful modules.
// It inherits from Stateful, and implements the clone method by cloning the python state of the Module's body as well as its own state.
class Stateful_core : public Stateful
{
  protected:
    bool cloned = false;;
  public:
    Stateful_core()
    : Stateful()
    {
    };

    Stateful_core(const Stateful_core& other)
    : Stateful(other)
    {
    };

    void set_cloned(const bool cloned) { this->cloned = cloned; }
    bool is_cloned() const { return cloned; }

    using Stateful::create_codelet;
    using Stateful::create_socket_fwd;
    using Stateful::create_socket_in;
    using Stateful::create_socket_out;
    using Stateful::create_task;
    using Stateful::set_n_frames_per_wave;
    using Stateful::deep_copy;

    Stateful_core* clone() const override
    {
        py::gil_scoped_acquire gil;

        py::function py_clone = py::get_override(this, "clone");
        if (py_clone) {
            py::object result = py_clone();
            result.inc_ref(); // increase ref count to ensure the object is not destroyed when owned goes out of scope
            auto owned = py::cast<Stateful_core*>(std::move(result));
            py::print("Cloning ", py::int_(reinterpret_cast<uintptr_t>(this)), " -> ", py::int_(reinterpret_cast<uintptr_t>(owned)));
            owned->set_cloned(true);
            owned->deep_copy(*this); // deep copy C++ state
            return owned; // release ownership to return a raw pointer, since clone() returns a raw pointer
        } // else should throw ?
        throw spu::tools::unimplemented_error(__FILE__, __LINE__, __func__, "clone_python_state method not implemented in python subclass of Stateful_core");
    };

    static void operator delete(void* ptr) {
        py::gil_scoped_acquire gil;

        Stateful_core* self = static_cast<Stateful_core*>(ptr);
        py::handle h = py::cast(self);
        h.dec_ref();  // compense le inc_ref() fait dans clone()
    }

    ~Stateful_core(){
        py::gil_scoped_acquire gil;
        py::print("Stateful_core destructor called for object at address:",  py::int_(reinterpret_cast<uintptr_t>(this)));
    };
};
} // namespace module
} // namespace spu

namespace pyspu
{
namespace wrapper
{
void
wrap_stateful(py::handle scop);
}
} // namespace pyspu
#endif // WRAPPER_STATEFUL_HPP_
