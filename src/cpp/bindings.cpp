#include <pybind11/pybind11.h>

#include "mt19937.hpp"
#include "middle_square.hpp"
#include "congruence.hpp"

namespace py = pybind11;

PYBIND11_MODULE(rngcpp, m) {
    m.doc() = "rng C++ module";

    py::class_<MiddleSquare>(m, "MiddleSquare")
        .def(py::init<>())
        .def(py::init<int>(), py::arg("seed"))
        .def("next_state", &MiddleSquare::nextState)
        .def("uniform", &MiddleSquare::uniform);

    py::class_<CongruenceGenerator>(m, "CongruenceGenerator")
        .def(py::init<>())
        .def(py::init<int>(), py::arg("seed"))
        .def("next_state", &CongruenceGenerator::nextState)
        .def("uniform", &CongruenceGenerator::uniform);

    py::class_<MT19937>(m, "MT19937")
        .def(py::init<>())
        .def(py::init<uint32_t>(), py::arg("seed"))
        .def("seed", &MT19937::seed, py::arg("seed"))
        .def("extract_number", &MT19937::extract_number)
        .def("uniform", (double (MT19937::*)()) &MT19937::uniform)
        .def("uniform_vec", (std::vector<double> (MT19937::*)(int)) &MT19937::uniform, py::arg("count"));
}

