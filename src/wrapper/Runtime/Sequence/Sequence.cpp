#include "wrapper/Runtime/Sequence/Sequence.hpp"
#include "wrapper/Common/pybind11_common.h"

#include <atomic>
#include <chrono>
#include <functional>
#include <iostream>

#include <streampu.hpp>

namespace py = pybind11;
using namespace py::literals;

void
pyspu::wrapper::wrap_sequence(py::handle scope)
{
    auto sequence_class = py::class_<spu::runtime::Sequence,
                                     spu::tools::Interface_clone,
                                     spu::tools::Interface_get_set_n_frames,
                                     spu::tools::Interface_is_done>(scope, "_Sequence", py::dynamic_attr(), R"pbdoc(
        C++ sequence of StreamPU: a graph of bound tasks, executed on one or several threads.

        Use `streampu.Sequence`, which can also be built from sockets.
    )pbdoc");

    sequence_class.def(py::init<spu::runtime::Task&, const size_t, const bool, const std::string&, bool>(),
                       "first"_a,
                       "n_threads"_a = 1,
                       "thread_pinning"_a = false,
                       "sequence_pinning_policy"_a = std::string(""),
                       "tasks_inplace"_a = true,
                       R"pbdoc(
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
    )pbdoc",
py::return_value_policy::take_ownership);
    sequence_class.def(
      py::init<spu::runtime::Task&, spu::runtime::Task&, const size_t, const bool, const std::string&, bool>(),
      "first"_a,
      "last"_a,
      "n_threads"_a = 1,
      "thread_pinning"_a = false,
      "sequence_pinning_policy"_a = std::string(""),
      "tasks_inplace"_a = true,
      R"pbdoc(
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
    )pbdoc",
py::return_value_policy::take_ownership);
    sequence_class.def(py::init<const std::vector<spu::runtime::Task*>&,
                                const size_t,
                                const bool,
                                const std::string&,
                                const bool>(),
                       "firsts"_a,
                       "n_threads"_a = 1,
                       "thread_pinning"_a = false,
                       "sequence_pinning_policy"_a = std::string(""),
                       "tasks_inplace"_a = true,
                       R"pbdoc(
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
    )pbdoc",
py::return_value_policy::take_ownership);
    sequence_class.def(py::init<const std::vector<spu::runtime::Task*>&,
                                const std::vector<spu::runtime::Task*>&,
                                const std::vector<spu::runtime::Task*>&,
                                const size_t,
                                const bool,
                                const std::string&,
                                const bool>(),
                       "firsts"_a,
                       "lasts"_a,
                       "exclusions"_a,
                       "n_threads"_a = 1,
                       "thread_pinning"_a = false,
                       "sequence_pinning_policy"_a = std::string(""),
                       "tasks_inplace"_a = true,
                       R"pbdoc(
        Build a sequence from its first task(s), and possibly its last tasks and the tasks
        to exclude.

        Args:
            n_threads (int): number of threads; the modules are cloned for each thread
            thread_pinning (bool): pin each thread to a processing unit
            sequence_pinning_policy (str): pinning policy, see the StreamPU documentation
            tasks_inplace (bool): execute the tasks in place when possible
    )pbdoc",
