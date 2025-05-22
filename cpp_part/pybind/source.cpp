#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <cstring>

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
    std::vector<double> v_steps, z_steps;

    for (size_t i = 0; i < n; i++) {
        double z = z_ptr[i];
        double v = v_ptr[i];
        if (v != undef_val && z >= 3 && z <= 7) {
            v_filtered1.push_back(-v);
            z_filtered1.push_back(-z);
            v_steps.push_back(v);
            z_steps.push_back(z);
        }
    }

    py::array_t<double> v_result(v_filtered1.size());
    py::array_t<double> z_result(z_filtered1.size());
    py::array_t<double> v_steps_result(v_steps.size());
    py::array_t<double> z_steps_result(z_steps.size());

    std::memcpy(v_result.mutable_data(), v_filtered1.data(), v_filtered1.size() * sizeof(double));
    std::memcpy(z_result.mutable_data(), z_filtered1.data(), z_filtered1.size() * sizeof(double));
    std::memcpy(v_steps_result.mutable_data(), v_steps.data(), v_steps.size() * sizeof(double));
    std::memcpy(z_steps_result.mutable_data(), z_steps.data(), z_steps.size() * sizeof(double));

    return py::make_tuple(
        z_result,
        v_result,
        z_steps_result,
        v_steps_result
    );
}

PYBIND11_MODULE(example, m) {
    m.def("perform_calculation", &perform_calculation,
        py::arg("z_array"),
        py::arg("v_array"),
        py::arg("min_z"),
        py::arg("max_z"),
        py::arg("step"),
        py::arg("contrast"),
        py::arg("undef_val"));
}
