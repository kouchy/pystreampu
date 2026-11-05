#include "wrapper/Runtime/Task/Task.hpp"
#include "wrapper/Module/Stateful/Array/Array.hpp"
#include "wrapper/Runtime/Socket/Socket.hpp"
#include "wrapper/Julia/gc_region.hpp"

#include <chrono>
#include <rang.hpp>

#include "wrapper/Common/pybind11_common.h"

namespace py = pybind11;
using namespace py::literals;
using namespace spu::module;
using namespace pyspu::wrapper;
using namespace spu::runtime;

void
pyspu::wrapper::wrap_task(py::handle scope)
{
    py::class_<spu::runtime::Task> py_task(scope, "Task", R"pbdoc(
        A processing step of a module: the code executed by a node of the data-flow graph.

        A task reads its input sockets, writes its output sockets and modifies its forward
        sockets. Its sockets are reached by name: `task["name"]` or `task.name`.

        Calling a task, `task(*sockets)`, binds the given sockets to its input and forward
        sockets (in the order of `task.sockets`), executes it once and returns its output
        sockets (without `status`).
    )pbdoc");

    py::enum_<status_t>(py_task, "Status", "Enumeration of tasks return code.")
      .value("SUCCESS", status_t::SUCCESS, "Success code")
      .value("FAILURE", status_t::FAILURE, "Failure code")
      .value("FAILURE_STOP", status_t::FAILURE_STOP, "Failure stop code")
      .value("UNKNOWN", status_t::UNKNOWN, "Unknown code");

    py_task.def_property_readonly("name", &spu::runtime::Task::get_name, "Name of the task.");
    py_task.def_property_readonly("sockets",
                                  [](spu::runtime::Task& t)
                                  {
                                      std::vector<spu::runtime::Socket*> sckts;

                                      for (auto s : t.sockets)
                                          sckts.push_back(s.get());
                                      return sckts;
                                  },
                                  "All the sockets of the task, in their order of creation.");

    py_task.def("can_exec", &spu::runtime::Task::can_exec, R"pbdoc(
        Tell whether the task can be executed.

        Returns:
            out (bool): True if every socket of the task has data (input sockets bound,
                output sockets allocated)
    )pbdoc");

    py_task.def("interrupt_processing", [](spu::runtime::Task& t) { throw spu::tools::processing_aborted(); }, R"pbdoc(
        Raise a `ProcessingAborted` exception (same as `abort_processing`).

        Raises:
            ProcessingAborted: always
    )pbdoc");

    py_task.def_property_readonly("inputs",
                                  [](spu::runtime::Task& t)
                                  {
                                      std::vector<spu::runtime::Socket*> in;

                                      for (auto s : t.sockets)
                                          if (s->get_type() == spu::runtime::socket_t::SIN) in.push_back(s.get());

                                      return in;
                                  },
                                  "Input sockets of the task.");

    py_task.def_property_readonly("forwards",
                                  [](spu::runtime::Task& t)
                                  {
                                      std::vector<spu::runtime::Socket*> fwd;

                                      for (auto s : t.sockets)
                                          if (s->get_type() == spu::runtime::socket_t::SFWD) fwd.push_back(s.get());

                                      return fwd;
                                  },
                                  "Forward sockets of the task.");

    py_task.def_property_readonly("outputs",
                                  [](spu::runtime::Task& t)
                                  {
                                      std::vector<spu::runtime::Socket*> out;
                                      auto sockets = t.sockets;
                                      for (auto s : t.sockets)
                                          if (s->get_type() == spu::runtime::socket_t::SOUT) out.push_back(s.get());
                                      return out;
                                  },
                                  "Output sockets of the task, including `status`.");

    py_task.def("exec",
      [](spu::runtime::Task& self, const int frame_id, const bool managed_memory)
      {
          py::scoped_ostream_redirect stream(std::cout,                                // std::ostream&
                                             py::module_::import("sys").attr("stdout") // Python output
          );
          // setControlMode(rang::control::Force);
#ifdef SPU_JULIA
          // A Julia module is evaluated by a Sequence or a Pipeline for each of its threads;
          // for an immediate execution, evaluate it here, at its first execution
          if (auto* mj = dynamic_cast<spu::module::Module_Julia*>(&self.get_module()))
              if (!mj->is_eval())
              {
                  pyspu::wrapper::Julia_gc_unsafe_region gc_unsafe;
                  mj->eval();
              }
#endif
          self.exec(frame_id, managed_memory);
      },
      "frame_id"_a = -1,
      "managed_memory"_a = true,
      R"pbdoc(
        Execute the task once.

        Args:
            frame_id (int): index of the frame to process, or -1 to process all the frames
                of the module (`n_frames`)
            managed_memory (bool): let StreamPU manage the memory of the sockets

        Raises:
            RuntimeError: if some sockets have no data (see `can_exec`)
    )pbdoc");
    py_task.def("__getitem__",
                [](spu::runtime::Task& t, const std::string& s)
                {
                    auto& m = t.get_module();
                    return py::cast(&m[t.get_name() + "::" + s]);
                }, py::is_operator());
    py_task.def_property_readonly("module", &spu::runtime::Task::get_module, "Module that owns the task.");
    py_task.def_property("debug", &spu::runtime::Task::is_debug, &spu::runtime::Task::set_debug,
                         "If True, print the content of the sockets at each execution.");
    py_task.def_property("stats", &spu::runtime::Task::is_stats, &spu::runtime::Task::set_stats,
                         "If True, measure the duration of each execution (see `avg_duration`...).");
    py_task.def_property("fast", &spu::runtime::Task::is_fast, &spu::runtime::Task::set_fast,
                         "If True, skip some checks at each execution, for speed.");
    py_task.def_property_readonly("n_calls", &spu::runtime::Task::get_n_calls, "Number of executions since the last `reset`.");
    py_task.def_property_readonly("total_duration",
                                  [](const spu::runtime::Task& self)
                                  {
                                      if (self.is_stats())
                                          return std::chrono::duration<double>(self.get_duration_total()).count();
                                      else
                                          return double(0.0f);
                                  },
                                  "Total time spent in the task, in seconds (0 if `stats` is False).");
    py_task.def_property_readonly("avg_duration",
                                  [](const spu::runtime::Task& self)
                                  {
                                      if (self.is_stats())
                                          return std::chrono::duration<double>(self.get_duration_avg()).count();
                                      else
                                          return double(0.0f);
                                  },
                                  "Average duration of an execution, in seconds (0 if `stats` is False).");
    py_task.def_property_readonly("min_duration",
                                  [](const spu::runtime::Task& self)
                                  {
                                      if (self.is_stats())
                                          return std::chrono::duration<double>(self.get_duration_min()).count();
                                      else
                                          return double(0.0f);
                                  },
                                  "Minimum duration of an execution, in seconds (0 if `stats` is False).");
    py_task.def_property_readonly("max_duration",
                                  [](const spu::runtime::Task& self)
                                  {
                                      if (self.is_stats())
                                          return std::chrono::duration<double>(self.get_duration_max()).count();
                                      else
                                          return double(0.0f);
                                  },
                                  "Maximum duration of an execution, in seconds (0 if `stats` is False).");
    py_task.def("reset", &spu::runtime::Task::reset, "Reset the statistics of the task (`n_calls`, durations).");
    py_task.def(
      "bind",
      [](spu::runtime::Task& self, spu::runtime::Socket& s_out, const int priority) { self.bind(s_out, priority); },
      R"pbdoc(
        Bind the task to a socket, to force an order of execution without exchanging data.

        The task will be executed after the task that owns `s_out`.

        Args:
            s_out (Socket): an output or forward socket of another task
            priority (int): priority of the binding, -1 for the default one
    )pbdoc",
      "s_out"_a,
      "priority"_a = -1);
    py_task.def(
      "bind",
      [](spu::runtime::Task& self, spu::runtime::Task& t_out, const int priority) { self.bind(t_out, priority); },
      R"pbdoc(
        Bind the task to another task, to force an order of execution without exchanging data.

        Args:
            t_out (Task): the task to execute before this one
            priority (int): priority of the binding, -1 for the default one
    )pbdoc",
      "t_out"_a,
      "priority"_a = -1);

    py_task.def("is_bound",[](spu::runtime::Task& self){
      return self.fake_input_sockets.size() > 0;
    }, R"pbdoc(
        Tell whether the task is bound to another task or socket with `bind`.

        Returns:
            out (bool): True if the task has been bound with `Task.bind`
    )pbdoc");
    py_task.def("set_debug_hex", &spu::runtime::Task::set_debug_hex, "debug_hex"_a, R"pbdoc(
        Print the data in hexadecimal in debug mode.

        Args:
            debug_hex (bool): True to print in hexadecimal
    )pbdoc");
    py_task.def("set_debug_limit", &spu::runtime::Task::set_debug_limit, "limit"_a, R"pbdoc(
        Set the maximum number of elements printed per socket in debug mode.

        Args:
            limit (int): maximum number of elements
    )pbdoc");
    py_task.def("set_debug_precision", &spu::runtime::Task::set_debug_precision, "prec"_a, R"pbdoc(
        Set the number of decimals of the floating-point values printed in debug mode.

        Args:
            prec (int): number of decimals
    )pbdoc");
    py_task.def("set_debug_frame_max", &spu::runtime::Task::set_debug_frame_max, "limit"_a, R"pbdoc(
        Set the maximum number of frames printed in debug mode.

        Args:
            limit (int): maximum number of frames
    )pbdoc");
    py_task.def("abort_processing",[](spu::runtime::Task& self){
        throw spu::tools::processing_aborted(__FILE__, __LINE__, __func__);
    }, R"pbdoc(
        Raise a `ProcessingAborted` exception, to stop the processing from a codelet.

        Raises:
            ProcessingAborted: always
    )pbdoc");
    py_task.def("cancel_waiting",[](spu::runtime::Task& self){
        throw spu::tools::waiting_canceled(__FILE__, __LINE__, __func__);
    }, R"pbdoc(
        Raise a `WaitingCanceled` exception, to stop a task that waits for data.

        Raises:
            WaitingCanceled: always
    )pbdoc");
    py_task.def_property("replicable", &spu::runtime::Task::is_replicable, &spu::runtime::Task::set_replicability,
                         "If True, the task can be duplicated on several threads (its module must be clonable).");
};
