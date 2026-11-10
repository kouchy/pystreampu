#include "wrapper/Runtime/Sequence/Sequence.hpp"
#include "wrapper/Julia/gc_region.hpp"
#include "wrapper/Common/pybind11_common.h"
#include "wrapper/Common/Tools/python_codelet.hpp"

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
                       [](spu::runtime::Sequence& self, size_t n_exec, const bool with_statuses, const bool per_thread)
                       {
                           py::gil_scoped_release release{};
                           const size_t n_threads = self.get_n_threads();
                           if (n_threads == 1)
                           {
                               size_t counter = 0;
                               if (!with_statuses)
                                   self.exec([&counter, n_exec]() { return ++counter >= n_exec; });
                               else
                                   self.exec([&counter, n_exec](const std::vector<const int*>&)
                                             { return ++counter >= n_exec; });
                           }
                           else if (per_thread)
                           {
                               const size_t n_per_thread = std::max<size_t>(1, n_exec / n_threads);
                               if (!with_statuses)
                                   self.exec(
                                     [n_per_thread]()
                                     {
                                         thread_local size_t tl_c = 0;
                                         if (++tl_c >= n_per_thread)
                                         {
                                             tl_c = 0;
                                             return true;
                                         }
                                         return false;
                                     });
                               else
                                   self.exec(
                                     [n_per_thread](const std::vector<const int*>&)
                                     {
                                         thread_local size_t tl_c = 0;
                                         if (++tl_c >= n_per_thread)
                                         {
                                             tl_c = 0;
                                             return true;
                                         }
                                         return false;
                                     });
                           }
                           else
                           {
                               std::atomic<size_t> counter(0);
                               if (!with_statuses)
                                   self.exec([&counter, n_exec]() { return ++counter >= n_exec; });
                               else
                                   self.exec([&counter, n_exec](const std::vector<const int*>&)
                                             { return ++counter >= n_exec; });
                           }
                       },
                       "n_exec"_a,
                       "with_statuses"_a = false,
                       "per_thread"_a = false,
                       R"pbdoc(
        Execute the sequence `n_exec` times in total, shared between the threads.

        Args:
            n_exec (int): number of executions
            with_statuses (bool): if True, use the status-collecting execution loop (`_exec`)
            per_thread (bool): if True and `n_threads > 1`, each thread executes `n_exec / n_threads`
                iterations using a thread-local counter without shared atomic contention
    )pbdoc");

    sequence_class.def_static(
      "bench_bare_cpp_call",
      [](const size_t n_exec,
         const size_t n_tasks,
         const bool collect_rt_percentiles,
         const size_t n_warmup,
         const size_t rt_skip) -> py::dict
      {
          double dt_ns = 0.0;
          double dt_ticks = 0.0;
          double std_ns = 0.0;
          double p50_ns = 0.0;
          double p99_ns = 0.0;
          double p999_ns = 0.0;
          double p9999_ns = 0.0;
          double max_ns = 0.0;
          {
              py::gil_scoped_release release{};
              for (size_t i = 0; i < n_warmup; ++i)
                  for (size_t t = 0; t < n_tasks; ++t)
                      pyspu::wrapper::empty_kernel_0(t);
              const auto t0_clk = std::chrono::steady_clock::now();
              const uint64_t t0_tsc = spu::tools::read_tsc();
              for (size_t i = 0; i < n_exec; ++i)
                  for (size_t t = 0; t < n_tasks; ++t)
                      pyspu::wrapper::empty_kernel_0(t);
              const uint64_t t1_tsc = spu::tools::read_tsc();
              const auto t1_clk = std::chrono::steady_clock::now();
              dt_ns = static_cast<double>(
                std::chrono::duration_cast<std::chrono::nanoseconds>(t1_clk - t0_clk).count());
              dt_ticks = static_cast<double>(t1_tsc - t0_tsc);
              const double ns_per_tick = (dt_ticks > 0.0) ? (dt_ns / dt_ticks) : 1.0;

              if (collect_rt_percentiles)
              {
                  spu::tools::Rt_stats raw_stats;
                  for (size_t i = 0; i < n_exec; ++i)
                  {
                      const uint64_t s0 = spu::tools::read_tsc();
                      for (size_t t = 0; t < n_tasks; ++t)
                          pyspu::wrapper::empty_kernel_0(t);
                      const uint64_t s1 = spu::tools::read_tsc();
                      if (i >= rt_skip) raw_stats.add_sample(s1 - s0);
                  }
                  std_ns = raw_stats.get_std_ticks() * ns_per_tick;
                  p50_ns = raw_stats.get_percentile_ticks(50.0) * ns_per_tick;
                  p99_ns = raw_stats.get_percentile_ticks(99.0) * ns_per_tick;
                  p999_ns = raw_stats.get_percentile_ticks(99.9) * ns_per_tick;
                  p9999_ns = raw_stats.get_percentile_ticks(99.99) * ns_per_tick;
                  max_ns = static_cast<double>(raw_stats.max_ticks) * ns_per_tick;
              }
          }
          const double ns_per_frame = dt_ns / static_cast<double>(n_exec);
          const double ns_per_task = ns_per_frame / static_cast<double>(n_tasks);
          const double ticks_per_frame = dt_ticks / static_cast<double>(n_exec);
          const double ticks_per_task = ticks_per_frame / static_cast<double>(n_tasks);

          py::dict d;
          d["n_tasks"] = n_tasks;
          d["ns_per_frame"] = ns_per_frame;
          d["ns_per_task"] = ns_per_task;
          d["ticks_per_frame"] = ticks_per_frame;
          d["ticks_per_task"] = ticks_per_task;
          d["std_ns_per_frame"] = std_ns;
          d["p50_ns_per_frame"] = p50_ns;
          d["p99_ns_per_frame"] = p99_ns;
          d["p999_ns_per_frame"] = p999_ns;
          d["p9999_ns_per_frame"] = p9999_ns;
          d["max_ns_per_frame"] = max_ns;
          return d;
      },
      "n_exec"_a,
      "n_tasks"_a = 8,
      "collect_rt_percentiles"_a = false,
      "n_warmup"_a = 256,
      "rt_skip"_a = 0,
      "Run `n_exec * n_tasks` bare C++ noinline `empty_kernel_0` calls and return latency/RT statistics.");

    sequence_class.def(
      "measure_bench",
      [](spu::runtime::Sequence& self,
         const size_t n_exec,
         const bool collect_rt_percentiles,
         const size_t n_warmup,
         const size_t rt_skip,
         const bool with_statuses,
         const size_t task_divisor_override,
         const bool per_thread) -> py::dict
      {
          const size_t n_tasks = task_divisor_override ? task_divisor_override : self.get_tasks_per_types().size();
          const size_t n_threads = std::max<size_t>(1, self.get_n_threads());

          double ns_per_frame = -1.0;
          double ns_per_task = -1.0;
          double ticks_per_frame = 0.0;
          double ticks_per_task = 0.0;
          double std_ns_per_frame = 0.0;
          double p50_ns_per_frame = 0.0;
          double p99_ns_per_frame = 0.0;
          double p999_ns_per_frame = 0.0;
          double p9999_ns_per_frame = 0.0;
          double max_ns_per_frame = 0.0;

          {
              py::gil_scoped_release release{};
              self.set_rt_stats(false);

              if (per_thread && n_threads > 1)
              {
                  if (n_warmup > 0)
                  {
                      std::atomic<size_t> w_cnt(0);
                      if (!with_statuses)
                          self.exec([&w_cnt, n_warmup]() { return ++w_cnt >= n_warmup; });
                      else
                          self.exec([&w_cnt, n_warmup](const std::vector<const int*>&) { return ++w_cnt >= n_warmup; });
                  }

                  std::atomic<size_t> cnt(0);
                  const auto t0_clk = std::chrono::steady_clock::now();
                  const uint64_t t0_tsc = spu::tools::read_tsc();
                  if (!with_statuses)
                      self.exec([&cnt, n_exec]() { return ++cnt >= n_exec; });
                  else
                      self.exec([&cnt, n_exec](const std::vector<const int*>&) { return ++cnt >= n_exec; });
                  const uint64_t t1_tsc = spu::tools::read_tsc();
                  const auto t1_clk = std::chrono::steady_clock::now();

                  const double dt_ns = static_cast<double>(
                    std::chrono::duration_cast<std::chrono::nanoseconds>(t1_clk - t0_clk).count());
                  const double dt_ticks = static_cast<double>(t1_tsc - t0_tsc);
                  ns_per_frame = dt_ns / static_cast<double>(n_exec);
                  ns_per_task = ns_per_frame / static_cast<double>(n_tasks);
                  ticks_per_frame = dt_ticks / static_cast<double>(n_exec);
                  ticks_per_task = ticks_per_frame / static_cast<double>(n_tasks);

                  if (collect_rt_percentiles)
                  {
                      self.reset_rt_stats();
                      self.set_rt_stats(true, rt_skip);
                      std::atomic<size_t> c2(0);
                      if (!with_statuses)
                          self.exec([&c2, n_exec]() { return ++c2 >= n_exec; });
                      else
                          self.exec([&c2, n_exec](const std::vector<const int*>&) { return ++c2 >= n_exec; });

                      spu::tools::Rt_stats st;
                      for (const auto& s : self.get_rt_stats_per_thread())
                          st.merge(s);
                      const double ns_per_tick = self.get_rt_ns_per_tick() / static_cast<double>(n_threads);
                      self.set_rt_stats(false);

                      std_ns_per_frame = st.get_std_ticks() * ns_per_tick;
                      p50_ns_per_frame = st.get_percentile_ticks(50.0) * ns_per_tick;
                      p99_ns_per_frame = st.get_percentile_ticks(99.0) * ns_per_tick;
                      p999_ns_per_frame = st.get_percentile_ticks(99.9) * ns_per_tick;
                      p9999_ns_per_frame = st.get_percentile_ticks(99.99) * ns_per_tick;
                      max_ns_per_frame = static_cast<double>(st.max_ticks) * ns_per_tick;
                  }
              }
              else
              {
                  if (n_warmup > 0)
                  {
                      size_t w = 0;
                      if (!with_statuses)
                          self.exec([&w, n_warmup]() { return ++w >= n_warmup; });
                      else
                          self.exec([&w, n_warmup](const std::vector<const int*>&) { return ++w >= n_warmup; });
                  }

                  size_t c1 = 0;
                  const auto t0_clk = std::chrono::steady_clock::now();
                  const uint64_t t0_tsc = spu::tools::read_tsc();
                  if (!with_statuses)
                      self.exec([&c1, n_exec]() { return ++c1 >= n_exec; });
                  else
                      self.exec([&c1, n_exec](const std::vector<const int*>&) { return ++c1 >= n_exec; });
                  const uint64_t t1_tsc = spu::tools::read_tsc();
                  const auto t1_clk = std::chrono::steady_clock::now();

                  const double dt_ns = static_cast<double>(
                    std::chrono::duration_cast<std::chrono::nanoseconds>(t1_clk - t0_clk).count());
                  const double dt_ticks = static_cast<double>(t1_tsc - t0_tsc);
                  ns_per_frame = dt_ns / static_cast<double>(n_exec);
                  ns_per_task = ns_per_frame / static_cast<double>(n_tasks);
                  ticks_per_frame = dt_ticks / static_cast<double>(n_exec);
                  ticks_per_task = ticks_per_frame / static_cast<double>(n_tasks);

                  if (collect_rt_percentiles)
                  {
                      self.reset_rt_stats();
                      self.set_rt_stats(true, rt_skip);
                      size_t c2 = 0;
                      if (!with_statuses)
                          self.exec([&c2, n_exec]() { return ++c2 >= n_exec; });
                      else
                          self.exec([&c2, n_exec](const std::vector<const int*>&) { return ++c2 >= n_exec; });

                      const auto& st = self.get_rt_stats_per_thread()[0];
                      const double ns_per_tick = self.get_rt_ns_per_tick();
                      self.set_rt_stats(false);

                      std_ns_per_frame = st.get_std_ticks() * ns_per_tick;
                      p50_ns_per_frame = st.get_percentile_ticks(50.0) * ns_per_tick;
                      p99_ns_per_frame = st.get_percentile_ticks(99.0) * ns_per_tick;
                      p999_ns_per_frame = st.get_percentile_ticks(99.9) * ns_per_tick;
                      p9999_ns_per_frame = st.get_percentile_ticks(99.99) * ns_per_tick;
                      max_ns_per_frame = static_cast<double>(st.max_ticks) * ns_per_tick;
                  }
              }
          }

          py::dict d;
          d["n_tasks"] = n_tasks;
          d["ns_per_frame"] = ns_per_frame;
          d["ns_per_task"] = ns_per_task;
          d["ticks_per_frame"] = ticks_per_frame;
          d["ticks_per_task"] = ticks_per_task;
          d["std_ns_per_frame"] = std_ns_per_frame;
          d["p50_ns_per_frame"] = p50_ns_per_frame;
          d["p99_ns_per_frame"] = p99_ns_per_frame;
          d["p999_ns_per_frame"] = p999_ns_per_frame;
          d["p9999_ns_per_frame"] = p9999_ns_per_frame;
          d["max_ns_per_frame"] = max_ns_per_frame;
          return d;
      },
      "n_exec"_a,
      "collect_rt_percentiles"_a = false,
      "n_warmup"_a = 256,
      "rt_skip"_a = 0,
      "with_statuses"_a = false,
      "task_divisor_override"_a = 0,
      "per_thread"_a = false,
      "Warm up and measure sequence latency and HDR real-time percentiles.");

    sequence_class.def("set_rt_stats",
                       &spu::runtime::Sequence::set_rt_stats,
                       "enable"_a,
                       "n_skip_frames"_a = 0,
                       "Enable or disable HDR real-time cycle-counter collection per stream.");
    sequence_class.def("reset_rt_stats",
                       &spu::runtime::Sequence::reset_rt_stats,
                       "Reset HDR real-time statistics across all threads of the sequence.");
    auto sys = py::module::import("sys");
    sequence_class.def("exec",
                       [](spu::runtime::Sequence& self, spu::tools::Terminal_dump& terminal, std::ostream& stream, bool force_report)
                       {
                           py::gil_scoped_release release{};
                           self.exec(
                            [&](const std::vector<const int*>& statuses) -> bool
                            {
                                pyspu::wrapper::Julia_gc_safe_region gc_safe; // see gc_region.hpp
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
                                pyspu::wrapper::Julia_gc_safe_region gc_safe; // see gc_region.hpp
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
      "show_rt_stats",
      [](spu::runtime::Sequence& self, const bool display_thr, const bool display_in_frames, std::ostream& stream)
      {
          spu::tools::Stats::show_rt(self, display_thr, display_in_frames, stream);
      },
      "display_thr"_a = true,
      "display_in_frames"_a = false,
      "stream"_a = sys.attr("stdout"),
      "Print the real-time HDR statistics of the sequence.");

    sequence_class.def(
      "get_rt_stats",
      [](spu::runtime::Sequence& self) -> py::dict
      {
          spu::tools::Rt_stats st;
          for (const auto& s : self.get_rt_stats_per_thread())
              st.merge(s);
          const double scale = self.get_rt_ns_per_tick();
          const size_t n_t = std::max<size_t>(1, self.get_tasks_per_types().size());
          py::dict d;
          d["n_calls"] = st.n_calls;
          d["n_tasks"] = n_t;
          d["ns_per_tick"] = scale;
          d["avg_ns"] = st.get_avg_ticks() * scale;
          d["std_ns"] = st.get_std_ticks() * scale;
          d["min_ns"] = (st.n_calls > 0) ? (static_cast<double>(st.min_ticks) * scale) : 0.0;
          d["p10_ns"] = st.get_percentile_ticks(10.0) * scale;
          d["p25_ns"] = st.get_percentile_ticks(25.0) * scale;
          d["p50_ns"] = st.get_percentile_ticks(50.0) * scale;
          d["p75_ns"] = st.get_percentile_ticks(75.0) * scale;
          d["p90_ns"] = st.get_percentile_ticks(90.0) * scale;
          d["p99_ns"] = st.get_percentile_ticks(99.0) * scale;
          d["p999_ns"] = st.get_percentile_ticks(99.9) * scale;
          d["p9999_ns"] = st.get_percentile_ticks(99.99) * scale;
          d["max_ns"] = (st.n_calls > 0) ? (static_cast<double>(st.max_ticks) * scale) : 0.0;
          return d;
      },
      "Return the collected HDR real-time statistics of the sequence as a Python dictionary.");

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
