#include "wrapper/Module/Stateful/Stateful/Stateful.hpp"
#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"
#include "wrapper/Common/Tools/python_codelet.hpp"
#include <pybind11/typing.h>

namespace py = pybind11;
using namespace py::literals;
using namespace spu::module;

void
pyspu::wrapper::wrap_stateful(py::handle scope)
{
    auto stateful_class = py::class_<spu::module::Stateful, spu::module::Module>(scope, "Stateful", R"pbdoc(Stateful modules are modules that cannot be cloned due to internal state.)pbdoc");

    auto stateful_core_class = py::class_<spu::module::Stateful_core, spu::module::Stateful>(scope, "Stateful_core", R"pbdoc(Stateful_core is the class that will contain the 'core' of python stateful modules. It inherits from Stateful, and implements the clone method by cloning the python state of the Module's body as well as its own state.)pbdoc");

    stateful_core_class.def(py::init<>(), "Build an empty module: add tasks with `create_task`, and implement `clone`.");
    stateful_core_class.def(py::init<const Stateful_core&>(), "Build a copy of another module.");

    stateful_core_class.def_property("n_frames_per_wave", &Stateful::get_n_frames_per_wave, &Stateful_core::set_n_frames_per_wave,
                                     "Number of frames processed by each call of the codelets (by default, all the frames).");

    stateful_core_class.def(
      "create_socket_in",
      [](Stateful_core& mdl,
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

    stateful_core_class.def(
      "create_socket_out",
      [](Stateful_core& mdl,
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

    stateful_core_class.def(
      "create_socket_fwd",
      [](Stateful_core& mdl,
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

    stateful_core_class.def(
      "create_task",
      [](Stateful_core& mdl, const std::string& name)
      {
          // Lets `clone()` know that StreamPU only checks whether the module is clonable
          mdl.set_creating_task(true);
          try
          {
              auto* task = &mdl.create_task(name);
              mdl.set_creating_task(false);
              return task;
          }
          catch (...)
          {
              mdl.set_creating_task(false);
              throw;
          }
      },
      "name"_a,
      R"pbdoc(
        Create a new task.

        Args:
            name (str): name of the task

        Returns:
            Task: newly created task.

    )pbdoc",
      py::return_value_policy::reference);

    stateful_core_class.def(
      "create_codelet",
      [](py::handle mdl_h, spu::runtime::Task& task, py::object codelet)
      {
          if (codelet.is_none())
          {
              auto& mdl = mdl_h.cast<Stateful_core&>();
              pyspu::wrapper::register_empty_cpp_codelet(mdl, task, 0);
              return;
          }
          // Fast path: if `codelet` is a `spu.numba_codelet` descriptor or a Numba `@njit`
          // `CPUDispatcher` (detected via its `py_func` and `overloads` attributes), compile a
          // GIL-free `@cfunc` trampoline and bind its C function pointer via `create_codelet_cfunc`.
          if (py::hasattr(codelet, "_is_numba_codelet") ||
              (py::hasattr(codelet, "py_func") && py::hasattr(codelet, "overloads")))
          {
              py::module_::import("streampu._numba")
                .attr("register_numba_codelet")(mdl_h, py::cast(&task, py::return_value_policy::reference), codelet);
              return;
          }
          auto& mdl = mdl_h.cast<Stateful_core&>();
          mdl.create_codelet(task, pyspu::wrapper::python_codelet(codelet.cast<py::function>()));
      },
      "task"_a,
      "codelet"_a = py::none(),
      R"pbdoc(
        Set the function executed by a task (its codelet).

        The codelet is called as `codelet(module, task, frame_id)` and must return 0 on
        success. Inside it, the data of the sockets are reached with `task.<name>.numpy`;
        outputs must be written in place (`out[:] = ...`).
        Alternatively, `codelet` may be a Numba `@njit` function taking the task's data
        sockets as 2D NumPy views (`wave`), a `streampu.numba_codelet(...)` descriptor,
        or `None` to bind a native C++ empty codelet.

        Args:
            task (Task): a task created with `create_task`
            codelet (Callable | None): the function to execute
    )pbdoc");

    stateful_core_class.def(
      "create_codelet_empty",
      [](Stateful_core& mdl, spu::runtime::Task& task, const int capture_mode)
      { pyspu::wrapper::register_empty_cpp_codelet(mdl, task, capture_mode); },
      "task"_a,
      "capture_mode"_a = 0,
      "Register a native C++ empty codelet on `task` (for runtime overhead benchmarking).");

    stateful_core_class.def(
      "create_codelet_cfunc",
      [](Stateful_core& mdl,
         spu::runtime::Task& task,
         const uintptr_t cfunc_addr,
         py::object keep_alive,
         py::object extra_args_packer)
      {
          pyspu::wrapper::register_numba_cfunc_codelet(
            mdl, task, cfunc_addr, std::move(keep_alive), std::move(extra_args_packer));
      },
      "task"_a,
      "cfunc_addr"_a,
      "keep_alive"_a = py::none(),
      "extra_args_packer"_a = py::none());

    stateful_core_class.def("clone", [](const Stateful_core& self) -> py::object {
        py::function py_clone = py::get_override(&self, "clone");
        if (py_clone) {
            return py_clone();                          // py::object complet ✓
        }
        // fallback : instance C++ pure
        return py::cast(self.Stateful::clone());
    }, py::return_value_policy::take_ownership, R"pbdoc(
        Return a copy of the module, used to duplicate it on several threads.

        Override it in Python subclasses: create the new instance without calling
        `__init__` (StreamPU copies the tasks, sockets and codelets) and copy the Python
        state.

        Returns:
            out (Stateful_core): the copy
    )pbdoc");
}