py::return_value_policy::take_ownership);
    /*sequence_class.def(py::init<const std::vector<const spu::runtime::Task *> &,
    const std::vector<const spu::runtime::Task *> &, const std::vector<const
    spu::runtime::Task *> &, const size_t, const bool, const std::vector<size_t>
    &>(), "firsts"_a, "lasts"_a, "exclusions"_a, "n_threads"_a = 1,
    "thread_pinning"_a = false, "puids"_a = std::vector<size_t>());
    sequence_class.def(py::init<const std::vector<spu::runtime::Task *> &, const
    size_t, const bool, const std::vector<size_t> &, const bool>(), "firsts"_a,
    "n_threads"_a = 1, "thread_pinning"_a = false, "puids"_a =
    std::vector<size_t>(), "tasks_inplace"_a = true);
    sequence_class.def(py::init<const std::vector<spu::runtime::Task *> &, const
    std::vector<spu::runtime::Task *> &, const size_t, const bool, const
    std::vector<size_t> &, const bool>(), "firsts"_a, "lasts"_a, "n_threads"_a =
    1, "thread_pinning"_a = false, "sequence_pinning_policy"_a = std::string(""),
    "tasks_inplace"_a = true); sequence_class.def(py::init<const
    std::vector<spu::runtime::Task *> &, const std::vector<spu::runtime::Task *>
    &, const std::vector<spu::runtime::Task *> &, const size_t, const bool, const
    std::vector<size_t> &, const bool>(), "firsts"_a, "lasts"_a, "exclusions"_a,
    "n_threads"_a = 1, "thread_pinning"_a = false, "puids"_a =
    std::vector<size_t>(), "tasks_inplace"_a = true);
    sequence_class.def(py::init<spu::runtime::Task &, const size_t, const bool,
    const std::vector<size_t> &, const bool>(), "first"_a, "n_threads"_a = 1,
    "thread_pinning"_a = false, "sequence_pinning_policy"_a = std::string(""),
    "tasks_inplace"_a = true); sequence_class.def(py::init<spu::runtime::Task &,
    spu::runtime::Task &, const size_t, const bool, const std::vector<size_t> &,
    const bool>(), "first"_a, "last"_a, "n_threads"_a = 1, "thread_pinning"_a =
    false, "sequence_pinning_policy"_a = std::string(""), "tasks_inplace"_a = true);*/
    // sequence_class.def("exec", [](spu::runtime::Sequence& self,
    // std::function<bool(const std::vector<const int*>&)>
    // stop_condition){self.exec(stop_condition);});
    sequence_class.def("exec",
                       [](spu::runtime::Sequence& self)
                       {
                           py::gil_scoped_release release{};
                           self.exec();
                       }, R"pbdoc(
        Execute the sequence until a module of the sequence is done (e.g. a source at the
        end of its file) or SIGINT (Ctrl+C) is received.
    )pbdoc");

    sequence_class.def("exec_n_times",
                       [](spu::runtime::Sequence& self, size_t n_exec)
                       {
                           py::gil_scoped_release release{};
                           std::atomic<size_t> counter(0);
                           self.exec([&counter, n_exec]() { return ++counter >= n_exec; });
                       }, "n_exec"_a, R"pbdoc(
        Execute the sequence `n_exec` times in total, shared between the threads.

        Args:
            n_exec (int): number of executions
    )pbdoc");
    auto sys = py::module::import("sys");
    sequence_class.def("exec",
                       [](spu::runtime::Sequence& self, spu::tools::Terminal_dump& terminal, std::ostream& stream, bool force_report)
                       {
                           py::gil_scoped_release release{};
                           self.exec(
                            [&](const std::vector<const int*>& statuses) -> bool
                            {
                                py::gil_scoped_acquire gil;
                                if (statuses.back() != nullptr || force_report)
                                   terminal.temp_report(stream);
                                return false;
                            });
                       }, "terminal"_a, "stream"_a = sys.attr("stdout"), "force_report"_a = false, R"pbdoc(
        Execute the sequence until a module is done or SIGINT is received, and print a
        report of the probes with `terminal` after each execution.

        Args:
            terminal (Terminal_dump): terminal displaying the reporters
            stream (file): stream where the report is written
            force_report (bool): report after every execution, even when the last task
                did not run
    )pbdoc");
    sequence_class.def("exec_n_times",
                       [](spu::runtime::Sequence& self, size_t n_exec, spu::tools::Terminal_dump& terminal, std::ostream& stream, bool force_report)
                       {
                           py::gil_scoped_release release{};
                           std::atomic<size_t> counter(0);
                           self.exec(
                            [&](const std::vector<const int*>& statuses) -> bool
                            {
                                py::gil_scoped_acquire gil;
                                if (statuses.back() != nullptr || force_report)
                                   terminal.temp_report(stream);
                                return ++counter >= n_exec;
                            });
                       }, "n_exec"_a, "terminal"_a, "stream"_a = sys.attr("stdout"), "force_report"_a = false, R"pbdoc(
        Execute the sequence `n_exec` times and print a report of the probes with
        `terminal` after each execution.

        Args:
            n_exec (int): number of executions
            terminal (Terminal_dump): terminal displaying the reporters
            stream (file): stream where the report is written
            force_report (bool): report after every execution, even when the last task
                did not run
    )pbdoc");

    sequence_class.def("exec_seq",
                       &spu::runtime::Sequence::exec_seq,
                       "tid"_a = 0,
                       "frame_id"_a = -1,
                       py::call_guard<py::gil_scoped_release>(),
                       R"pbdoc(
        Execute the sequence of one thread once, sequentially.

        Args:
            tid (int): index of the thread whose sequence is executed
            frame_id (int): index of the frame to process, or -1 for all the frames
    )pbdoc");
    sequence_class.def("exec_step",
                       &spu::runtime::Sequence::exec_step,
                       "tid"_a = 0,
                       "frame_id"_a = -1,
                       py::return_value_policy::reference,
                       py::call_guard<py::gil_scoped_release>(),
                       R"pbdoc(
        Execute the next task of the sequence of one thread, for step-by-step debugging.

        Args:
            tid (int): index of the thread
            frame_id (int): index of the frame to process, or -1 for all the frames

        Returns:
            out (Task | None): the executed task, or None when a full execution of the
                sequence is over
    )pbdoc");

    sequence_class.def("export_dot",
                       [](spu::runtime::Sequence& self, const std::string& file_name)
                       {
                           std::ofstream f(file_name);
                           self.export_dot(f);
                       }, "file_name"_a, R"pbdoc(
        Export the graph of the sequence in the Graphviz DOT format.

        Args:
            file_name (str): path of the DOT file to write
    )pbdoc");

    sequence_class.def(
      "show_stats",
      [](spu::runtime::Sequence& self, const bool ordered, const bool display_thr, std::ostream& stream)
      {
          spu::tools::Stats::show(self.get_modules_per_types(), ordered, display_thr, stream);
      },
      "ordered"_a = false,
      "display_thr"_a = true,
      "stream"_a = sys.attr("stdout"),
      R"pbdoc(
        Print the statistics of the tasks (enable them first with `task.stats = True`).

        Args:
            ordered (bool): sort the tasks by decreasing duration
            display_thr (bool): display the throughput columns
            stream (file): stream where the statistics are written
    )pbdoc");

    sequence_class.def(
      "get_modules_per_threads", &spu::runtime::Sequence::get_modules_per_threads, py::return_value_policy::reference, "Return the modules of each thread: a list (one per thread) of lists of modules.");
    sequence_class.def(
      "get_modules_per_types", &spu::runtime::Sequence::get_modules_per_types, py::return_value_policy::reference, "Return the modules grouped by type: a list (one per original module) of the modules of all the threads.");
    sequence_class.def(
      "get_tasks_per_threads", &spu::runtime::Sequence::get_tasks_per_threads, py::return_value_policy::reference, "Return the tasks of each thread: a list (one per thread) of lists of tasks.");
    sequence_class.def(
      "get_tasks_per_types", &spu::runtime::Sequence::get_tasks_per_types, py::return_value_policy::reference, "Return the tasks grouped by type: a list (one per original task) of the tasks of all the threads.");

    sequence_class.def_property_readonly(
      "last_tasks", &spu::runtime::Sequence::get_lasts_tasks, py::return_value_policy::reference,
      "Last tasks of the sequence, one list per thread.");
    sequence_class.def_property_readonly(
      "first_tasks", &spu::runtime::Sequence::get_firsts_tasks, py::return_value_policy::reference,
      "First tasks of the sequence, one list per thread.");
    sequence_class.def_property(
      "no_copy_mode", &spu::runtime::Sequence::is_no_copy_mode, &spu::runtime::Sequence::set_no_copy_mode,
      "If True, avoid the data copies between tasks when possible.");
};
