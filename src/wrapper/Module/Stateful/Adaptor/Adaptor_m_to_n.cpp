#include "wrapper/Module/Stateful/Adaptor/Adaptor_m_to_n.hpp"

#include "wrapper/Common/Tools/Type/Type.hpp"
#include "wrapper/Common/Tools/type_functions.h"

namespace py = pybind11;
using namespace pyspu::wrapper;
using namespace py::literals;

void
pyspu::wrapper::wrap_adaptor_m_to_n(py::handle scope)
{
    auto py_adaptor_class =
      py::class_<spu::module::Adaptor_m_to_n, spu::module::Stateful, spu::tools::Interface_waiting>(scope, "Adaptor_m_to_n", "Module inserted by a pipeline between two stages: it buffers the frames from m threads to n threads.");

    py_adaptor_class.def_property_readonly("n_elmts", &spu::module::Adaptor_m_to_n::get_n_elmts, "Number of elements of each buffered socket.");
    py_adaptor_class.def_property_readonly("n_bytes", &spu::module::Adaptor_m_to_n::get_n_bytes, "Number of bytes of each buffered socket.");
    py_adaptor_class.def_property_readonly("dtype",
                                           [](const spu::module::Adaptor_m_to_n& self)
                                           { return pyspu::dtype::get(pyspu::utils::typeid2str(self.get_datatype())); },
                                           "Data type of the buffered sockets.");
    py_adaptor_class.def_property("n_frames", &spu::module::Adaptor_m_to_n::get_n_frames, &spu::module::Adaptor_m_to_n::set_n_frames,
                                  "Number of frames per execution.");
}

//void
//pyspu::wrapper::wrap_adaptors_m_to_n(py::handle scope)
//{
//    pyspu::wrapper::wrap_adaptor_m_to_n(scope);
//}
