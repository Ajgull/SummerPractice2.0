import example
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class DataProcessor:
    def __init__(self, df: pd.DataFrame) -> None:
        self.data_frame = df
        self.result = None
        self.undefined_value = -999.25

    def perform_calculation_pybind(self, min_z: float, max_z: float, contrast: float, step: float, undef_val: float) \
            -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        self.undefined_value = undef_val
        if self.data_frame is not None and not self.data_frame.empty:
            input_data = self.data_frame.iloc[:, :2].to_numpy(dtype=np.float64)

            z_array = input_data[:, 0]
            v_array = input_data[:, 1]

            z_filtered, v_filtered, z_steps, v_steps = example.perform_calculation(
                z_array, v_array, min_z, max_z, step, contrast, self.undefined_value
            )

            self.result = (z_steps, v_steps)

            print(z_filtered)
            print(v_filtered)
            print(z_steps)
            print(v_steps)
            return z_filtered, v_filtered, z_steps, v_steps
        else:
            print('No data to calculate')

    def perform_calculation1(self, min_z: float, max_z: float, contrast: float, step: float, undef_val: float) \
            -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        print('perform calculation python')
        self.undefined_value = undef_val
        if self.data_frame is not None and not self.data_frame.empty:
            z_data = self.data_frame.iloc[:, 0].to_numpy()
            v_data = self.data_frame.iloc[:, 1].to_numpy()
            valid_mask = (v_data != undef_val) & (z_data >= min_z) & (z_data <= max_z)
            z_filtered = z_data[valid_mask]
            v_filtered = v_data[valid_mask]

            if len(z_filtered) == 0:
                return np.array([]), np.array([]), np.array([]), np.array([])

            z_start = z_filtered[0]
            z_end = z_filtered[-1]

            z_steps = [z_start]
            v_steps = [v_filtered[0]]

            current_index = 0
            current_z = z_start
            last_v = v_filtered[0]
            initial_step = step
            current_step = initial_step

            while current_z < z_end and current_index < len(z_filtered):
                target_z = min(current_z + current_step, z_end)

                # Сбор данных в интервале
                sum_v = 0.0
                count = 0
                temp_index = current_index

                while temp_index < len(z_filtered) and z_filtered[temp_index] < target_z:
                    sum_v += v_filtered[temp_index]
                    count += 1
                    temp_index += 1

                # Обработка интервала
                if count == 0:
                    # Нет данных - просто продвигаемся
                    z_steps.extend([current_z, target_z])
                    v_steps.extend([last_v, last_v])
                    current_z = target_z
                    current_index = temp_index
                    current_step = initial_step
                    continue

                avg_v = sum_v / count

                # Безопасное вычисление ratio
                if last_v == 0:
                    ratio = float('inf') if avg_v != 0 else 1.0
                else:
                    ratio = avg_v / last_v

                print(ratio, current_z, last_v, current_step)

                if contrast > 1:
                    # Стандартная проверка для contrast > 1
                    is_significant_change = (ratio >= contrast) or (ratio <= 1 / contrast)
                elif contrast == 1:
                    # Любое изменение считается значимым
                    is_significant_change = (ratio != 1.0)
                else:
                    # Для contrast < 1 (если нужно более агрессивное сглаживание)
                    is_significant_change = (ratio >= 1 / contrast) or (ratio <= contrast)

                # Конец данных всегда считается значимым изменением
                if target_z >= z_end:
                    is_significant_change = True

                # Обработка результата проверки
                if is_significant_change:
                    z_steps.extend([current_z, target_z])
                    v_steps.extend([avg_v, avg_v])
                    current_z = target_z
                    last_v = avg_v
                    current_step = initial_step
                    current_index = temp_index
                else:
                    current_step += 1.0  # Лучше увеличивать на initial_step, а не на 1.0

            if z_steps[-1] != z_end:
                z_steps.append(z_end)
                v_steps.append(v_filtered[-1])

            self.result = (z_steps, v_steps)
            return np.array(z_filtered), np.array(v_filtered), np.array(z_steps), np.array(v_steps)
        else:
            print('No data to calculate')
            return np.array([]), np.array([]), np.array([]), np.array([])


df = pd.DataFrame({
    'v': np.linspace(0, 10, 10),
    'z': np.sin(np.linspace(0, 10, 10))
})

processor = DataProcessor(df)
v_f, z_f, v_s, z_s = processor.perform_calculation_pybind(0, 10, contrast=1, step=5, undef_val=-999.25)

plt.figure(figsize=(10, 6))

plt.plot(v_f, z_f, color='blue', label='Original graph')

plt.plot(v_s, z_s, color='red', label='Step graph')

plt.xlabel('v')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()
