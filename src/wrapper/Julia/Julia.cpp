#ifdef SPU_JULIA

#include "wrapper/Julia/Julia.hpp"
#include "wrapper/Julia/gc_region.hpp"

namespace py = pybind11;
using namespace py::literals;
using spu::tools::Julia;

void
pyspu::wrapper::check_julia_exception(const std::string& context)
{
    jl_value_t* exception = jl_exception_occurred();
    if (exception == nullptr) return;
    std::string message = context;
    jl_function_t* sprint = jl_get_function(jl_base_module, "sprint");
    jl_function_t* showerror = jl_get_function(jl_base_module, "showerror");
    jl_exception_clear();
    if (sprint != nullptr && showerror != nullptr)
    {
        jl_value_t* text = jl_call2(sprint, showerror, exception);
        if (text != nullptr && jl_is_string(text)) message += ": " + std::string(jl_string_ptr(text));
        jl_exception_clear();
    }
    throw spu::tools::runtime_error(std::move(message)); // spu.exceptions.RuntimeError, like the errors of StreamPU
}

std::string
pyspu::wrapper::julia_repr(jl_value_t* value)
{
    pyspu::wrapper::Julia_gc_unsafe_region gc_unsafe;
    jl_function_t* repr = jl_get_function(jl_base_module, "repr");
    jl_value_t* text = jl_call1(repr, value);
    pyspu::wrapper::check_julia_exception("Julia error in repr");
    return text != nullptr && jl_is_string(text) ? std::string(jl_string_ptr(text)) : std::string();
}

void
pyspu::wrapper::wrap_julia(py::handle scope)
{
    auto julia_class = py::class_<Julia>(scope, "Julia", R"pbdoc(
        The Julia runtime used by the Julia modules (`Stateless_Julia`, `Stateful_Julia`).

        All the methods are static. Julia is started automatically when the first Julia
        module is created; call `Julia.init` before to choose the number of GC root slots.
        The code evaluated by `eval` and `eval_file` is evaluated in the `Main` module of
        Julia, where the codelets are looked up.
    )pbdoc");

    julia_class.def_static("init",
                           &Julia::init,
                           "n_proxies"_a = 256,
                           R"pbdoc(
        Start the Julia runtime, if it is not started yet (it is never started twice).

        Args:
            n_proxies (int): number of GC root slots per thread
    )pbdoc");

    julia_class.def_static("is_init", &Julia::is_init, "True if the Julia runtime has been started.");

    julia_class.def_static("get_n_proxies", &Julia::get_n_proxies, "Number of GC root slots per thread.");

    julia_class.def_static(
      "eval",
      [](const std::string& code)
      {
          Julia::init();
          pyspu::wrapper::Julia_gc_unsafe_region gc_unsafe;
          Julia::eval_string(code);
          pyspu::wrapper::check_julia_exception("Julia error");
      },
      "code"_a,
      R"pbdoc(
        Evaluate Julia code in the `Main` module (starts Julia if needed).

        Args:
            code (str): Julia code

        Raises:
            spu.exceptions.RuntimeError: if the evaluation raises a Julia exception
    )pbdoc");

    julia_class.def_static(
      "eval_file",
      [](const py::object& path)
      {
          const std::string filename = py::str(py::module_::import("os").attr("fspath")(path));
          Julia::init();
          pyspu::wrapper::Julia_gc_unsafe_region gc_unsafe;
          Julia::eval_file(filename);
          pyspu::wrapper::check_julia_exception("Julia error in '" + filename + "'");
      },
      "path"_a,
      R"pbdoc(
        Evaluate a Julia file in the `Main` module (starts Julia if needed).

        Args:
            path (str | os.PathLike): path of the `.jl` file

        Raises:
            spu.exceptions.RuntimeError: if the file cannot be read, or if its evaluation
                raises a Julia exception
    )pbdoc");
}

#endif /* SPU_JULIA */
