import pandas as pd
from PySide6.QtWidgets import QFileDialog, QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt
from ui_window import Ui_MainWindow
from WidgetDrawer import MplCanvas
import matplotlib.pyplot as plt
from Model import Model

class MainWindow(QMainWindow):
    def __init__(self):
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
        self.ui.PB_Clear_Step.clicked.connect(self.clear_step_graph)

        self.ui.SB_Contrast.valueChanged.connect(self.contrast_changed)
        self.ui.SB_Step.valueChanged.connect(self.step_val_changed)
        self.ui.SB_Max_Z.valueChanged.connect(self.max_z_changed)
        self.ui.SB_Min_Z.valueChanged.connect(self.min_z_changed)
        self.ui.SB_uv.valueChanged.connect(self.undef_val_changed)

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

    def choose_file_name(self):
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

    def combobox_list_choose_change(self):
        sheet = self.ui.CB_list_choose.currentText()
        print(f"Chosen sheet {sheet}")

        columns = self.model.select_sheet(sheet)

        self.ui.CB_data_choose.blockSignals(True)
        self.ui.CB_data_choose.clear()
        self.ui.CB_data_choose.addItems(columns)
        self.ui.CB_data_choose.setCurrentIndex(0)
        self.ui.CB_data_choose.blockSignals(False)
        self.combobox_data_choose_change()

    def combobox_data_choose_change(self):
        column = self.ui.CB_data_choose.currentText()
        print(f"Chosen column {column}")
        self.model.select_column(column)

    def import_data(self):
        print(f"Importing data")
        self.model.import_data()
        print(self.model.data_frame.head())

    def calculate(self):
        v_data, z_data, x_steps, z_steps = self.model.perform_calculation2(
            self.ui.SB_Min_Z.value(),
            self.ui.SB_Max_Z.value(),
            self.ui.SB_Contrast.value(),
            self.ui.SB_Step.value(),
            self.ui.SB_uv.value()
        )

        self.plot_results(v_data, z_data, x_steps, z_steps)

        # v_min, v_max, v_mean, v_std = self.model.compute_statistics()
        # self.preform_statistics(v_min, v_max, v_mean, v_std)

    def preform_statistics(self, v_min, v_max, v_mean, v_std):
        self.ui.LB_Min_Val.setText(str(format(v_min, '.2f')))
        self.ui.LB_Max_Val.setText(str(format(v_max, '.2f')))
        self.ui.LB_Mean_Val.setText(str(format(v_mean, '.2f')))
        self.ui.LB_Std_Val.setText(str(format(v_std, '.2f')))

    def export_data(self):
        self.model.save_to_file_xlsx("Обработанные данные.xlsx")
        print('Data export')

    def plot_results(self, v_data, z_data, x_steps, z_steps):
        ax = self.canvas.ax
        ax.clear()

        plt.rcParams.update({'font.size': 8})

        mask = (v_data >= self.ui.SB_Min_Z.value()) & (v_data <= self.ui.SB_Max_Z.value())
        ax.invert_yaxis()
        self.original_line = ax.plot(z_data[mask], v_data[mask], 'b-', label='Original graph')[0]
        self.step_line = ax.step(z_steps, x_steps, 'r-', where='post', label='Step graph')[0]
        ax.set_ylabel('Z')
        ax.spines['bottom'].set_visible(False)
        ax.xaxis.set_visible(False)

        self.canvas.fig.subplots_adjust(left=0.3)

        ax_top = ax.twiny()
        ax_top.set_xlim(ax.get_xlim())
        ax_top.set_xlabel('V')
        ax_top.xaxis.set_label_position('top')
        ax_top.xaxis.tick_top()
        ax.legend(loc='lower right')
        ax.grid(True)
        ax.figure.canvas.draw()

    def clear_all_graphs(self):
        ax = self.canvas.ax
        ax.clear()
        ax.figure.canvas.draw()
        self.original_line = None
        self.step_line = None

    def clear_step_graph(self):
        if self.step_line is not None:
            self.step_line.remove()
            self.step_line = None
            self.canvas.ax.figure.canvas.draw()

    def remove_original_graph(self, checked: bool):
        if self.original_line is not None:
            self.original_line.set_visible(not checked)
            self.canvas.draw()

    def remove_step_graph(self, checked: bool):
        if self.step_line is not None:
            self.step_line.set_visible(not checked)
            self.canvas.draw()

    def contrast_changed(self, value):
        print(f'Value of contrast {value}')

    def step_val_changed(self, value):
        print(f'Value of step {value}')

    def max_z_changed(self, value):
        print(f'Max z = {value}')

    def min_z_changed(self, value):
        print(f'Min z = {value}')

    def text_changed(self, text):
        print(f'Text changed {text}')

    def text_edited(self, text):
        print(f'Text edited {text}')

    def return_pressed(self):
        print(f'Enter was pressed')

    def undef_val_changed(self, value):
        print(f'Undefined value changed {value}')
