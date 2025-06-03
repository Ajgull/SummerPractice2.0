import example
import numpy as np
import pandas as pd


class Model:
    def __init__(self) -> None:
        self.file_path = None
        self.current_excel = None  # объект ExcelFile
        self.sheet = None
        self.column = None
        self.data_frame = None
        self.min_z = None
        self.max_z = None
        self.undefined_value = None
        self.new_min = None
        self.new_max = None
        self.statistics_min = None
        self.statistics_max = None
        self.statistics_mean = None
        self.statistics_std = None
        self.result = None

    def load_excel(self, file_path: str) -> list[str]:  # загрузка данных
        self.file_path = file_path
        self.current_excel = pd.ExcelFile(file_path)
        return self.current_excel.sheet_names

    def select_sheet(self, sheet: str) -> list[str]:  # выбор страницы в файле экселя
        self.sheet = sheet
        df = pd.read_excel(self.current_excel, sheet_name=sheet, nrows=0)
        return df.columns.tolist()[2:]

    def select_column(self, column: str) -> None:  # выбор колонки
        self.column = column

    def import_data(self) -> None:  # импорт данных
        if not self.file_path or not self.sheet or not self.column:
            print('File, sheet or column not chosen')
            return
        df = pd.read_excel(self.current_excel, sheet_name=self.sheet, usecols=[self.column, 'MD'])
        self.data_frame = df

        self.min_z = self.data_frame.iloc[:, 0].min()
        self.max_z = self.data_frame.iloc[:, 0].max()
        print(self.min_z, self.max_z)

    def _norm_data(self, data: np.array, mask: np.array) -> np.array:  # нормировка данных
        print('normalizing data')

        if self.new_min == self.new_max:
            return data.copy()

        v_norm_data = data.copy()
        if np.any(mask):
            v_min = data[mask].min()
            v_max = data[mask].max()

            v_norm_data[mask] = (data[mask] - v_min) / (v_max - v_min) * (self.new_max - self.new_min) + self.new_min
        return v_norm_data

    def perform_calculation(self, min_z: float, max_z: float, contrast: float, step: float, undef_val: float,
                            new_min: int, new_max: int) \
            -> tuple[
                np.ndarray, np.ndarray, np.ndarray, np.ndarray]:  # вычисления без контрастности с нормировкой, питон
        print('perform calculation python')
        self.undefined_value = undef_val
        self.new_min = new_min
        self.new_max = new_max
        if self.data_frame is not None and not self.data_frame.empty:

            z_data = self.data_frame.iloc[:, 0].to_numpy()
            v_data = self.data_frame.iloc[:, 1].to_numpy()

            valid_data = (v_data != self.undefined_value)

            v_data = self._norm_data(v_data, valid_data)  # нормировка данных

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
            print('No data to calculate')
            return np.array([]), np.array([]), np.array([]), np.array([])

    def perform_calculation1(self, min_z: float, max_z: float, contrast: float, step: float, undef_val: float,
                             new_min: int, new_max: int) \
            -> tuple[
                np.ndarray, np.ndarray, np.ndarray, np.ndarray]:  # вычисления с контрастностью и с нормировкой, питон
        print('perform calculation python')
        self.undefined_value = undef_val
        self.new_min = new_min
        self.new_max = new_max
        if self.data_frame is not None and not self.data_frame.empty:
            z_data = self.data_frame.iloc[:, 0].to_numpy()
            v_data = self.data_frame.iloc[:, 1].to_numpy()

            valid_mask = (v_data != undef_val) & (z_data >= min_z) & (z_data <= max_z)

            v_data = self._norm_data(v_data, valid_mask)  # нормировка данных

            z_filtered = z_data[valid_mask]
            v_filtered = v_data[valid_mask]

            if len(z_filtered) == 0:
                return np.array([]), np.array([]), np.array([]), np.array([])

            z_start = z_filtered[0]
            z_end = z_filtered[-1]

            z_steps = []
            v_steps = []

            z_steps.append(z_start)
            v_steps.append(v_filtered[0])

            current_index = 0
            current_z = z_start
            last_v = v_filtered[0]
            initial_step = step
            current_step = initial_step

            while current_z < z_end and current_index < len(z_filtered):
                target_z = min(current_z + current_step, z_end)

                sum_v = 0.0
                count = 0
                temp_index = current_index

                while temp_index < len(z_filtered) and z_filtered[temp_index] < target_z:
                    sum_v += v_filtered[temp_index]
                    count += 1
                    temp_index += 1

                if count == 0:
                    z_steps.extend([current_z, target_z])
                    v_steps.extend([last_v, last_v])
                    current_z = target_z
                    current_index = temp_index
                    current_step = initial_step
                    continue

                avg_v = sum_v / count
                ratio = avg_v / last_v if last_v != 0 else float('inf')
                print(ratio, current_step)

                if target_z >= z_end:
                    z_steps.extend([current_z, target_z])
                    v_steps.extend([avg_v, avg_v])
                    break

                if ratio <= 1 / contrast or ratio >= contrast:
                    z_steps.extend([current_z, target_z])
                    v_steps.extend([avg_v, avg_v])
                    current_z = target_z
                    last_v = avg_v
                    current_step = initial_step
                    current_index = temp_index
                else:
                    current_step += 1.0

            z_steps.append(z_filtered[-1])
            v_steps.append(v_filtered[-1])

            self.result = (z_steps, v_steps)

            return np.array(z_filtered), np.array(v_filtered), np.array(z_steps), np.array(v_steps)
        else:
            print('No data to calculate')
            return np.array([]), np.array([]), np.array([]), np.array([])

    def perform_calculation2(self, min_z: float, max_z: float, contrast: float, step: float, undef_val: float,
                             new_min: int, new_max: int) \
            -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:  # вычисления с контрастностью и с нормировкой c++
        print('perform calculation pybind2')

        self.undefined_value = undef_val
        self.new_min = new_min
        self.new_max = new_max

        if self.data_frame is not None and not self.data_frame.empty:
            input_data = self.data_frame.iloc[:, :2].to_numpy(dtype=np.float64)

            z_array = input_data[:, 0]
            v_array = input_data[:, 1]

            z_filtered, v_filtered, z_steps, v_steps = example.perform_calculation(
                z_array, v_array, min_z, max_z, step, contrast, self.undefined_value, self.new_min, self.new_max
            )

            self.result = (z_steps, v_steps)

            print(z_filtered)
            print(v_filtered)
            print(z_steps)
            print(v_steps)
            return z_filtered, v_filtered, z_steps, v_steps
        else:
            print('No data to calculate')
            return np.array([]), np.array([]), np.array([]), np.array([])

    def compute_statistics2(self, z_steps: np.array) -> tuple[float, float, float, float]:  # вычисления статистики c++
        if self.result is None:
            print('No results to calculate statistics2')
            return 0.0, 0.0, 0.0, 0.0

        # z_steps = self.result[1]

        self.statistics_min, self.statistics_max, self.statistics_mean, self.statistics_std = (
            example.calculate_statistics2(z_steps))
        return self.statistics_min, self.statistics_max, self.statistics_mean, self.statistics_std

    def compute_statistics(self, z_steps: np.array) -> tuple[float, float, float, float]:  # вычисления статистики питон
        if self.result is None:
            print('No results to calculate statistics')
            return 0.0, 0.0, 0.0, 0.0

        # z_steps = self.result[0]

        self.statistics_min = np.min(z_steps)
        self.statistics_max = np.max(z_steps)
        self.statistics_mean = np.mean(z_steps)
        self.statistics_std = np.std(z_steps)

        return self.statistics_min, self.statistics_max, self.statistics_mean, self.statistics_std

    def save_to_file_xlsx(self, filename: str) -> None:  # выгрузка данных
        if self.result is None:
            print('No results to save')
            return
        x_steps, z_steps = self.result
        df_export = pd.DataFrame({
            'X_steps': x_steps,
            'Z_steps': z_steps
        })
        df_export.to_excel(filename, index=False)
