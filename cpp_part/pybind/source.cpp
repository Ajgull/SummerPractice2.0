#include <vector>
#include <algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

py::tuple perform_calculation(
    py::array_t<double> z_array,
    py::array_t<double> v_array,
    double min_z,
    double max_z,
    double step,
    double contrast,
    double undef_val)
{
    auto v_buf = v_array.request();
    auto z_buf = z_array.request();

    double* v_ptr = static_cast<double*>(v_buf.ptr);
    double* z_ptr = static_cast<double*>(z_buf.ptr);
    size_t n = v_buf.size;

    std::vector<double> v_filtered1, z_filtered1;
    std::vector<double> z_steps, v_steps;

    for (int i = 0; i < n; i++) {
        double z = z_ptr[i];
        double v = v_ptr[i];
        if (v != undef_val && z >= min_z && z <= max_z) {
            v_filtered1.push_back(v);
            z_filtered1.push_back(z);
            v_steps.push_back(v);
            z_steps.push_back(z);
        }
    }
    
    py::array_t<double> v_result(v_steps.size(), v_steps.data());
    py::array_t<double> z_result(v_steps.size(), v_steps.data());
    py::array_t<double> v_steps_result(v_steps.size(), v_steps.data());
    py::array_t<double> z_steps_result(z_steps.size(), z_steps.data());

    return py::make_tuple(
        z_result,
        v_result,
        z_steps_result,
        v_steps_result
    );
}


PYBIND11_MODULE(example, m) {
    m.def("perform_calculation_pybind", &perform_calculation,
        py::arg("z_array"),
        py::arg("v_array"),
        py::arg("min_z"),
        py::arg("max_z"),
        py::arg("step"),
        py::arg("contrast"),
        py::arg("undef_val"));
}