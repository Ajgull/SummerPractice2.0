# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ui_window.ui'
##
# Created by: Qt User Interface Compiler version 6.9.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u'MainWindow')
        MainWindow.resize(465, 604)
        MainWindow.setMinimumSize(QSize(465, 604))
        MainWindow.setBaseSize(QSize(450, 516))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u'centralwidget')
        self.centralwidget.setStyleSheet(u'')
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u'gridLayout_4')
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u'splitter')
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.horizontalLayoutWidget_3 = QWidget(self.splitter)
        self.horizontalLayoutWidget_3.setObjectName(u'horizontalLayoutWidget_3')
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u'horizontalLayout_3')
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName(u'label')
        self.label.setMinimumSize(QSize(80, 11))
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_data = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_data.setObjectName(u'lineEdit_data')

        self.horizontalLayout_3.addWidget(self.lineEdit_data)

        self.PB_Choose_file = QPushButton(self.horizontalLayoutWidget_3)
        self.PB_Choose_file.setObjectName(u'PB_Choose_file')

        self.horizontalLayout_3.addWidget(self.PB_Choose_file)

        self.splitter.addWidget(self.horizontalLayoutWidget_3)
        self.horizontalLayoutWidget_4 = QWidget(self.splitter)
        self.horizontalLayoutWidget_4.setObjectName(u'horizontalLayoutWidget_4')
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u'horizontalLayout_4')
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.horizontalLayoutWidget_4)
        self.widget.setObjectName(u'widget')
        self.widget.setMinimumSize(QSize(212, 450))
        self.widget.setStyleSheet(u'background-color:red;')

        self.horizontalLayout_4.addWidget(self.widget)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u'verticalLayout_8')
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u'horizontalLayout_5')
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u'verticalLayout_10')
        self.LB_list = QLabel(self.horizontalLayoutWidget_4)
        self.LB_list.setObjectName(u'LB_list')
        self.LB_list.setMinimumSize(QSize(92, 24))
        self.LB_list.setFrameShape(QFrame.Shape.Box)
        self.LB_list.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.LB_list)

        self.LB_data = QLabel(self.horizontalLayoutWidget_4)
        self.LB_data.setObjectName(u'LB_data')
        self.LB_data.setMinimumSize(QSize(92, 24))
        self.LB_data.setFrameShape(QFrame.Shape.Box)
        self.LB_data.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.LB_data)

        self.LB_undef_val = QLabel(self.horizontalLayoutWidget_4)
        self.LB_undef_val.setObjectName(u'LB_undef_val')
        self.LB_undef_val.setMinimumSize(QSize(92, 24))
        self.LB_undef_val.setFrameShape(QFrame.Shape.Box)
        self.LB_undef_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.LB_undef_val)

        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u'verticalLayout_2')
        self.CB_list_choose = QComboBox(self.horizontalLayoutWidget_4)
        self.CB_list_choose.setObjectName(u'CB_list_choose')

        self.verticalLayout_2.addWidget(self.CB_list_choose)

        self.CB_data_choose = QComboBox(self.horizontalLayoutWidget_4)
        self.CB_data_choose.setObjectName(u'CB_data_choose')

        self.verticalLayout_2.addWidget(self.CB_data_choose)

        self.SB_uv = QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.SB_uv.setObjectName(u'SB_uv')
        self.SB_uv.setMinimum(-1000.000000000000000)
        self.SB_uv.setMaximum(1000.000000000000000)
        self.SB_uv.setValue(-999.250000000000000)

        self.verticalLayout_2.addWidget(self.SB_uv)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.PB_Import_Data = QPushButton(self.horizontalLayoutWidget_4)
        self.PB_Import_Data.setObjectName(u'PB_Import_Data')

        self.verticalLayout_8.addWidget(self.PB_Import_Data)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u'horizontalLayout_2')
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u'verticalLayout_5')
        self.LB_MinZ = QLabel(self.horizontalLayoutWidget_4)
        self.LB_MinZ.setObjectName(u'LB_MinZ')
        self.LB_MinZ.setFrameShape(QFrame.Shape.Box)
        self.LB_MinZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.LB_MinZ)

        self.LB_MaxZ = QLabel(self.horizontalLayoutWidget_4)
        self.LB_MaxZ.setObjectName(u'LB_MaxZ')
        self.LB_MaxZ.setMinimumSize(QSize(0, 0))
        self.LB_MaxZ.setFrameShape(QFrame.Shape.Box)
        self.LB_MaxZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.LB_MaxZ)

        self.LB_MinNorm = QLabel(self.horizontalLayoutWidget_4)
        self.LB_MinNorm.setObjectName(u'LB_MinNorm')
        self.LB_MinNorm.setFrameShape(QFrame.Shape.Box)
        self.LB_MinNorm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.LB_MinNorm)

        self.LB_MaxNorm = QLabel(self.horizontalLayoutWidget_4)
        self.LB_MaxNorm.setObjectName(u'LB_MaxNorm')
        self.LB_MaxNorm.setFrameShape(QFrame.Shape.Box)
        self.LB_MaxNorm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.LB_MaxNorm)

        self.LB_Contrast = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Contrast.setObjectName(u'LB_Contrast')
        self.LB_Contrast.setFrameShape(QFrame.Shape.Box)
        self.LB_Contrast.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.LB_Contrast)

        self.LB_Step = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Step.setObjectName(u'LB_Step')
        self.LB_Step.setFrameShape(QFrame.Shape.Box)
        self.LB_Step.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.LB_Step)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u'verticalLayout_6')
        self.SB_Min_Z = QSpinBox(self.horizontalLayoutWidget_4)
        self.SB_Min_Z.setObjectName(u'SB_Min_Z')
        self.SB_Min_Z.setMinimum(1)
        self.SB_Min_Z.setMaximum(100000)
        self.SB_Min_Z.setValue(1100)

        self.verticalLayout_6.addWidget(self.SB_Min_Z)

        self.SB_Max_Z = QSpinBox(self.horizontalLayoutWidget_4)
        self.SB_Max_Z.setObjectName(u'SB_Max_Z')
        self.SB_Max_Z.setMinimum(1)
        self.SB_Max_Z.setMaximum(100000)
        self.SB_Max_Z.setValue(1500)

        self.verticalLayout_6.addWidget(self.SB_Max_Z)

        self.SB_Min_Norm = QSpinBox(self.horizontalLayoutWidget_4)
        self.SB_Min_Norm.setObjectName(u'SB_Min_Norm')

        self.verticalLayout_6.addWidget(self.SB_Min_Norm)

        self.SB_Max_Norm = QSpinBox(self.horizontalLayoutWidget_4)
        self.SB_Max_Norm.setObjectName(u'SB_Max_Norm')
        self.SB_Max_Norm.setValue(0)

        self.verticalLayout_6.addWidget(self.SB_Max_Norm)

        self.SB_Contrast = QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.SB_Contrast.setObjectName(u'SB_Contrast')
        self.SB_Contrast.setDecimals(5)
        self.SB_Contrast.setSingleStep(0.010000000000000)
        self.SB_Contrast.setValue(1.000000000000000)

        self.verticalLayout_6.addWidget(self.SB_Contrast)

        self.SB_Step = QSpinBox(self.horizontalLayoutWidget_4)
        self.SB_Step.setObjectName(u'SB_Step')
        self.SB_Step.setMinimum(1)
        self.SB_Step.setMaximum(100000)
        self.SB_Step.setValue(5)

        self.verticalLayout_6.addWidget(self.SB_Step)

        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.PB_Calculate = QPushButton(self.horizontalLayoutWidget_4)
        self.PB_Calculate.setObjectName(u'PB_Calculate')

        self.verticalLayout_8.addWidget(self.PB_Calculate)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u'verticalLayout_7')
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u'verticalLayout_11')
        self.PB_Clear_All = QPushButton(self.horizontalLayoutWidget_4)
        self.PB_Clear_All.setObjectName(u'PB_Clear_All')

        self.verticalLayout_11.addWidget(self.PB_Clear_All)

        self.PB_Clear_Step = QPushButton(self.horizontalLayoutWidget_4)
        self.PB_Clear_Step.setObjectName(u'PB_Clear_Step')

        self.verticalLayout_11.addWidget(self.PB_Clear_Step)

        self.PB_Export = QPushButton(self.horizontalLayoutWidget_4)
        self.PB_Export.setObjectName(u'PB_Export')

        self.verticalLayout_11.addWidget(self.PB_Export)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u'horizontalLayout_7')
        self.CheckBox_Remove_Step = QCheckBox(self.horizontalLayoutWidget_4)
        self.CheckBox_Remove_Step.setObjectName(u'CheckBox_Remove_Step')

        self.horizontalLayout_7.addWidget(self.CheckBox_Remove_Step)

        self.CheckBox_Remove_Original = QCheckBox(self.horizontalLayoutWidget_4)
        self.CheckBox_Remove_Original.setObjectName(u'CheckBox_Remove_Original')

        self.horizontalLayout_7.addWidget(self.CheckBox_Remove_Original)

        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_7.addLayout(self.verticalLayout_11)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u'horizontalLayout')
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u'verticalLayout_3')
        self.LB_Min = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Min.setObjectName(u'LB_Min')
        self.LB_Min.setFrameShape(QFrame.Shape.Box)
        self.LB_Min.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Min)

        self.LB_Max = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Max.setObjectName(u'LB_Max')
        self.LB_Max.setFrameShape(QFrame.Shape.Box)
        self.LB_Max.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Max)

        self.LB_Mean = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Mean.setObjectName(u'LB_Mean')
        self.LB_Mean.setFrameShape(QFrame.Shape.Box)
        self.LB_Mean.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Mean)

        self.LB_Std = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Std.setObjectName(u'LB_Std')
        self.LB_Std.setFrameShape(QFrame.Shape.Box)
        self.LB_Std.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Std)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u'verticalLayout_4')
        self.LB_Min_Val = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Min_Val.setObjectName(u'LB_Min_Val')
        self.LB_Min_Val.setFrameShape(QFrame.Shape.Box)
        self.LB_Min_Val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.LB_Min_Val)

        self.LB_Max_Val = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Max_Val.setObjectName(u'LB_Max_Val')
        self.LB_Max_Val.setFrameShape(QFrame.Shape.Box)
        self.LB_Max_Val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.LB_Max_Val)

        self.LB_Mean_Val = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Mean_Val.setObjectName(u'LB_Mean_Val')
        self.LB_Mean_Val.setFrameShape(QFrame.Shape.Box)
        self.LB_Mean_Val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.LB_Mean_Val)

        self.LB_Std_Val = QLabel(self.horizontalLayoutWidget_4)
        self.LB_Std_Val.setObjectName(u'LB_Std_Val')
        self.LB_Std_Val.setFrameShape(QFrame.Shape.Box)
        self.LB_Std_Val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.LB_Std_Val)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.horizontalLayout_4.setStretch(0, 3)
        self.splitter.addWidget(self.horizontalLayoutWidget_4)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate('MainWindow', u'PracticePythonWindow', None))
        self.label.setText(QCoreApplication.translate('MainWindow', u'data', None))
        self.PB_Choose_file.setText(QCoreApplication.translate('MainWindow', u'file', None))
        self.LB_list.setText(QCoreApplication.translate('MainWindow', u'list', None))
        self.LB_data.setText(QCoreApplication.translate('MainWindow', u'data', None))
        self.LB_undef_val.setText(QCoreApplication.translate('MainWindow', u'undefined value', None))
        self.CB_list_choose.setCurrentText('')
        self.PB_Import_Data.setText(QCoreApplication.translate('MainWindow', u'import', None))
        self.LB_MinZ.setText(QCoreApplication.translate('MainWindow', u'min z', None))
        self.LB_MaxZ.setText(QCoreApplication.translate('MainWindow', u'max z', None))
        self.LB_MinNorm.setText(QCoreApplication.translate('MainWindow', u'norm min', None))
        self.LB_MaxNorm.setText(QCoreApplication.translate('MainWindow', u'norm max', None))
        self.LB_Contrast.setText(QCoreApplication.translate('MainWindow', u'contrast', None))
        self.LB_Step.setText(QCoreApplication.translate('MainWindow', u'step', None))
        self.PB_Calculate.setText(QCoreApplication.translate('MainWindow', u'calculate', None))
        self.PB_Clear_All.setText(QCoreApplication.translate('MainWindow', u'clear all', None))
        self.PB_Clear_Step.setText(QCoreApplication.translate('MainWindow', u'delete step graph', None))
        self.PB_Export.setText(QCoreApplication.translate('MainWindow', u'export', None))
        self.CheckBox_Remove_Step.setText(QCoreApplication.translate('MainWindow', u'remove step', None))
        self.CheckBox_Remove_Original.setText(QCoreApplication.translate('MainWindow', u'remove original', None))
        self.LB_Min.setText(QCoreApplication.translate('MainWindow', u'min', None))
        self.LB_Max.setText(QCoreApplication.translate('MainWindow', u'max', None))
        self.LB_Mean.setText(QCoreApplication.translate('MainWindow', u'mean', None))
        self.LB_Std.setText(QCoreApplication.translate('MainWindow', u'std', None))
        self.LB_Min_Val.setText('')
        self.LB_Max_Val.setText('')
        self.LB_Mean_Val.setText('')
        self.LB_Std_Val.setText('')
    # retranslateUi
