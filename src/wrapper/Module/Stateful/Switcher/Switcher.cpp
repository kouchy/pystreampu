#include "wrapper/Module/Stateful/Switcher/Switcher.hpp"
#include "wrapper/Common/Tools/Type/Type.hpp"

#include "wrapper/Common/Tools/type_functions.h"
#include <map>
#include <memory>
#include <typeindex>
#include <typeinfo>

namespace py = pybind11;
using namespace py::literals;

void
pyspu::wrapper::wrap_switcher(py::handle scope)
{
    auto switcher_class = py::class_<spu::module::Switcher, spu::module::Stateful>(scope, "Switcher", R"pbdoc(
        Module that implements a conditional path in a sequence.

        Its task `commute` sends its data to one of `n_data_sockets` paths, chosen by the
        output of a controller; its task `select` takes the data of the path that was
        executed and forwards it.
    )pbdoc");
    switcher_class.def(
      py::init(
        [](const size_t n_data_sockets,
           const size_t n_elmts_commute,
           pyspu::dtype datatype_commute,
           const size_t n_elmts_select,
           pyspu::dtype datatype_select)
        {
            std::type_index cpp_datatype_commute = pyspu::utils::str2typeid(datatype_commute.get_name());
            std::type_index cpp_datatype_select = pyspu::utils::str2typeid(datatype_select.get_name());
            return new spu::module::Switcher(
              n_data_sockets, n_elmts_commute, cpp_datatype_commute, n_elmts_select, cpp_datatype_select);
        }),
      "n_data_sockets"_a,
      "n_elmts_commute"_a,
      "datatype_commute"_a,
      "n_elmts_select"_a,
      "datatype_select"_a,
      R"pbdoc(
        Build a switcher whose commuted and selected data have different types.

        Args:
            n_data_sockets (int): number of paths
            n_elmts_commute (int): number of elements of the commuted data
            datatype_commute (dtype): data type of the commuted data
            n_elmts_select (int): number of elements of the selected data
            datatype_select (dtype): data type of the selected data
    )pbdoc",
      py::return_value_policy::take_ownership);

    switcher_class.def(py::init(
                         [](const size_t n_data_sockets, const size_t n_elmts, pyspu::dtype datatype)
                         {
                             std::type_index cpp_datatype = pyspu::utils::str2typeid(datatype.get_name());
                             return new spu::module::Switcher(n_data_sockets, n_elmts, cpp_datatype);
                         }),
                       "n_data_sockets"_a,
                       "n_elmts"_a,
                       "datatype"_a,
                       R"pbdoc(
        Build a switcher.

        Args:
            n_data_sockets (int): number of paths
            n_elmts (int): number of elements of the data
            datatype (dtype): data type of the data
    )pbdoc",
                       py::return_value_policy::take_ownership);
}
