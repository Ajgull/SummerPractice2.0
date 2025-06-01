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

            valid_data = (v_data != self.undefined_value)
            z_data_filtered = z_data[valid_data]
            v_data_filtered = v_data[valid_data]

            range_data = (z_data_filtered >= min_z) & (z_data_filtered <= max_z)
            z_data_filtered = z_data_filtered[range_data]
            v_data_filtered = v_data_filtered[range_data]

            if len(z_data_filtered) == 0:
                return np.array([]), np.array([]), np.array([]), np.array([])

            z_start = z_data_filtered[0]
            z_end = z_data_filtered[-1]

            z_steps = np.arange(z_start, z_end + step, step)

            x_steps = np.interp(z_steps, z_data_filtered, v_data_filtered)

            x_steps = np.insert(x_steps, 0, v_data_filtered[0])
            x_steps = np.append(x_steps, v_data_filtered[-1])

            z_steps = np.insert(z_steps, 0, z_data_filtered[0])
            z_steps = np.append(z_steps, z_data_filtered[-1])

            self.result = (x_steps, z_steps)

            print('Filtered z_data:', z_data_filtered)
            print('Filtered v_data:', v_data_filtered)

            return z_data_filtered, v_data_filtered, z_steps, x_steps
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
