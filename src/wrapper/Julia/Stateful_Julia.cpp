#ifdef SPU_JULIA

#include "wrapper/Common/Tools/socket_creation.hpp"
#include "wrapper/Julia/Julia.hpp"
#include "wrapper/Julia/gc_region.hpp"

namespace py = pybind11;
using namespace py::literals;
using spu::module::Stateful_Julia;

void
pyspu::wrapper::wrap_stateful_julia(py::handle scope)
{
    auto cls = py::class_<Stateful_Julia, spu::module::Stateful, spu::module::Module_Julia>(scope,
                                                                                            "Stateful_Julia",
                                                                                            py::is_final(),
                                                                                            R"pbdoc(
        Module with Julia states whose codelets are written in Julia.

        The codelet of a task is called with the states of the module (in their creation
        order), the sockets of the task, its constants, then `frame_id` and
        `n_frames_per_wave` (see `Module_Julia`). The tasks of a module share its states.
        When a `Sequence` or a `Pipeline` clones the module, each clone gets a `deepcopy`
        of a state, or the same object if the state is shared.
    )pbdoc");

    cls.def(py::init(
              [](const bool jl_safe)
              {
                  spu::tools::Julia::init();
                  return new Stateful_Julia(jl_safe);
              }),
            "jl_safe"_a = true,
            R"pbdoc(
        Build an empty Julia module (starts Julia if needed): add states with
        `create_state` and tasks with `create_task`.

        Args:
            jl_safe (bool): raise the Julia exceptions of the codelets as Python exceptions
    )pbdoc");

    cls.def(
      "create_task",
      [](Stateful_Julia& mdl, const std::string& name) { return &mdl.create_task(name); },
      "name"_a,
      "Create a new task.",
      py::return_value_policy::reference);

    pyspu::wrapper::def_socket_creation<Stateful_Julia>(cls);

    cls.def_property("n_frames_per_wave",
                     &Stateful_Julia::get_n_frames_per_wave,
                     &Stateful_Julia::set_n_frames_per_wave,
                     "Number of frames processed by each call of the codelets (by default, all the frames).");

    // The code that defines the type of a state is evaluated here, not by StreamPU: StreamPU 1.10.0
    // evaluates the code of the codelets before the types of the states, so a codelet whose
    // arguments are typed with a state type (`acc::Acc`) could not be defined. It also reports
    // an error in this code at once.
    cls.def(
      "create_state",
      [](Stateful_Julia& mdl, const std::string& constructor, const bool shared, const std::string& code)
      {
          if (!code.empty())
          {
              pyspu::wrapper::Julia_gc_unsafe_region gc_unsafe;
              spu::tools::Julia::eval_string(code);
              pyspu::wrapper::check_julia_exception("Julia error in the code of the state '" + constructor + "'");
          }
          mdl.create_state(constructor, shared);
      },
      "constructor"_a,
            "shared"_a = false,
            "code"_a = "",
            R"pbdoc(
        Add a state to the module. Create the states before the codelets. The code that
        defines the type of the state is evaluated at once (in the `Main` module of Julia).

        Args:
            constructor (str): Julia expression that builds the state, e.g. `"Acc(0)"`
            shared (bool): False: each clone gets a `deepcopy` of the state; True: the clones
                share the same object
            code (str): Julia code that defines the type of the state
    )pbdoc");

    cls.def(
      "create_state_file",
      [](Stateful_Julia& mdl, const std::string& constructor, const py::object& path, const bool shared)
      {
          const std::string filename = py::str(py::module_::import("os").attr("fspath")(path));
          {
              pyspu::wrapper::Julia_gc_unsafe_region gc_unsafe;
              spu::tools::Julia::eval_file(filename); // see create_state
              pyspu::wrapper::check_julia_exception("Julia error in '" + filename + "'");
          }
          mdl.create_state(constructor, shared);
      },
      "constructor"_a,
      "path"_a,
      "shared"_a = false,
      R"pbdoc(
        Add a state to the module, whose type is defined in a `.jl` file (evaluated at once,
        in the `Main` module of Julia).

        Args:
            constructor (str): Julia expression that builds the state
            path (str | os.PathLike): file that defines the type of the state
            shared (bool): False: each clone gets a `deepcopy` of the state; True: the clones
                share the same object
    )pbdoc");

    cls.def(
      "get_states",
      [](const Stateful_Julia& mdl)
      {
          std::vector<std::string> states;
          for (auto* state : mdl.get_states())
              states.push_back(pyspu::wrapper::julia_repr(state));
          return states;
      },
      R"pbdoc(
        Representation of the states of the module, as `repr` gives it in Julia. The states
        exist once the module has been evaluated.

        Returns:
            list[str]: one string per state
    )pbdoc");
}

#endif /* SPU_JULIA */
