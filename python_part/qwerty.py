import pandas as pd
import numpy as np
import example
import matplotlib.pyplot as plt


class DataProcessor:
    def __init__(self, df):
        self.data_frame = df
        self.result = None
        self.undefined_value = -999.25

    def perform_calculation_pybind(self, min_z, max_z, contrast, step, undef_val):
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
            print("No data to calculate")


df = pd.DataFrame({
    'v': np.linspace(0, 10, 20),
    'z': np.sin(np.linspace(0, 10, 20))
})

processor = DataProcessor(df)
v_f, z_f, v_s, z_s = processor.perform_calculation_pybind(1, 9, contrast=1, step=2, undef_val=-999.25)

plt.figure(figsize=(10, 6))

plt.plot(v_f, z_f, color='blue', label='Original graph')

plt.step(v_s, z_s, color='red', label='Step graph')

plt.xlabel('v')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()
