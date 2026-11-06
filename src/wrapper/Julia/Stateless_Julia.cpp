#ifdef SPU_JULIA

#include "wrapper/Common/Tools/socket_creation.hpp"
#include "wrapper/Julia/Julia.hpp"

namespace py = pybind11;
using namespace py::literals;
using spu::module::Stateless_Julia;

void
pyspu::wrapper::wrap_stateless_julia(py::handle scope)
{
    auto cls = py::class_<Stateless_Julia, spu::module::Module, spu::module::Module_Julia>(scope,
                                                                                           "Stateless_Julia",
                                                                                           py::is_final(),
                                                                                           R"pbdoc(
        Module without state whose codelets are written in Julia.

        The codelet of a task is called with the sockets of the task, its constants, then
        `frame_id` and `n_frames_per_wave` (see `Module_Julia`).
    )pbdoc");

    cls.def(py::init(
              [](const bool jl_safe)
              {
                  pyspu::wrapper::julia_init();
                  return new Stateless_Julia(jl_safe);
              }),
            "jl_safe"_a = true,
            R"pbdoc(
        Build an empty Julia module (starts Julia if needed): add tasks with `create_task`.

        Args:
            jl_safe (bool): raise the Julia exceptions of the codelets as Python exceptions
    )pbdoc");

    cls.def(
      "create_task",
      [](Stateless_Julia& mdl, const std::string& name) { return &mdl.create_task(name); },
      "name"_a,
      "Create a new task.",
      py::return_value_policy::reference);

    pyspu::wrapper::def_socket_creation<Stateless_Julia>(cls);

    cls.def_property("n_frames_per_wave",
                     &Stateless_Julia::get_n_frames_per_wave,
                     &Stateless_Julia::set_n_frames_per_wave,
                     "Number of frames processed by each call of the codelets (by default, all the frames).");
}

#endif /* SPU_JULIA */
