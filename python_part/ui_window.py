# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(465, 700)
        MainWindow.setMinimumSize(QSize(465, 700))
        MainWindow.setBaseSize(QSize(450, 516))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.horizontalLayoutWidget_3 = QWidget(self.splitter)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 11))
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_data = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_data.setObjectName(u"lineEdit_data")

        self.horizontalLayout_3.addWidget(self.lineEdit_data)

        self.PB_Choose_file = QPushButton(self.horizontalLayoutWidget_3)
        self.PB_Choose_file.setObjectName(u"PB_Choose_file")

        self.horizontalLayout_3.addWidget(self.PB_Choose_file)

        self.splitter.addWidget(self.horizontalLayoutWidget_3)
        self.horizontalLayoutWidget_4 = QWidget(self.splitter)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.horizontalLayoutWidget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(212, 450))
        self.widget.setStyleSheet(u"background-color:red;")

        self.horizontalLayout_4.addWidget(self.widget)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalGroupBox_6 = QGroupBox(self.horizontalLayoutWidget_4)
        self.verticalGroupBox_6.setObjectName(u"verticalGroupBox_6")
        self.verticalGroupBox_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_25 = QVBoxLayout(self.verticalGroupBox_6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.LB_list = QLabel(self.verticalGroupBox_6)
        self.LB_list.setObjectName(u"LB_list")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_list.sizePolicy().hasHeightForWidth())
        self.LB_list.setSizePolicy(sizePolicy)
        self.LB_list.setMinimumSize(QSize(90, 20))
        self.LB_list.setFrameShape(QFrame.Shape.Box)
        self.LB_list.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.LB_list)

        self.LB_data = QLabel(self.verticalGroupBox_6)
        self.LB_data.setObjectName(u"LB_data")
        sizePolicy.setHeightForWidth(self.LB_data.sizePolicy().hasHeightForWidth())
        self.LB_data.setSizePolicy(sizePolicy)
        self.LB_data.setMinimumSize(QSize(90, 20))
        self.LB_data.setFrameShape(QFrame.Shape.Box)
        self.LB_data.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.LB_data)

        self.LB_undef_val = QLabel(self.verticalGroupBox_6)
        self.LB_undef_val.setObjectName(u"LB_undef_val")
        sizePolicy.setHeightForWidth(self.LB_undef_val.sizePolicy().hasHeightForWidth())
        self.LB_undef_val.setSizePolicy(sizePolicy)
        self.LB_undef_val.setMinimumSize(QSize(90, 20))
        self.LB_undef_val.setFrameShape(QFrame.Shape.Box)
        self.LB_undef_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.LB_undef_val)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CB_list_choose = QComboBox(self.verticalGroupBox_6)
        self.CB_list_choose.setObjectName(u"CB_list_choose")
        self.CB_list_choose.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.CB_list_choose)

        self.CB_data_choose = QComboBox(self.verticalGroupBox_6)
        self.CB_data_choose.setObjectName(u"CB_data_choose")
        self.CB_data_choose.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.CB_data_choose)

        self.SB_uv = QDoubleSpinBox(self.verticalGroupBox_6)
        self.SB_uv.setObjectName(u"SB_uv")
        self.SB_uv.setMaximumSize(QSize(16777215, 20))
        self.SB_uv.setMinimum(-1000.000000000000000)
        self.SB_uv.setMaximum(1000.000000000000000)
        self.SB_uv.setValue(-999.250000000000000)

        self.verticalLayout_2.addWidget(self.SB_uv)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_25.addLayout(self.horizontalLayout_5)

        self.PB_Import_Data = QPushButton(self.verticalGroupBox_6)
        self.PB_Import_Data.setObjectName(u"PB_Import_Data")
        self.PB_Import_Data.setMaximumSize(QSize(16777215, 23))

        self.verticalLayout_25.addWidget(self.PB_Import_Data)


        self.verticalLayout_8.addWidget(self.verticalGroupBox_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.verticalGroupBox_61 = QGroupBox(self.horizontalLayoutWidget_4)
        self.verticalGroupBox_61.setObjectName(u"verticalGroupBox_61")
        self.verticalGroupBox_61.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_27 = QVBoxLayout(self.verticalGroupBox_61)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_27.setContentsMargins(-1, 0, -1, -1)
        self.cb_use_normalization = QCheckBox(self.verticalGroupBox_61)
        self.cb_use_normalization.setObjectName(u"cb_use_normalization")
        self.cb_use_normalization.setMaximumSize(QSize(16777215, 19))

        self.verticalLayout_27.addWidget(self.cb_use_normalization)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.LB_MinNorm = QLabel(self.verticalGroupBox_61)
        self.LB_MinNorm.setObjectName(u"LB_MinNorm")
        sizePolicy.setHeightForWidth(self.LB_MinNorm.sizePolicy().hasHeightForWidth())
        self.LB_MinNorm.setSizePolicy(sizePolicy)
        self.LB_MinNorm.setMaximumSize(QSize(90, 20))
        self.LB_MinNorm.setFrameShape(QFrame.Shape.Box)
        self.LB_MinNorm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.LB_MinNorm)

        self.LB_MaxNorm = QLabel(self.verticalGroupBox_61)
        self.LB_MaxNorm.setObjectName(u"LB_MaxNorm")
        sizePolicy.setHeightForWidth(self.LB_MaxNorm.sizePolicy().hasHeightForWidth())
        self.LB_MaxNorm.setSizePolicy(sizePolicy)
        self.LB_MaxNorm.setMaximumSize(QSize(90, 20))
        self.LB_MaxNorm.setFrameShape(QFrame.Shape.Box)
        self.LB_MaxNorm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.LB_MaxNorm)


        self.horizontalLayout_15.addLayout(self.verticalLayout_22)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.SB_Min_Norm = QSpinBox(self.verticalGroupBox_61)
        self.SB_Min_Norm.setObjectName(u"SB_Min_Norm")
        self.SB_Min_Norm.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_20.addWidget(self.SB_Min_Norm)

        self.SB_Max_Norm = QSpinBox(self.verticalGroupBox_61)
        self.SB_Max_Norm.setObjectName(u"SB_Max_Norm")
        self.SB_Max_Norm.setMaximumSize(QSize(16777215, 20))
        self.SB_Max_Norm.setValue(0)

        self.verticalLayout_20.addWidget(self.SB_Max_Norm)


        self.horizontalLayout_15.addLayout(self.verticalLayout_20)


        self.verticalLayout_27.addLayout(self.horizontalLayout_15)


        self.verticalLayout_8.addWidget(self.verticalGroupBox_61)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalGroupBox_62 = QGroupBox(self.horizontalLayoutWidget_4)
        self.verticalGroupBox_62.setObjectName(u"verticalGroupBox_62")
        self.verticalGroupBox_62.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_28 = QVBoxLayout(self.verticalGroupBox_62)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_28.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.LB_MinZ = QLabel(self.verticalGroupBox_62)
        self.LB_MinZ.setObjectName(u"LB_MinZ")
        sizePolicy.setHeightForWidth(self.LB_MinZ.sizePolicy().hasHeightForWidth())
        self.LB_MinZ.setSizePolicy(sizePolicy)
        self.LB_MinZ.setMinimumSize(QSize(0, 0))
        self.LB_MinZ.setMaximumSize(QSize(90, 20))
        self.LB_MinZ.setFrameShape(QFrame.Shape.Box)
        self.LB_MinZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.LB_MinZ)

        self.LB_MaxZ = QLabel(self.verticalGroupBox_62)
        self.LB_MaxZ.setObjectName(u"LB_MaxZ")
        sizePolicy.setHeightForWidth(self.LB_MaxZ.sizePolicy().hasHeightForWidth())
        self.LB_MaxZ.setSizePolicy(sizePolicy)
        self.LB_MaxZ.setMinimumSize(QSize(0, 0))
        self.LB_MaxZ.setMaximumSize(QSize(90, 20))
        self.LB_MaxZ.setFrameShape(QFrame.Shape.Box)
        self.LB_MaxZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.LB_MaxZ)

        self.LB_Contrast = QLabel(self.verticalGroupBox_62)
        self.LB_Contrast.setObjectName(u"LB_Contrast")
        sizePolicy.setHeightForWidth(self.LB_Contrast.sizePolicy().hasHeightForWidth())
        self.LB_Contrast.setSizePolicy(sizePolicy)
        self.LB_Contrast.setMaximumSize(QSize(90, 20))
        self.LB_Contrast.setFrameShape(QFrame.Shape.Box)
        self.LB_Contrast.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.LB_Contrast)

        self.LB_Step = QLabel(self.verticalGroupBox_62)
        self.LB_Step.setObjectName(u"LB_Step")
        sizePolicy.setHeightForWidth(self.LB_Step.sizePolicy().hasHeightForWidth())
        self.LB_Step.setSizePolicy(sizePolicy)
        self.LB_Step.setMaximumSize(QSize(90, 20))
        self.LB_Step.setFrameShape(QFrame.Shape.Box)
        self.LB_Step.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.LB_Step)


        self.horizontalLayout_22.addLayout(self.verticalLayout_33)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.SB_Min_Z = QSpinBox(self.verticalGroupBox_62)
        self.SB_Min_Z.setObjectName(u"SB_Min_Z")
        self.SB_Min_Z.setMaximumSize(QSize(16777215, 20))
        self.SB_Min_Z.setMinimum(1)
        self.SB_Min_Z.setMaximum(100000)

        self.verticalLayout_32.addWidget(self.SB_Min_Z)

        self.SB_Max_Z = QSpinBox(self.verticalGroupBox_62)
        self.SB_Max_Z.setObjectName(u"SB_Max_Z")
        self.SB_Max_Z.setMaximumSize(QSize(16777215, 20))
        self.SB_Max_Z.setMinimum(1)
        self.SB_Max_Z.setMaximum(100000)
        self.SB_Max_Z.setValue(1)

        self.verticalLayout_32.addWidget(self.SB_Max_Z)

        self.SB_Contrast = QDoubleSpinBox(self.verticalGroupBox_62)
        self.SB_Contrast.setObjectName(u"SB_Contrast")
        self.SB_Contrast.setMaximumSize(QSize(16777215, 20))
        self.SB_Contrast.setDecimals(5)
        self.SB_Contrast.setSingleStep(0.010000000000000)
        self.SB_Contrast.setValue(1.000000000000000)

        self.verticalLayout_32.addWidget(self.SB_Contrast)

        self.SB_Step = QSpinBox(self.verticalGroupBox_62)
        self.SB_Step.setObjectName(u"SB_Step")
        self.SB_Step.setMaximumSize(QSize(16777215, 20))
        self.SB_Step.setMinimum(1)
        self.SB_Step.setMaximum(100000)
        self.SB_Step.setValue(5)

        self.verticalLayout_32.addWidget(self.SB_Step)


        self.horizontalLayout_22.addLayout(self.verticalLayout_32)


        self.verticalLayout_28.addLayout(self.horizontalLayout_22)

        self.PB_Calculate = QPushButton(self.verticalGroupBox_62)
        self.PB_Calculate.setObjectName(u"PB_Calculate")
        self.PB_Calculate.setMaximumSize(QSize(16777215, 23))

        self.verticalLayout_28.addWidget(self.PB_Calculate)

        self.PB_Clear_All = QPushButton(self.verticalGroupBox_62)
        self.PB_Clear_All.setObjectName(u"PB_Clear_All")
        self.PB_Clear_All.setMaximumSize(QSize(16777215, 23))

        self.verticalLayout_28.addWidget(self.PB_Clear_All)

        self.PB_Export = QPushButton(self.verticalGroupBox_62)
        self.PB_Export.setObjectName(u"PB_Export")
        self.PB_Export.setMaximumSize(QSize(16777215, 23))

        self.verticalLayout_28.addWidget(self.PB_Export)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.CheckBox_Remove_Step = QCheckBox(self.verticalGroupBox_62)
        self.CheckBox_Remove_Step.setObjectName(u"CheckBox_Remove_Step")
        self.CheckBox_Remove_Step.setMaximumSize(QSize(16777215, 19))

        self.horizontalLayout_7.addWidget(self.CheckBox_Remove_Step)

        self.CheckBox_Remove_Original = QCheckBox(self.verticalGroupBox_62)
        self.CheckBox_Remove_Original.setObjectName(u"CheckBox_Remove_Original")
        self.CheckBox_Remove_Original.setMaximumSize(QSize(16777215, 19))

        self.horizontalLayout_7.addWidget(self.CheckBox_Remove_Original)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)


        self.verticalLayout_28.addLayout(self.verticalLayout_11)


        self.verticalLayout_8.addWidget(self.verticalGroupBox_62)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.groupBox1 = QGroupBox(self.groupBox)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.LB_Min = QLabel(self.groupBox1)
        self.LB_Min.setObjectName(u"LB_Min")
        self.LB_Min.setFrameShape(QFrame.Shape.Box)
        self.LB_Min.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Min)

        self.LB_Max = QLabel(self.groupBox1)
        self.LB_Max.setObjectName(u"LB_Max")
        self.LB_Max.setFrameShape(QFrame.Shape.Box)
        self.LB_Max.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Max)

        self.LB_Mean = QLabel(self.groupBox1)
        self.LB_Mean.setObjectName(u"LB_Mean")
        self.LB_Mean.setFrameShape(QFrame.Shape.Box)
        self.LB_Mean.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Mean)

        self.LB_Std = QLabel(self.groupBox1)
        self.LB_Std.setObjectName(u"LB_Std")
        self.LB_Std.setFrameShape(QFrame.Shape.Box)
        self.LB_Std.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.LB_Std)


        self.horizontalLayout.addWidget(self.groupBox1)

        self.groupBox2 = QGroupBox(self.groupBox)
        self.groupBox2.setObjectName(u"groupBox2")
        self.groupBox2.setMinimumSize(QSize(66, 110))
        self.groupBox2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_step_min_val = QLabel(self.groupBox2)
        self.lb_step_min_val.setObjectName(u"lb_step_min_val")
        self.lb_step_min_val.setFrameShape(QFrame.Shape.Box)
        self.lb_step_min_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_step_min_val)

        self.lb_step_max_val = QLabel(self.groupBox2)
        self.lb_step_max_val.setObjectName(u"lb_step_max_val")
        self.lb_step_max_val.setFrameShape(QFrame.Shape.Box)
        self.lb_step_max_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_step_max_val)

        self.lb_step_mean_val = QLabel(self.groupBox2)
        self.lb_step_mean_val.setObjectName(u"lb_step_mean_val")
        self.lb_step_mean_val.setFrameShape(QFrame.Shape.Box)
        self.lb_step_mean_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_step_mean_val)

        self.lb_step_std_val = QLabel(self.groupBox2)
        self.lb_step_std_val.setObjectName(u"lb_step_std_val")
        self.lb_step_std_val.setFrameShape(QFrame.Shape.Box)
        self.lb_step_std_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_step_std_val)


        self.horizontalLayout.addWidget(self.groupBox2)

        self.verticalGroupBox_5 = QGroupBox(self.groupBox)
        self.verticalGroupBox_5.setObjectName(u"verticalGroupBox_5")
        self.verticalGroupBox_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_24 = QVBoxLayout(self.verticalGroupBox_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.lb_orig_min_val = QLabel(self.verticalGroupBox_5)
        self.lb_orig_min_val.setObjectName(u"lb_orig_min_val")
        self.lb_orig_min_val.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_24.addWidget(self.lb_orig_min_val)

        self.lb_orig_max_val = QLabel(self.verticalGroupBox_5)
        self.lb_orig_max_val.setObjectName(u"lb_orig_max_val")
        self.lb_orig_max_val.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_24.addWidget(self.lb_orig_max_val)

        self.lb_orig_mean_val = QLabel(self.verticalGroupBox_5)
        self.lb_orig_mean_val.setObjectName(u"lb_orig_mean_val")
        self.lb_orig_mean_val.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_24.addWidget(self.lb_orig_mean_val)

        self.lb_orig_std_val = QLabel(self.verticalGroupBox_5)
        self.lb_orig_std_val.setObjectName(u"lb_orig_std_val")
        self.lb_orig_std_val.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_24.addWidget(self.lb_orig_std_val)


        self.horizontalLayout.addWidget(self.verticalGroupBox_5)


        self.verticalLayout_7.addWidget(self.groupBox)


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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PracticePythonWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"data", None))
        self.PB_Choose_file.setText(QCoreApplication.translate("MainWindow", u"file", None))
        self.verticalGroupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"input", None))
        self.LB_list.setText(QCoreApplication.translate("MainWindow", u"list", None))
        self.LB_data.setText(QCoreApplication.translate("MainWindow", u"data", None))
        self.LB_undef_val.setText(QCoreApplication.translate("MainWindow", u"undefined value", None))
        self.CB_list_choose.setCurrentText("")
        self.PB_Import_Data.setText(QCoreApplication.translate("MainWindow", u"import", None))
        self.verticalGroupBox_61.setTitle(QCoreApplication.translate("MainWindow", u"normalization", None))
        self.cb_use_normalization.setText(QCoreApplication.translate("MainWindow", u"use normalization", None))
        self.LB_MinNorm.setText(QCoreApplication.translate("MainWindow", u"norm min", None))
        self.LB_MaxNorm.setText(QCoreApplication.translate("MainWindow", u"norm max", None))
        self.verticalGroupBox_62.setTitle(QCoreApplication.translate("MainWindow", u"graph settings", None))
        self.LB_MinZ.setText(QCoreApplication.translate("MainWindow", u"min z", None))
        self.LB_MaxZ.setText(QCoreApplication.translate("MainWindow", u"max z", None))
        self.LB_Contrast.setText(QCoreApplication.translate("MainWindow", u"contrast", None))
        self.LB_Step.setText(QCoreApplication.translate("MainWindow", u"step", None))
        self.PB_Calculate.setText(QCoreApplication.translate("MainWindow", u"calculate", None))
        self.PB_Clear_All.setText(QCoreApplication.translate("MainWindow", u"clear all", None))
        self.PB_Export.setText(QCoreApplication.translate("MainWindow", u"export", None))
        self.CheckBox_Remove_Step.setText(QCoreApplication.translate("MainWindow", u"remove step", None))
        self.CheckBox_Remove_Original.setText(QCoreApplication.translate("MainWindow", u"remove original", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"statistics", None))
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"values", None))
        self.LB_Min.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.LB_Max.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.LB_Mean.setText(QCoreApplication.translate("MainWindow", u"mean", None))
        self.LB_Std.setText(QCoreApplication.translate("MainWindow", u"std", None))
        self.groupBox2.setTitle(QCoreApplication.translate("MainWindow", u"step", None))
        self.lb_step_min_val.setText("")
        self.lb_step_max_val.setText("")
        self.lb_step_mean_val.setText("")
        self.lb_step_std_val.setText("")
        self.verticalGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"original", None))
        self.lb_orig_min_val.setText("")
        self.lb_orig_max_val.setText("")
        self.lb_orig_mean_val.setText("")
        self.lb_orig_std_val.setText("")
    # retranslateUi

