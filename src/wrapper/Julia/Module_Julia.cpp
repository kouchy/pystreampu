#ifdef SPU_JULIA

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Julia/Julia.hpp"

namespace py = pybind11;
using namespace py::literals;
using spu::module::Module_Julia;

namespace
{
// Name of the C++ type of a constant: the given dtype, or deduced from the Python value
std::string
constant_type_name(const py::object& value, const py::object& dtype)
{
    if (!dtype.is_none()) return dtype.cast<pyspu::dtype>().get_name();
    if (py::isinstance<py::bool_>(value)) return "bool";
    if (py::hasattr(value, "dtype")) // NumPy scalar
    {
        const std::string name = py::str(value.attr("dtype").attr("name"));
        return name;
    }
    if (py::isinstance<py::int_>(value)) return "int64";
    if (py::isinstance<py::float_>(value)) return "float64";
    throw py::type_error("the value of a constant must be a bool, an int, a float or a NumPy scalar");
}

void
create_constant(Module_Julia& mdl, spu::runtime::Task& task, const py::object& value, const py::object& dtype)
{
    const std::string type = constant_type_name(value, dtype);
    if (type == "bool")
        mdl.create_constant<bool>(task, value.cast<bool>());
    else if (type == "int8")
        mdl.create_constant<int8_t>(task, value.cast<int8_t>());
    else if (type == "int16")
        mdl.create_constant<int16_t>(task, value.cast<int16_t>());
    else if (type == "int32")
        mdl.create_constant<int32_t>(task, value.cast<int32_t>());
    else if (type == "int64")
        mdl.create_constant<int64_t>(task, value.cast<int64_t>());
    else if (type == "uint8")
        mdl.create_constant<uint8_t>(task, value.cast<uint8_t>());
    else if (type == "uint16")
        mdl.create_constant<uint16_t>(task, value.cast<uint16_t>());
    else if (type == "uint32")
        mdl.create_constant<uint32_t>(task, value.cast<uint32_t>());
    else if (type == "uint64")
        mdl.create_constant<uint64_t>(task, value.cast<uint64_t>());
    else if (type == "float32")
        mdl.create_constant<float>(task, value.cast<float>());
    else if (type == "float64")
        mdl.create_constant<double>(task, value.cast<double>());
    else
        throw py::type_error("unsupported type for a Julia constant: '" + type + "'");
}
} // namespace

void
pyspu::wrapper::wrap_module_julia(py::handle scope)
{
    auto mj_class = py::class_<Module_Julia>(scope, "Module_Julia", R"pbdoc(
        Base class of the Julia modules (`Stateless_Julia`, `Stateful_Julia`): the methods
        that set the Julia codelets and constants of their tasks. It cannot be built.

        A Julia codelet is a Julia function called with, in this order: the states of the
        module (`Stateful_Julia` only), the sockets of the task (in their creation order, as
        1D Julia vectors of `n_elmts * n_frames_per_wave` elements, without copy), the
        constants of the task, then `frame_id` and `n_frames_per_wave` (`UInt32`). It
        returns 0 on success.
    )pbdoc");

    mj_class.def_property("jl_safe",
                          &Module_Julia::is_jl_safe,
                          &Module_Julia::set_jl_safety,
                          R"pbdoc(
        If True (default), a Julia exception in a codelet is caught and raised as a Python
        RuntimeError with the Julia stack trace. False calls the codelets directly (faster).
    )pbdoc");

    mj_class.def("is_eval", &Module_Julia::is_eval, "True if the Julia code of the module has been evaluated.");

    mj_class.def("eval",
                 &Module_Julia::eval,
                 R"pbdoc(
        Evaluate the Julia code of the module (states and codelets). A `Sequence` or a
        `Pipeline` does it for each of its threads.

        Raises:
            RuntimeError: if the module has already been evaluated, or has no codelet
    )pbdoc");

    mj_class.def("create_constant",
                 &create_constant,
                 "task"_a,
                 "value"_a,
                 "dtype"_a = py::none(),
                 R"pbdoc(
        Add a constant argument to the codelet of a task, after its sockets. Create the
        constants before the codelet.

        Args:
            task (Task): a task of this module
            value (bool | int | float | numpy scalar): value of the constant
            dtype (dtype | None): Julia type of the constant (`spu.int32` gives `Int32`...).
                Without it: `Bool` for a bool, `Int64` for an int, `Float64` for a float,
                the type of a NumPy scalar.
    )pbdoc");

    mj_class.def("create_codelet",
                 static_cast<void (Module_Julia::*)(spu::runtime::Task&, const std::string&, const std::string&)>(
                   &Module_Julia::create_codelet),
                 "task"_a,
                 "code"_a = "",
                 "function_name"_a = "",
                 R"pbdoc(
        Set the Julia codelet of a task.

        Args:
            task (Task): a task of this module
            code (str): Julia code that defines the function; empty if the function is
                already defined (see `Julia.eval`)
            function_name (str): name of the Julia function; by default, the name of the task
    )pbdoc");

    mj_class.def(
      "create_codelet_file",
      [](Module_Julia& mdl, spu::runtime::Task& task, const py::object& path, const std::string& function_name)
      {
          const std::string filename = py::str(py::module_::import("os").attr("fspath")(path));
          mdl.create_codelet_file(task, filename, function_name);
      },
      "task"_a,
      "path"_a,
      "function_name"_a = "",
      R"pbdoc(
        Set the Julia codelet of a task from a `.jl` file.

        Args:
            task (Task): a task of this module
            path (str | os.PathLike): file that defines the function
            function_name (str): name of the Julia function; by default, the name of the task
    )pbdoc");
}

#endif /* SPU_JULIA */
