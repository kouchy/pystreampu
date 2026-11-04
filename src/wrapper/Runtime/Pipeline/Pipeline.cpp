#include "wrapper/Runtime/Pipeline/Pipeline.hpp"


#include "wrapper/Common/pybind11_common.h"

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
    pipeline_class.def("get_original_modules", &spu::runtime::Pipeline::get_original_modules,
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

    pipeline_class.def("get_modules_per_threads", &spu::runtime::Pipeline::get_modules_per_threads, "Return the modules of each thread, for all the stages.");
    pipeline_class.def("get_modules_per_types", &spu::runtime::Pipeline::get_modules_per_types, "Return the modules grouped by type, for all the stages.");
    pipeline_class.def("get_tasks_per_types", &spu::runtime::Pipeline::get_tasks_per_types, "Return the tasks grouped by type, for all the stages.");
    pipeline_class.def("get_tasks_per_threads", &spu::runtime::Pipeline::get_tasks_per_threads, "Return the tasks of each thread, for all the stages.");
    pipeline_class.def("__getitem__", &spu::runtime::Pipeline::operator[], py::is_operator());
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
    pipeline_class.def_property_readonly(
      "stages", &spu::runtime::Pipeline::get_stages, py::return_value_policy::reference,
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
