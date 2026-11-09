#include "wrapper/Runtime/Pipeline/Pipeline.hpp"


#include "wrapper/Common/pybind11_common.h"

#include <algorithm>
#include <atomic>
#include <chrono>
#include <functional>
#include <iostream>

#include <streampu.hpp>

namespace py = pybind11;
using namespace py::literals;

void
pyspu::wrapper::wrap_pipeline(py::handle scope)
{
  auto sys = py::module::import("sys");
  auto pipeline_class =
    py::class_<spu::runtime::Pipeline, spu::tools::Interface_get_set_n_frames>(scope, "_Pipeline", R"pbdoc(
        C++ pipeline of StreamPU: a graph split into stages that run concurrently.

        Each stage is a sequence with its own number of threads; consecutive stages exchange
        frames through buffers (adaptor modules). Use `streampu.Pipeline`.
    )pbdoc");
    pipeline_class.def(py::init(
                         [](const std::vector<spu::runtime::Task*>& firsts,
                            const std::vector<spu::runtime::Task*>& lasts,
                            const std::vector<std::tuple<std::vector<spu::runtime::Task*>,
                                                         std::vector<spu::runtime::Task*>,
                                                         std::vector<spu::runtime::Task*>>>& sep_stages,
                            const std::vector<size_t> n_threads,
                            const std::vector<size_t> synchro_buffer_sizes,
                            const std::vector<bool> synchro_active_waiting,
                            const std::vector<bool> thread_pinning,
                            const std::vector<std::vector<size_t>> puids)
                         {
                             return std::unique_ptr<spu::runtime::Pipeline>(
                               new spu::runtime::Pipeline(firsts,
                                                          lasts,
                                                          sep_stages,
                                                          n_threads,
                                                          synchro_buffer_sizes,
                                                          synchro_active_waiting,
                                                          thread_pinning,
                                                          puids));
                         }),
                       "firsts"_a,
                       "lasts"_a,
                       "sep_stages"_a = std::vector<std::tuple<std::vector<spu::runtime::Task*>,
                                                               std::vector<spu::runtime::Task*>,
                                                               std::vector<spu::runtime::Task*>>>(),
                       "n_threads"_a = std::vector<size_t>(),
                       "synchro_buffer_sizes"_a = std::vector<size_t>(),
                       "synchro_active_waiting"_a = std::vector<bool>(),
                       "thread_pinning"_a = std::vector<bool>(),
                       "puids"_a = std::vector<std::vector<size_t>>(),
                       R"pbdoc(
        Build a pipeline.

        Args:
            firsts (list[Task]): first tasks of the graph
            lasts (list[Task]): last tasks of the graph
            sep_stages (list): for each stage, `[first tasks, last tasks, excluded tasks]`
            n_threads (list[int]): number of threads of each stage
            synchro_buffer_sizes (list[int]): size of the buffer between each pair of
                consecutive stages
            synchro_active_waiting (list[bool]): active waiting between each pair of
                consecutive stages (faster, but uses a core)
            thread_pinning (list[bool]): pin the threads of each stage
            puids (list[list[int]]): processing units of the threads of each stage
    )pbdoc",
                       py::return_value_policy::take_ownership);
    pipeline_class.def("get_original_modules", &spu::runtime::Pipeline::get_original_modules, py::return_value_policy::reference,
                       "Return the modules created by the user, one list per stage (without the clones and adaptors).");

    pipeline_class.def("exec",
                       [](spu::runtime::Pipeline& self)
                       {
                           py::gil_scoped_release release{};
                           self.exec();
                       }, "Execute the pipeline until a module is done (e.g. a source at the end of its file) or SIGINT is received.");

    pipeline_class.def("export_dot",
                       [](spu::runtime::Pipeline& self, const std::string& file_name)
                       {
                           std::ofstream f(file_name);
                           self.export_dot(f);
                       }, "file_name"_a, R"pbdoc(
        Export the graph of the pipeline in the Graphviz DOT format.

        Args:
            file_name (str): path of the DOT file to write
    )pbdoc");

    pipeline_class.def("get_modules_per_threads", &spu::runtime::Pipeline::get_modules_per_threads, py::return_value_policy::reference, "Return the modules of each thread, for all the stages.");
    pipeline_class.def("get_modules_per_types", &spu::runtime::Pipeline::get_modules_per_types, py::return_value_policy::reference, "Return the modules grouped by type, for all the stages.");
    pipeline_class.def("get_tasks_per_types", &spu::runtime::Pipeline::get_tasks_per_types, py::return_value_policy::reference, "Return the tasks grouped by type, for all the stages.");
    pipeline_class.def("get_tasks_per_threads", &spu::runtime::Pipeline::get_tasks_per_threads, py::return_value_policy::reference, "Return the tasks of each thread, for all the stages.");
    pipeline_class.def("__getitem__", &spu::runtime::Pipeline::operator[], py::return_value_policy::reference, py::is_operator());
    pipeline_class.def("bind_adaptors", &spu::runtime::Pipeline::bind_adaptors, "Bind the adaptors that connect the stages (done when the pipeline is built).");
    pipeline_class.def("unbind_adaptors", &spu::runtime::Pipeline::unbind_adaptors, "Unbind the adaptors and restore the original bindings of the tasks.");
    pipeline_class.def("is_bound_adaptors", &spu::runtime::Pipeline::is_bound_adaptors, "Return True if the adaptors are bound.");

    pipeline_class.def("show_stats",
                       [](spu::runtime::Pipeline& self, std::ostream& stream)
                       {
                           auto stages = self.get_stages();
                           for (size_t s = 0; s < stages.size(); s++)
                           {
                               const int n_threads = stages[s]->get_n_threads();
                               stream << "#" << std::endl
                                      << "# Pipeline stage " << s << " (" << n_threads
                                      << " thread(s)): " << std::endl;
                               spu::tools::Stats::show(stages[s]->get_tasks_per_types(), true, true, stream);
                           }
                       }, "stream"_a = sys.attr("stdout"), R"pbdoc(
        Print the statistics of the tasks, one table per stage (enable them first with
        `task.stats = True`).

        Args:
            stream (file): stream where the statistics are written
    )pbdoc");

    pipeline_class.def("set_rt_stats",
                       &spu::runtime::Pipeline::set_rt_stats,
                       "enable"_a,
                       "n_skip_frames"_a = 0,
                       "Enable or disable HDR real-time cycle-counter collection across all pipeline stages.");
    pipeline_class.def("reset_rt_stats",
                       &spu::runtime::Pipeline::reset_rt_stats,
                       "Reset HDR real-time statistics across all stages of the pipeline.");
    pipeline_class.def(
      "show_rt_stats",
      [](spu::runtime::Pipeline& self, const bool display_thr, const bool display_in_frames, std::ostream& stream)
      {
          spu::tools::Stats::show_rt(self, display_thr, display_in_frames, stream);
      },
      "display_thr"_a = true,
      "display_in_frames"_a = false,
      "stream"_a = sys.attr("stdout"),
      "Print the real-time HDR statistics of the pipeline.");

    pipeline_class.def(
      "measure_bench",
      [](spu::runtime::Pipeline& self, const size_t n_exec, const size_t n_warmup, const size_t n_skip_frames) -> py::dict
      {
          double sum_stage_ns_per_task = 0.0;
          double sum_stage_std_ns = 0.0;
          double sum_stage_p50_ns = 0.0;
          double sum_stage_p99_ns = 0.0;
          double sum_stage_p999_ns = 0.0;
          double sum_stage_p9999_ns = 0.0;
          double max_stage_ns = 0.0;
          double out_ns_per_stream = -1.0;
          double e2e_avg_ns = -1.0;
          double e2e_std_ns = -1.0;
          double e2e_p50_ns = -1.0;
          double e2e_p99_ns = -1.0;
          double e2e_p999_ns = -1.0;
          double e2e_p9999_ns = -1.0;
          double e2e_max_ns = -1.0;
          size_t n_stages = 0;

          {
              py::gil_scoped_release release{};
              for (auto* m : self.get_modules<spu::module::Module>(false))
                  for (auto& t : m->tasks)
                      t->set_fast(true);

              if (n_warmup > 0)
              {
                  std::atomic<size_t> w(0);
                  self.set_rt_stats(false);
                  self.exec([&w, n_warmup]() { return ++w >= n_warmup; });
                  for (auto* m : self.get_modules<spu::tools::Interface_reset>(false))
                      m->reset();
              }

              self.reset_rt_stats();
              self.set_rt_stats(true, n_skip_frames);
              std::atomic<size_t> cnt(0);
              self.exec([&cnt, n_exec]() { return ++cnt >= n_exec; });

              const auto stages = self.get_stages();
              n_stages = stages.size();
              for (const auto* stg : stages)
              {
                  spu::tools::Rt_stats stg_merged;
                  for (const auto& s : stg->get_rt_stats_per_thread())
                      stg_merged.merge(s);
                  const size_t n_t = std::max<size_t>(1, stg->get_tasks_per_types().size());
                  const double scale = stg->get_rt_ns_per_tick() / static_cast<double>(n_t);
                  sum_stage_ns_per_task += stg_merged.get_avg_ticks() * scale;
                  sum_stage_std_ns += stg_merged.get_std_ticks() * scale;
                  sum_stage_p50_ns += stg_merged.get_percentile_ticks(50.0) * scale;
                  sum_stage_p99_ns += stg_merged.get_percentile_ticks(99.0) * scale;
                  sum_stage_p999_ns += stg_merged.get_percentile_ticks(99.9) * scale;
                  sum_stage_p9999_ns += stg_merged.get_percentile_ticks(99.99) * scale;
                  const double stg_max =
                    (stg_merged.n_calls > 0) ? (static_cast<double>(stg_merged.max_ticks) * scale) : 0.0;
                  if (stg_max > max_stage_ns) max_stage_ns = stg_max;
              }
              const double n_stg_d = static_cast<double>(std::max<size_t>(1, n_stages));
              sum_stage_ns_per_task /= n_stg_d;
              sum_stage_std_ns /= n_stg_d;
              sum_stage_p50_ns /= n_stg_d;
              sum_stage_p99_ns /= n_stg_d;
              sum_stage_p999_ns /= n_stg_d;
              sum_stage_p9999_ns /= n_stg_d;

              spu::tools::Rt_stats e2e_merged;
              for (const auto& s : stages.back()->get_pipeline_e2e_rt_stats_per_thread())
                  e2e_merged.merge(s);

              spu::tools::Rt_stats inter_merged;
              for (const auto& s : stages.back()->get_pipeline_inter_rt_stats_per_thread())
                  inter_merged.merge(s);

              const double ns_per_tick = stages.back()->get_rt_ns_per_tick();
              const double last_threads = static_cast<double>(std::max<size_t>(1, stages.back()->get_n_threads()));
              out_ns_per_stream = (inter_merged.get_avg_ticks() * ns_per_tick) / last_threads;
              e2e_avg_ns = e2e_merged.get_avg_ticks() * ns_per_tick;
              e2e_std_ns = e2e_merged.get_std_ticks() * ns_per_tick;
              e2e_p50_ns = e2e_merged.get_percentile_ticks(50.0) * ns_per_tick;
              e2e_p99_ns = e2e_merged.get_percentile_ticks(99.0) * ns_per_tick;
              e2e_p999_ns = e2e_merged.get_percentile_ticks(99.9) * ns_per_tick;
              e2e_p9999_ns = e2e_merged.get_percentile_ticks(99.99) * ns_per_tick;
              e2e_max_ns = (e2e_merged.n_calls > 0) ? (static_cast<double>(e2e_merged.max_ticks) * ns_per_tick) : 0.0;
          }

          py::dict d;
          d["n_stages"] = n_stages;
          d["stage_ns_per_task"] = sum_stage_ns_per_task;
          d["stage_std_ns_per_task"] = sum_stage_std_ns;
          d["stage_p50_ns_per_task"] = sum_stage_p50_ns;
          d["stage_p99_ns_per_task"] = sum_stage_p99_ns;
          d["stage_p999_ns_per_task"] = sum_stage_p999_ns;
          d["stage_p9999_ns_per_task"] = sum_stage_p9999_ns;
          d["stage_max_ns_per_task"] = max_stage_ns;
          d["out_ns_per_stream"] = out_ns_per_stream;
          d["e2e_avg_ns"] = e2e_avg_ns;
          d["e2e_std_ns"] = e2e_std_ns;
          d["e2e_p50_ns"] = e2e_p50_ns;
          d["e2e_p99_ns"] = e2e_p99_ns;
          d["e2e_p999_ns"] = e2e_p999_ns;
          d["e2e_p9999_ns"] = e2e_p9999_ns;
          d["e2e_max_ns"] = e2e_max_ns;
          return d;
      },
      "n_exec"_a,
      "n_warmup"_a = 256,
      "n_skip_frames"_a = 0,
      "Warm up and measure pipeline stage and end-to-end HDR real-time statistics.");
    pipeline_class.def_property_readonly(
      "stages",
      [](spu::runtime::Pipeline& self) { return self.get_stages(); },
      py::return_value_policy::reference,
      "Sequences of the stages of the pipeline.");
    pipeline_class.def_property_readonly(
      "last_tasks", &spu::runtime::Pipeline::get_lasts_tasks, py::return_value_policy::reference,
      "Last tasks of the pipeline.");
    pipeline_class.def_property_readonly(
      "first_tasks", &spu::runtime::Pipeline::get_firsts_tasks, py::return_value_policy::reference,
      "First tasks of the pipeline.");
    pipeline_class.def_property(
      "auto_stop", &spu::runtime::Pipeline::is_auto_stop, &spu::runtime::Pipeline::set_auto_stop,
      "If True, the pipeline stops by itself when a module is done.");
}
