import numpy as np
from PySide6.QtWidgets import QFileDialog, QMainWindow, QVBoxLayout

from model import Model
from ui_window import Ui_MainWindow
from widget_drawer import MplCanvas


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.original_line = None
        self.step_line = None

        self.model = Model()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.PB_Choose_file.clicked.connect(self.choose_file_name)
        self.ui.PB_Import_Data.clicked.connect(self.import_data)
        self.ui.PB_Calculate.clicked.connect(self.calculate)
        self.ui.PB_Export.clicked.connect(self.export_data)
        self.ui.PB_Clear_All.clicked.connect(self.clear_all_graphs)
        # self.ui.PB_Clear_Step.clicked.connect(self.clear_step_graph)

        self.ui.SB_Contrast.valueChanged.connect(self.contrast_changed)
        self.ui.SB_Step.valueChanged.connect(self.step_val_changed)
        self.ui.SB_Max_Z.valueChanged.connect(self.max_z_changed)
        self.ui.SB_Min_Z.valueChanged.connect(self.min_z_changed)
        self.ui.SB_uv.valueChanged.connect(self.undef_val_changed)
        self.ui.SB_Max_Norm.valueChanged.connect(self.norm_max_val_changed)
        self.ui.SB_Min_Norm.valueChanged.connect(self.norm_min_val_changed)

        self.ui.CB_list_choose.currentIndexChanged.connect(self.combobox_list_choose_change)
        self.ui.CB_data_choose.currentIndexChanged.connect(self.combobox_data_choose_change)

        self.ui.CheckBox_Remove_Original.toggled.connect(self.remove_original_graph)
        self.ui.CheckBox_Remove_Step.toggled.connect(self.remove_step_graph)

        self.ui.lineEdit_data.textChanged.connect(self.text_changed)
        self.ui.lineEdit_data.textEdited.connect(self.text_edited)
        self.ui.lineEdit_data.returnPressed.connect(self.return_pressed)

        self.canvas = MplCanvas(self.ui.widget)
        layout = QVBoxLayout(self.ui.widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)

    def choose_file_name(self) -> None:  # выбор файла для считывания данных и динамическое заполнение именами листов
        file, _ = QFileDialog.getOpenFileName(self, '', '', 'Excel Files (*.xlsx)')
        if not file:
            return
        self.ui.lineEdit_data.setText(file)
        sheet_names = self.model.load_excel(file)
        self.ui.CB_list_choose.blockSignals(True)
        self.ui.CB_list_choose.clear()
        self.ui.CB_list_choose.addItems(sheet_names)
        self.ui.CB_list_choose.setCurrentIndex(0)
        self.ui.CB_list_choose.blockSignals(False)
        self.combobox_list_choose_change()

    def combobox_list_choose_change(self) -> None:  # динамическое заполнение именами колонок и выбор листа
        sheet = self.ui.CB_list_choose.currentText()
        print(f'Chosen sheet {sheet}')

        columns = self.model.select_sheet(sheet)

        self.ui.CB_data_choose.blockSignals(True)
        self.ui.CB_data_choose.clear()
        self.ui.CB_data_choose.addItems(columns)
        self.ui.CB_data_choose.setCurrentIndex(0)
        self.ui.CB_data_choose.blockSignals(False)
        self.combobox_data_choose_change()

    def combobox_data_choose_change(self) -> None:  # выбор колонки
        column = self.ui.CB_data_choose.currentText()
        print(f'Chosen column {column}')
        self.model.select_column(column)

    def import_data(self) -> None:  # загрузка данных
        print('Importing data')
        self.model.import_data()
        if self.model.data_frame is not None:
            print(self.model.data_frame.head())

    def calculate(self) -> None:  # вычисления
        self.ui.CheckBox_Remove_Original.setChecked(False)
        self.ui.CheckBox_Remove_Step.setChecked(False)
        v_data, z_data, x_steps, z_steps = self.model.perform_calculation1(
            self.ui.SB_Min_Z.value(),
            self.ui.SB_Max_Z.value(),
            self.ui.SB_Contrast.value(),
            self.ui.SB_Step.value(),
            self.ui.SB_uv.value(),
            self.ui.SB_Min_Norm.value(),
            self.ui.SB_Max_Norm.value(),
        )

        self.plot_results(v_data, z_data, x_steps, z_steps)

        v_step_min, v_step_max, v_step_mean, v_step_std = self.model.compute_statistics2(z_steps)  # подсчет статистики
        self.perform_step_statistics(v_step_min, v_step_max, v_step_mean, v_step_std)

        v_orig_min, v_orig_max, v_orig_mean, v_orig_std = self.model.compute_statistics2(z_data)  # подсчет статистики
        self.perform_orig_statistics(v_orig_min, v_orig_max, v_orig_mean, v_orig_std)

    def perform_step_statistics(self, v_min: float, v_max: float, v_mean: float, v_std: float) -> None:  # результаты ступенчатого графика
        self.ui.lb_step_min_val.setText(str(format(v_min, '.2f')))
        self.ui.lb_step_max_val.setText(str(format(v_max, '.2f')))
        self.ui.lb_step_mean_val.setText(str(format(v_mean, '.2f')))
        self.ui.lb_step_std_val.setText(str(format(v_std, '.2f')))

    def perform_orig_statistics(self, v_min: float, v_max: float, v_mean: float, v_std: float) -> None:  # результаты ступенчатого графика
        self.ui.lb_orig_min_val.setText(str(format(v_min, '.2f')))
        self.ui.lb_orig_max_val.setText(str(format(v_max, '.2f')))
        self.ui.lb_orig_mean_val.setText(str(format(v_mean, '.2f')))
        self.ui.lb_orig_std_val.setText(str(format(v_std, '.2f')))

    def export_data(self) -> None:  # выгрузка данных
        self.model.save_to_file_xlsx('Обработанные данные.xlsx')
        print('Data export')

    def plot_results(self, v_data: np.ndarray, z_data: np.ndarray, x_steps: np.ndarray, z_steps: np.ndarray) -> None:  # построение графика
        ax = self.canvas.ax
        ax_top = self.canvas.ax_top

        # Очищаем содержимое обеих осей
        ax.cla()
        ax_top.cla()

        # Инвертируем ось y заново после очистки
        ax.invert_yaxis()

        # Скрываем нижнюю ось x и правую границу основной оси
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(True)
        ax.spines['top'].set_visible(True)

        # Восстанавливаем подписи и положение осей
        ax.set_ylabel('Z', fontsize=8)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_ticks_position('left')

        # Строим графики на основной оси
        self.original_line = ax.plot(z_data, v_data, 'b-', label='Original graph')[0]
        self.step_line = ax.plot(z_steps, x_steps, 'r-', label='Step graph')[0]

        # Настраиваем верхнюю ось
        ax_top.spines['top'].set_visible(True)
        ax_top.spines['bottom'].set_visible(False)
        ax_top.xaxis.set_ticks_position('top')
        ax_top.xaxis.set_label_position('top')
        ax_top.set_xlabel('V', fontsize=8)

        # Устанавливаем одинаковые пределы по X для обеих осей
        ax_top.set_xlim(ax.get_xlim())

        # Легенда и сетка на основной оси
        ax.legend(loc='lower right')
        ax.grid(True)

        # Отступы
        self.canvas.fig.subplots_adjust(left=0.25, top=0.85)

        # Обновляем холст
        self.canvas.fig.canvas.draw_idle()

    def clear_all_graphs(self) -> None:  # удаляет все графики
        ax = self.canvas.ax
        ax.clear()
        ax.figure.canvas.draw()
        self.original_line = None
        self.step_line = None

    # такой кнопки больше нет
    # def clear_step_graph(self) -> None:  # удаляет ступенчатый график
    #     if self.step_line is not None:
    #         self.step_line.remove()
    #         self.step_line = None
    #         self.canvas.ax.figure.canvas.draw()

    def remove_original_graph(self, checked: bool) -> None:  # скрывает исходный график
        if self.original_line is not None:
            self.original_line.set_visible(not checked)
            self.canvas.draw()

    def remove_step_graph(self, checked: bool) -> None:  # скрывает ступенчатый график
        if self.step_line is not None:
            self.step_line.set_visible(not checked)
            self.canvas.draw()

    def norm_max_val_changed(self, value: int) -> None:
        print(f'Value of max norm {value}')

    def norm_min_val_changed(self, value: int) -> None:
        print(f'Value of min norm {value}')

    def contrast_changed(self, value: int) -> None:
        print(f'Value of contrast {value}')

    def step_val_changed(self, value: int) -> None:
        print(f'Value of step {value}')

    def max_z_changed(self, value: int) -> None:
        print(f'Max z = {value}')

    def min_z_changed(self, value: int) -> None:
        print(f'Min z = {value}')

    def text_changed(self, text: str) -> None:
        print(f'Text changed {text}')

    def text_edited(self, text: str) -> None:
        print(f'Text edited {text}')

    def return_pressed(self) -> None:
        print('Enter was pressed')

    def undef_val_changed(self, value: int) -> None:
        print(f'Undefined value changed {value}')
