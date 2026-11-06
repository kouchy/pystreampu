#include "wrapper/Module/Stateless/Stateless.hpp"
#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"
#include "wrapper/Common/Tools/python_codelet.hpp"
#include <pybind11/typing.h>

namespace py = pybind11;
using namespace py::literals;
using namespace spu::module;

void
pyspu::wrapper::wrap_stateless(py::handle scope)
{
    auto stateless_class = py::class_<spu::module::Stateless, spu::module::Module>(scope,"Stateless",py::is_final(),
                                                                                        R"pbdoc(
        Stateless modules are modules that can be cloned automatically.
        )pbdoc");
    stateless_class.def(py::init<>(), "Build an empty module: add tasks with `create_task`.");
    stateless_class.def_property("n_frames_per_wave", &Stateless::get_n_frames_per_wave, &Stateless::set_n_frames_per_wave,
                                 "Number of frames processed by each call of the codelets (by default, all the frames).");

    stateless_class.def(
      "create_socket_in",
      [](Stateless& mdl,
         spu::runtime::Task& task,
         const std::string& name,
         const size_t n_elmts,
         const pyspu::dtype dtype)
      { return mdl.create_socket_in(task, name, n_elmts, pyspu::utils::str2typeid(dtype.get_name())); },
      "task"_a,
      "name"_a,
      "n_elmts"_a,
      "dtype"_a,
      R"pbdoc(
        Create a new input socket to a task.
    )pbdoc");

    stateless_class.def(
      "create_socket_out",
      [](Stateless& mdl,
         spu::runtime::Task& task,
         const std::string& name,
         const size_t n_elmts,
         const pyspu::dtype dtype)
      { return mdl.create_socket_out(task, name, n_elmts, pyspu::utils::str2typeid(dtype.get_name())); },
      "task"_a,
      "name"_a,
      "n_elmts"_a,
      "dtype"_a,
      R"pbdoc(
        Create a new output socket to a task.
    )pbdoc");

    stateless_class.def(
      "create_socket_fwd",
      [](Stateless& mdl,
         spu::runtime::Task& task,
         const std::string& name,
         const size_t n_elmts,
         const pyspu::dtype dtype)
      { return mdl.create_socket_fwd(task, name, n_elmts, pyspu::utils::str2typeid(dtype.get_name())); },
      "task"_a,
      "name"_a,
      "n_elmts"_a,
      "dtype"_a,
      R"pbdoc(
        Create a new forward socket to a task.
    )pbdoc");

    stateless_class.def(
      "create_task",
      [](Stateless& mdl, const std::string& name) { return &mdl.create_task(name); },
      "name"_a,
      R"pbdoc(
        Create a new task.

        Args:
            name (str): name of the task

        Returns:
            Task: newly created task.

    )pbdoc",
      py::return_value_policy::reference);

    stateless_class.def("create_codelet",
      [](Stateless& mdl, spu::runtime::Task& task,
         const py::typing::Callable<int(spu::module::Module&, spu::runtime::Task&, size_t)>& codelet)
      { mdl.create_codelet(task, pyspu::wrapper::python_codelet(codelet)); },
      "task"_a, "codelet"_a, R"pbdoc(
        Set the function executed by a task (its codelet).

        The codelet is called as `codelet(module, task, frame_id)` and must return 0 on
        success. Inside it, the data of the sockets are reached with `task.<name>.numpy`;
        outputs must be written in place (`out[:] = ...`).

        Args:
            task (Task): a task created with `create_task`
            codelet (Callable): the function to execute
    )pbdoc");

    //stateless_class.def("deep_copy", &Stateless::deep_copy);

}
