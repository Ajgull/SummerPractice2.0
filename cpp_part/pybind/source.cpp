#include <vector>
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

    std::vector<double> v_filtered, z_filtered;

    for (size_t i = 0; i < n; i++) {
        double z = z_ptr[i];
        double v = v_ptr[i];
        if (v != undef_val && z >= min_z && z <= max_z) {
            v_filtered.push_back(v);
            z_filtered.push_back(z);
        }
    }

    if (z_filtered.empty() || v_filtered.empty()) {
        py::array_t<double> empty_array(0);
        return py::make_tuple(empty_array, empty_array, empty_array, empty_array);
    }

    // Построение ступенчатого графика с шагом step
    // Определяем количество шагов
    const double z_start = z_filtered.front();
    const double z_end = z_filtered.back();
    const size_t num_steps = static_cast<size_t>(std::ceil((z_end - z_start) / step)) + 1;

    std::vector<double> z_steps(num_steps);
    std::vector<double> v_steps(num_steps);

    size_t current_index = 0;
    double last_valid_v = 0.0; // Для запоминания последнего валидного значения

    for (size_t step_idx = 0; step_idx < num_steps; ++step_idx) {
        const double z0 = z_start + step_idx * step;
        const double z1 = z0 + step;

        // Подсчет суммы и количества элементов в сегменте
        double sum = 0.0;
        size_t count = 0;

        while (current_index < z_filtered.size() && z_filtered[current_index] < z1) {
            sum += v_filtered[current_index];
            count++;
            current_index++;
        }

        // Расчет среднего значения
        if (count > 0) {
            last_valid_v = sum / count;
            v_steps[step_idx] = last_valid_v;
        }
        else {
            v_steps[step_idx] = (step_idx > 0) ? v_steps[step_idx - 1] : 0.0;
        }

        z_steps[step_idx] = z0;
    }

    py::array_t<double> v_result(v_filtered.size());
    py::array_t<double> z_result(z_filtered.size());
    py::array_t<double> v_steps_result(v_steps.size());
    py::array_t<double> z_steps_result(z_steps.size());

    std::memcpy(v_result.mutable_data(), v_filtered.data(), v_filtered.size() * sizeof(double));
    std::memcpy(z_result.mutable_data(), z_filtered.data(), z_filtered.size() * sizeof(double));
    std::memcpy(v_steps_result.mutable_data(), v_steps.data(), v_steps.size() * sizeof(double));
    std::memcpy(z_steps_result.mutable_data(), z_steps.data(), z_steps.size() * sizeof(double));

    return py::make_tuple(
        z_result,
        v_result,
        z_steps_result,
        v_steps_result
    );
}

py::tuple calculate_statistics(py::array_t<double> arr) {
    auto buf = arr.request();

    if (buf.ndim != 1)
        throw std::runtime_error("Input array must be 1D");

    double* ptr = static_cast<double*>(buf.ptr);
    size_t n = buf.size;

    if (n == 0)
        throw std::runtime_error("Input array is empty");

    double min_val = std::numeric_limits<double>::max();
    double max_val = std::numeric_limits<double>::lowest();
    double sum = 0.0;

    // Вычисляем минимум, максимум и сумму
    for (size_t i = 0; i < n; ++i) {
        double val = ptr[i];
        if (val < min_val) min_val = val;
        if (val > max_val) max_val = val;
        sum += val;
    }

    double mean = sum / n;

    // Вычисляем стандартное отклонение
    double sq_diff_sum = 0.0;
    for (size_t i = 0; i < n; ++i) {
        double diff = ptr[i] - mean;
        sq_diff_sum += diff * diff;
    }
    double stddev = std::sqrt(sq_diff_sum / n);

    return py::make_tuple(min_val, max_val, mean, stddev);
}

int add(int i, int j) {
    return i + j;
}

py::array_t<double> add_vec(int size) {
    std::vector<double> first(size);
    std::vector<double> second(size);

    for (int i = 0; i < size; i++) {
        first[i] = double(i);
        second[i] = double(i) + 1.0;
    }

    for (int i = 0; i < second.size(); i++) {
        second[i] += first[i];
    }

    py::array_t<double> result(second.size());
    std::memcpy(result.mutable_data(), second.data(), second.size() * sizeof(double));
    return result;
}

py::tuple add_vects(int size) {
    py::array_t<double> first(size);
    py::array_t<double> second(size);

    auto first_buf = first.mutable_data();
    auto second_buf = second.mutable_data();

    for (size_t i = 0; i < size; i++) {
        first_buf[i] = double(i);
        second_buf[i] = double(i) + 1.0;
    }

    for (size_t i = 0; i < size; i++) {
        second_buf[i] += first_buf[i];
    }

    return py::make_tuple(first, second);
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

    m.def("calculate_statistics2", &calculate_statistics, "Calculate min, max, mean and stddev of a 1D numpy array");

    m.def("add", &add, "A function that adds two numbers");

    m.def("add_vec", &add_vec, "Add two vectors and return numpy array");

    m.def("add_vects", &add_vects, "Return two numpy arrays after element-wise addition");
}
