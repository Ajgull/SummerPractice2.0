#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <algorithm>

namespace py = pybind11;

std::vector<double> norm_data(std::vector<double>& data, int min_v, int max_v) {
    if (min_v == max_v) {
        return data;
    }
    else {
        double min_v_val = *std::min_element(begin(data), end(data));
        double max_v_val = *std::max_element(begin(data), end(data));


        for (size_t i = 0; i < data.size(); i++) {
            data[i] = (data[i] - min_v_val) / (max_v_val - min_v_val) * (max_v - min_v) + min_v;
        }
        return data;
    }
}

py::tuple perform_calculation(
    py::array_t<double> z_array,
    py::array_t<double> v_array,
    double min_z,
    double max_z,
    double step,
    double contrast,
    double undef_val,
    int new_min,
    int new_max)
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

    v_filtered = norm_data(v_filtered, new_min, new_max);

    const double z_start = z_filtered.front();
    const double z_end = z_filtered.back();

    std::vector<double> z_steps;
    std::vector<double> v_steps;

    size_t current_index = 0;
    double current_z = z_start;
    double last_v = v_filtered.front();

    double initial_step = step;
    double current_step = initial_step;

    while (current_z < z_end && current_index < z_filtered.size()) {
        double target_z = std::min(current_z + current_step, z_end);

        double sum_v = 0.0;
        size_t count = 0;
        size_t temp_index = current_index;

        while (temp_index < z_filtered.size() && z_filtered[temp_index] < target_z) {
            sum_v += v_filtered[temp_index];
            count++;
            temp_index++;
        }

        if (count == 0) {
            z_steps.push_back(current_z);
            z_steps.push_back(target_z);
            v_steps.push_back(last_v);
            v_steps.push_back(last_v);
            current_z = target_z;
            current_index = temp_index;
            current_step = initial_step;
            continue;
        }

        double avg_v = sum_v / count;
        double contrast_val;

        if (last_v != 0) {
            contrast_val = avg_v / last_v;
        }
        else {
            contrast_val = std::numeric_limits<double>::infinity();
        }

        if (target_z >= z_end) {
            z_steps.push_back(current_z);
            z_steps.push_back(target_z);
            v_steps.push_back(avg_v);
            v_steps.push_back(avg_v);
            break;
        }

        if (contrast_val <= (1.0 / contrast) || contrast_val >= contrast) {
            z_steps.push_back(current_z);
            z_steps.push_back(target_z);
            v_steps.push_back(avg_v);
            v_steps.push_back(avg_v);
            current_z = target_z;
            last_v = avg_v;
            current_step = initial_step;
            current_index = temp_index;
        }
        else {
            current_step += 1.0;
        }
    }

    z_steps.push_back(z_end);
    v_steps.push_back(v_filtered.back());

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
    double step,
    double contrast,
    double undef_val,
    int new_min,
    int new_max)
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
    const size_t num_steps = static_cast<size_t>(std::ceil((z_end - z_start) / step)) + 1;

    std::vector<double> z_steps(2 * num_steps);
    std::vector<double> v_steps(2 * num_steps);

    size_t current_index = 0;
    double v_val = 0.0;

    for (size_t step_idx = 0; step_idx < num_steps; step_idx++) {
        double z0 = z_start + step_idx * step;
        double z1 = z0 + step;

        double sum = 0.0;
        size_t count = 0;

        while (current_index < z_filtered.size() && z_filtered[current_index] < z1) {
            sum += v_filtered[current_index];
            count++;
            current_index++;
        }

        if (count > 0) {
            v_val = sum / count;
        }
        else if (step_idx > 0) { // не первое значение
            v_val = v_steps[2 * step_idx - 1];
        }

        z_steps[2 * step_idx] = z0;
        v_steps[2 * step_idx] = v_val;

        z_steps[2 * step_idx + 1] = z1;
        v_steps[2 * step_idx + 1] = v_val;
    }

    v_steps.pop_back();
    z_steps.pop_back();

    z_steps.insert(z_steps.begin(), z_filtered.front());
    v_steps.insert(v_steps.begin(), v_filtered.front());



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

py::tuple perform_calculation_no_contrast_iter(
    py::array_t<double> z_array,
    py::array_t<double> v_array,
    double min_z,
    double max_z,
    double step,
    double contrast,
    double undef_val,
    int new_min,
    int new_max)
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

    size_t filtered_size = z_filtered.size();

    size_t num_steps = (filtered_size + static_cast<size_t>(step) - 1) / static_cast<size_t>(step);

    std::vector<double> z_steps;
    std::vector<double> v_steps;

    for (size_t i = 0; i < num_steps; i++) {
        size_t idx = i * static_cast<size_t>(step);
        if (idx >= filtered_size) {
            idx = filtered_size - 1;
        }

        double z_val = z_filtered[idx];
        double v_val = v_filtered[idx];

        if (i == 0) {
            z_steps.push_back(z_val);
            v_steps.push_back(v_val);
        }
        else {
            z_steps.push_back(z_val);
            v_steps.push_back(v_steps.back());

            z_steps.push_back(z_val);
            v_steps.push_back(v_val);
        }
    }

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
        py::arg("undef_val"),
        py::arg("new_min"), 
        py::arg("new_max"));

    m.def("perform_calculation2", &perform_calculation_no_contrast,
        py::arg("z_array"),
        py::arg("v_array"),
        py::arg("min_z"),
        py::arg("max_z"),
        py::arg("step"),
        py::arg("contrast"),
        py::arg("undef_val"),
        py::arg("new_min"),
        py::arg("new_max"));

    m.def("perform_calculation3", &perform_calculation_no_contrast_iter,
        py::arg("z_array"),
        py::arg("v_array"),
        py::arg("min_z"),
        py::arg("max_z"),
        py::arg("step"),
        py::arg("contrast"),
        py::arg("undef_val"),
        py::arg("new_min"),
        py::arg("new_max"));

    m.def("calculate_statistics2", &calculate_statistics);

    m.def("add", &add);

    m.def("add_vec", &add_vec);

    m.def("add_vects", &add_vects);
}
