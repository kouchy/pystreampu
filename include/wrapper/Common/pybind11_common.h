#ifndef PYBIND11_HPP_
#define PYBIND11_HPP_

#include <pybind11/pybind11.h>

#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>
#include <pybind11/iostream.h>

#include "wrapper/Common/pystreambuf.h"
// typing of the spu::module::Module* returned to Python (must be seen by every translation unit, ODR)
#include "wrapper/Common/Tools/Module_downcast.hpp"

#endif