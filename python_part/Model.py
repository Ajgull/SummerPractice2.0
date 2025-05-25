import pandas as pd
import numpy as np
import example


class Model:
    def __init__(self):
        self.file_path = None
        self.current_excel = None  # объект ExcelFile
        self.sheet = None
        self.column = None
        self.data_frame = None
        self.undefined_value = None
        self.statistics_min = None
        self.statistics_max = None
        self.statistics_mean = None
        self.statistics_std = None
        self.result = None

    def load_excel(self, file_path):
        self.file_path = file_path
        self.current_excel = pd.ExcelFile(file_path)
        return self.current_excel.sheet_names

    def select_sheet(self, sheet):
        self.sheet = sheet
        df = pd.read_excel(self.current_excel, sheet_name=sheet, nrows=0)
        return df.columns.tolist()[2:]

    def select_column(self, column):
        self.column = column

    def import_data(self):
        if not self.file_path or not self.sheet or not self.column:
            print("File, sheet or column not chosen")
            return
        df = pd.read_excel(self.current_excel, sheet_name=self.sheet, usecols=[self.column, 'MD'])
        self.data_frame = df

    def perform_calculation(self, min_z, max_z, contrast, step, undef_val):
        print(f'perform calculation python')
        self.undefined_value = undef_val
        if self.data_frame is not None and not self.data_frame.empty:

            z_data = self.data_frame.iloc[:, 0].to_numpy()
            v_data = self.data_frame.iloc[:, 1].to_numpy()

            valid_data = (v_data != self.undefined_value)

            z_data_filtered = z_data[valid_data]
            v_data_filtered = v_data[valid_data]

            range_data = (z_data_filtered >= min_z) & (z_data_filtered <= max_z)
            v_data_filtered = v_data_filtered[range_data]
            z_data_filtered = z_data_filtered[range_data]

            z_steps = np.arange(z_data_filtered[0], max_z + step, step)

            x_steps = np.interp(z_steps, z_data_filtered, v_data_filtered)

            self.result = (x_steps, z_steps)

            print(z_data_filtered, v_data_filtered)

            return z_data_filtered, v_data_filtered, z_steps, x_steps
        else:
            print(f'No data to calculate')
            return

    def perform_calculation2(self, min_z, max_z, contrast, step, undef_val):
        print(f'perform calculation pybind2')
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
            print(f'No data to calculate')
            return

    def compute_statistics2(self):
        if self.result is None:
            print(f"No results to calculate statistics2")
            return

        z_steps = self.result[1]

        self.statistics_min, self.statistics_max, self.statistics_mean, self.statistics_std = example.calculate_statistics2(z_steps)
        return self.statistics_min, self.statistics_max, self.statistics_mean, self.statistics_std

    def compute_statistics(self):
        if self.result is None:
            print(f"No results to calculate statistics")
            return

        z_steps = self.result[1]

        self.statistics_min = np.min(z_steps)
        self.statistics_max = np.max(z_steps)
        self.statistics_mean = np.mean(z_steps)
        self.statistics_std = np.std(z_steps)

        return self.statistics_min, self.statistics_max, self.statistics_mean, self.statistics_std

    def save_to_file_xlsx(self, filename):
        if self.result is None:
            print("No results to save")
            return
        x_steps, z_steps = self.result
        df_export = pd.DataFrame({
            'X_steps': x_steps,
            'Z_steps': z_steps
        })
        df_export.to_excel(filename, index=False)
