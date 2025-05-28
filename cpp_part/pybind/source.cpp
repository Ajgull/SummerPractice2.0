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

    const double z_start = z_filtered.front();
    const double z_end = z_filtered.back();

    std::vector<double> z_steps, v_steps;

    z_steps.push_back(z_start);
    v_steps.push_back(v_filtered.front());

    size_t current_index = 0; // индекс в исходных данных
    double current_z = z_start;
    double last_v = v_filtered.front();

    double best_z = 0.0;
    double best_v = 0.0;

    while (current_z < z_end) {
        best_z = current_z;
        best_v = last_v;

        // Ищем подходящий шаг с контрастностью
        for (double test_z = current_z; test_z <= z_end; ) {
            double sum = 0.0;
            size_t count = 0;

            size_t temp_index = current_index;
            while (temp_index < z_filtered.size() && z_filtered[temp_index] < test_z) {
                sum += v_filtered[temp_index];
                count++;
                temp_index++;
            }

            if (count > 0) {
                double avg_v = sum / count;
                if (last_v != 0 && avg_v != 0) {
                    double ratio = avg_v / last_v;
                    if (ratio <= contrast || ratio >= 1.0 / contrast) {
                        best_z = test_z;
                        best_v = avg_v;
                        current_index = temp_index; // обновляем индекс, чтобы не считать эти точки повторно
                        z_steps.push_back(current_z);
                        v_steps.push_back(last_v);

                        z_steps.push_back(current_z);
                        v_steps.push_back(best_v);
                        test_z += step;
                        break;
                    }
                    else {
                        test_z += 1.0;
                    }
                }
            }

        }


        current_z = best_z;
        last_v = best_v;
        best_z += step;
    }

    if (z_steps.empty() || z_steps.back() < z_end) {
        z_steps.push_back(z_end);
        v_steps.push_back(last_v);

        z_steps.push_back(z_end);
        v_steps.push_back(v_filtered.back());
    }

    py::array_t<double> v_result(v_filtered.size());
    py::array_t<double> z_result(z_filtered.size());
    py::array_t<double> v_steps_result(v_steps.size());
    py::array_t<double> z_steps_result(z_steps.size());

    std::copy(v_filtered.begin(), v_filtered.end(), v_result.mutable_data());
    std::copy(z_filtered.begin(), z_filtered.end(), z_result.mutable_data());
    std::copy(v_steps.begin(), v_steps.end(), v_steps_result.mutable_data());
    std::copy(z_steps.begin(), z_steps.end(), z_steps_result.mutable_data());


    return py::make_tuple(
        z_result,
        v_result,
        z_steps_result,
        v_steps_result
    );
}

py::tuple perform_calculation_no_contrast(
    py::array_t<double> z_array,
    py::array_t<double> v_array,
    double min_z,
    double max_z,
    double step,       // шаг теперь в индексах, например 1, 2, 3...
    double contrast,   // параметр contrast можно игнорировать, т.к. функция без контрастности
    double undef_val)
{
    auto v_buf = v_array.request();
    auto z_buf = z_array.request();

    double* v_ptr = static_cast<double*>(v_buf.ptr);
    double* z_ptr = static_cast<double*>(z_buf.ptr);
    size_t n = v_buf.size;

    std::vector<double> v_filtered, z_filtered;

    // Фильтрация по undef_val и диапазону z
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

    size_t filtered_size = z_filtered.size();

    // Количество шагов по индексам с шагом step
    size_t num_steps = (filtered_size + static_cast<size_t>(step) - 1) / static_cast<size_t>(step);

    std::vector<double> z_steps;
    std::vector<double> v_steps;

    // Формируем ступенчатые точки с повторением для горизонтальных и вертикальных сегментов
    for (size_t i = 0; i < num_steps; i++) {
        size_t idx = i * static_cast<size_t>(step);
        if (idx >= filtered_size) {
            idx = filtered_size - 1;
        }

        double z_val = z_filtered[idx];
        double v_val = v_filtered[idx];

        // Для первой точки просто добавляем
        if (i == 0) {
            z_steps.push_back(z_val);
            v_steps.push_back(v_val);
        }
        else {
            // Горизонтальный сегмент: z меняется, v фиксирован (предыдущее значение)
            z_steps.push_back(z_val);
            v_steps.push_back(v_steps.back());

            // Вертикальный сегмент: z фиксирован, v меняется на новое значение
            z_steps.push_back(z_val);
            v_steps.push_back(v_val);
        }
    }

    // Добавляем последнюю точку, если она не совпадает с последней добавленной
    if (z_steps.back() < z_filtered.back()) {
        z_steps.push_back(z_filtered.back());
        v_steps.push_back(v_steps.back());

        z_steps.push_back(z_filtered.back());
        v_steps.push_back(v_filtered.back());
    }

    py::array_t<double> v_result(v_filtered.size());
    py::array_t<double> z_result(z_filtered.size());
    py::array_t<double> v_steps_result(v_steps.size());
    py::array_t<double> z_steps_result(z_steps.size());

    std::copy(v_filtered.begin(), v_filtered.end(), v_result.mutable_data());
    std::copy(z_filtered.begin(), z_filtered.end(), z_result.mutable_data());
    std::copy(v_steps.begin(), v_steps.end(), v_steps_result.mutable_data());
    std::copy(z_steps.begin(), z_steps.end(), z_steps_result.mutable_data());

    return py::make_tuple(
        z_result,
        v_result,
        z_steps_result,
        v_steps_result
    );
}





py::tuple calculate_statistics(py::array_t<double> arr) {
    auto buf = arr.request();

    double* ptr = static_cast<double*>(buf.ptr);
    size_t n = buf.size;

    if (n == 0) {
        return py::make_tuple(0.0, 0.0, 0.0, 0.0);
    }

    double min_val = std::numeric_limits<double>::max();
    double max_val = std::numeric_limits<double>::lowest();
    double sum = 0.0;

    for (size_t i = 0; i < n; i++) {
        double val = ptr[i];
        if (val < min_val) {
            min_val = val;
        }
        if (val > max_val) {
            max_val = val;
        }
        sum += val;
    }

    double mean = sum / n;

    double diff_sum = 0.0;
    for (size_t i = 0; i < n; i++) {
        double diff = ptr[i] - mean;
        diff_sum += diff * diff;
    }
    double stddev = std::sqrt(diff_sum / n);

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

    m.def("perform_calculation2", &perform_calculation_no_contrast,
        py::arg("z_array"),
        py::arg("v_array"),
        py::arg("min_z"),
        py::arg("max_z"),
        py::arg("step"),
        py::arg("contrast"),
        py::arg("undef_val"));

    m.def("calculate_statistics2", &calculate_statistics);

    m.def("add", &add);

    m.def("add_vec", &add_vec);

    m.def("add_vects", &add_vects);
}
