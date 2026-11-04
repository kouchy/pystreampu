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
    bool cloned = false;
    // True while a task is created (see `create_task` in Stateful.cpp and `clone`)
    bool creating_task = false;

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
    void set_creating_task(const bool creating_task) { this->creating_task = creating_task; }

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
            // While a task is created, StreamPU calls `Module::is_clonable()`, which only checks
            // that `clone()` succeeds and deletes the clone at once. Answer without running the
            // Python `clone()` (costly, and possibly called before the Python state is set): an
            // empty module, never used, is enough.
            if (this->creating_task) return new Stateful_core();

            py::object result = py_clone();
            // The clone is owned by C++ (StreamPU deletes it), but it lives in a Python object
            // that holds the Python state of the module. This reference keeps the Python object
            // alive as long as the clone; it is released by the destructor (see below).
            result.inc_ref();
            auto owned = py::cast<Stateful_core*>(std::move(result));
            owned->set_cloned(true);
            owned->deep_copy(*this); // deep copy C++ state
            return owned; // release ownership to return a raw pointer, since clone() returns a raw pointer
        } // else should throw ?
        throw spu::tools::unimplemented_error(__FILE__, __LINE__, __func__, "clone_python_state method not implemented in python subclass of Stateful_core");
    };

    // No custom `operator delete`: the memory of the modules is released normally. (A previous
    // version did not release it, which leaked about 600 bytes per module, and called
    // `dec_ref()` on objects that were already destroyed.)

    ~Stateful_core()
    {
        if (!this->cloned) return; // an original module is owned (and deleted) by its Python object

        // A clone is deleted by StreamPU: by a sequence, or right after its creation by
        // `Module::is_clonable()`, which StreamPU calls for each created task. Detach the C++
        // object from its Python object, so that the latter does not delete it a second time,
        // then release the reference taken by `clone()`: the Python object is freed.
        py::gil_scoped_acquire gil;
        auto* tinfo = py::detail::get_type_info(typeid(Stateful_core));
        if (tinfo == nullptr) return;
        py::handle self = py::detail::get_object_handle(this, tinfo);
        if (!self) return;
        auto* inst = reinterpret_cast<py::detail::instance*>(self.ptr());
        auto v_h = inst->get_value_and_holder(tinfo, false);
        if (!v_h) return;
        if (v_h.instance_registered())
        {
            py::detail::deregister_instance(inst, v_h.value_ptr(), tinfo);
            v_h.set_instance_registered(false);
        }
        if (v_h.holder_constructed())
        {
            v_h.holder<std::unique_ptr<Stateful_core>>().release();
            v_h.set_holder_constructed(false);
        }
        v_h.value_ptr() = nullptr; // nothing left to delete for pybind11
        self.dec_ref();
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
