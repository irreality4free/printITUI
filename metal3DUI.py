# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metal3DUI1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1362, 784)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1331, 781))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(370, 80, 611, 301))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PORTlistWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.PORTlistWidget.setObjectName("PORTlistWidget")
        self.verticalLayout_3.addWidget(self.PORTlistWidget)
        self.RATE_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.RATE_comboBox.setObjectName("RATE_comboBox")
        self.RATE_comboBox.addItem("")
        self.RATE_comboBox.addItem("")
        self.RATE_comboBox.addItem("")
        self.RATE_comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.RATE_comboBox)
        self.REFRESHpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.REFRESHpushButton.setObjectName("REFRESHpushButton")
        self.verticalLayout_3.addWidget(self.REFRESHpushButton)
        self.CONNECTpushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.CONNECTpushButton.setObjectName("CONNECTpushButton")
        self.verticalLayout_3.addWidget(self.CONNECTpushButton)
        self.CONN_textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CONN_textBrowser.sizePolicy().hasHeightForWidth())
        self.CONN_textBrowser.setSizePolicy(sizePolicy)
        self.CONN_textBrowser.setMinimumSize(QtCore.QSize(0, 70))
        self.CONN_textBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        self.CONN_textBrowser.setObjectName("CONN_textBrowser")
        self.verticalLayout_3.addWidget(self.CONN_textBrowser)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 1432, 731))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.OPENFILE_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.OPENFILE_pushButton.setObjectName("OPENFILE_pushButton")
        self.verticalLayout.addWidget(self.OPENFILE_pushButton)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.b0001radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.b0001radioButton.setChecked(True)
        self.b0001radioButton.setObjectName("b0001radioButton")
        self.verticalLayout_9.addWidget(self.b0001radioButton)
        self.b001radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.b001radioButton.setObjectName("b001radioButton")
        self.verticalLayout_9.addWidget(self.b001radioButton)
        self.b1radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.b1radioButton.setObjectName("b1radioButton")
        self.verticalLayout_9.addWidget(self.b1radioButton)
        self.b10radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.b10radioButton.setObjectName("b10radioButton")
        self.verticalLayout_9.addWidget(self.b10radioButton)
        self.CONT_radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.CONT_radioButton.setObjectName("CONT_radioButton")
        self.verticalLayout_9.addWidget(self.CONT_radioButton)
        self.horizontalLayout_15.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.UP_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UP_pushButton.sizePolicy().hasHeightForWidth())
        self.UP_pushButton.setSizePolicy(sizePolicy)
        self.UP_pushButton.setAutoRepeat(True)
        self.UP_pushButton.setAutoRepeatDelay(500)
        self.UP_pushButton.setObjectName("UP_pushButton")
        self.verticalLayout_10.addWidget(self.UP_pushButton)
        self.DOWN_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DOWN_pushButton.sizePolicy().hasHeightForWidth())
        self.DOWN_pushButton.setSizePolicy(sizePolicy)
        self.DOWN_pushButton.setAutoRepeat(True)
        self.DOWN_pushButton.setAutoRepeatDelay(500)
        self.DOWN_pushButton.setObjectName("DOWN_pushButton")
        self.verticalLayout_10.addWidget(self.DOWN_pushButton)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.ALL_LAYERS_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ALL_LAYERS_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ALL_LAYERS_label.setObjectName("ALL_LAYERS_label")
        self.horizontalLayout_5.addWidget(self.ALL_LAYERS_label)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.CURRENT_LAYER_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.CURRENT_LAYER_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CURRENT_LAYER_label.setObjectName("CURRENT_LAYER_label")
        self.horizontalLayout_6.addWidget(self.CURRENT_LAYER_label)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.TIME_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TIME_label.sizePolicy().hasHeightForWidth())
        self.TIME_label.setSizePolicy(sizePolicy)
        self.TIME_label.setMinimumSize(QtCore.QSize(70, 0))
        self.TIME_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.TIME_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TIME_label.setObjectName("TIME_label")
        self.horizontalLayout_3.addWidget(self.TIME_label)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.TIME_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.TIME_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TIME_label_2.setObjectName("TIME_label_2")
        self.horizontalLayout_4.addWidget(self.TIME_label_2)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.LIFT_POS_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.LIFT_POS_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LIFT_POS_label.setObjectName("LIFT_POS_label")
        self.horizontalLayout_8.addWidget(self.LIFT_POS_label)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.ALL_LAYERS_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ALL_LAYERS_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ALL_LAYERS_label_2.setObjectName("ALL_LAYERS_label_2")
        self.horizontalLayout_14.addWidget(self.ALL_LAYERS_label_2)
        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_12.addWidget(self.pushButton_8)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_12.addWidget(self.spinBox_2)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_13.addWidget(self.pushButton_9)
        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_13.addWidget(self.spinBox_3)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 1)
        self.verticalLayout.setStretch(11, 1)
        self.verticalLayout.setStretch(12, 1)
        self.verticalLayout.setStretch(13, 1)
        self.verticalLayout.setStretch(14, 1)
        self.verticalLayout.setStretch(15, 1)
        self.verticalLayout.setStretch(16, 1)
        self.verticalLayout.setStretch(17, 1)
        self.horizontalLayout_11.addLayout(self.verticalLayout)
        self.verticalSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_11.addWidget(self.verticalSlider)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openGLWidget.sizePolicy().hasHeightForWidth())
        self.openGLWidget.setSizePolicy(sizePolicy)
        self.openGLWidget.setMinimumSize(QtCore.QSize(998, 0))
        self.openGLWidget.setMaximumSize(QtCore.QSize(600, 800))
        self.openGLWidget.setObjectName("openGLWidget")
        self.horizontalLayout_11.addWidget(self.openGLWidget)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11.setStretch(3, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 1081, 111))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(720, 130, 375, 351))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_4.addLayout(self.gridLayout_5)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(370, 130, 341, 351))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("дфдфд")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 490, 1091, 80))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.RB_HOME_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RB_HOME_pushButton.sizePolicy().hasHeightForWidth())
        self.RB_HOME_pushButton.setSizePolicy(sizePolicy)
        self.RB_HOME_pushButton.setObjectName("RB_HOME_pushButton")
        self.horizontalLayout_9.addWidget(self.RB_HOME_pushButton)
        self.RF_HOME_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RF_HOME_pushButton.sizePolicy().hasHeightForWidth())
        self.RF_HOME_pushButton.setSizePolicy(sizePolicy)
        self.RF_HOME_pushButton.setObjectName("RF_HOME_pushButton")
        self.horizontalLayout_9.addWidget(self.RF_HOME_pushButton)
        self.LT_HOME_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LT_HOME_pushButton.sizePolicy().hasHeightForWidth())
        self.LT_HOME_pushButton.setSizePolicy(sizePolicy)
        self.LT_HOME_pushButton.setObjectName("LT_HOME_pushButton")
        self.horizontalLayout_9.addWidget(self.LT_HOME_pushButton)
        self.LB_HOME_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_HOME_pushButton.sizePolicy().hasHeightForWidth())
        self.LB_HOME_pushButton.setSizePolicy(sizePolicy)
        self.LB_HOME_pushButton.setObjectName("LB_HOME_pushButton")
        self.horizontalLayout_9.addWidget(self.LB_HOME_pushButton)
        self.BUNKER1_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BUNKER1_pushButton.sizePolicy().hasHeightForWidth())
        self.BUNKER1_pushButton.setSizePolicy(sizePolicy)
        self.BUNKER1_pushButton.setCheckable(True)
        self.BUNKER1_pushButton.setObjectName("BUNKER1_pushButton")
        self.horizontalLayout_9.addWidget(self.BUNKER1_pushButton)
        self.BUNKER2_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BUNKER2_pushButton.sizePolicy().hasHeightForWidth())
        self.BUNKER2_pushButton.setSizePolicy(sizePolicy)
        self.BUNKER2_pushButton.setCheckable(True)
        self.BUNKER2_pushButton.setObjectName("BUNKER2_pushButton")
        self.horizontalLayout_9.addWidget(self.BUNKER2_pushButton)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(90, 590, 1251, 102))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_5)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.FLUSH_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.FLUSH_checkBox.setCheckable(True)
        self.FLUSH_checkBox.setChecked(True)
        self.FLUSH_checkBox.setObjectName("FLUSH_checkBox")
        self.verticalLayout_5.addWidget(self.FLUSH_checkBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(890, 10, 191, 241))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_7)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.verticalLayout_7.addWidget(self.lcdNumber_6)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_7)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.verticalLayout_7.addWidget(self.lcdNumber_7)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RATE_comboBox.setItemText(0, _translate("MainWindow", "9600"))
        self.RATE_comboBox.setItemText(1, _translate("MainWindow", "38400"))
        self.RATE_comboBox.setItemText(2, _translate("MainWindow", "57600"))
        self.RATE_comboBox.setItemText(3, _translate("MainWindow", "115200"))
        self.REFRESHpushButton.setText(_translate("MainWindow", "ОБНОВИТЬ"))
        self.CONNECTpushButton.setText(_translate("MainWindow", "ПОДКЛЮЧИТСЯ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ПОДКЛЮЧЕНИЕ"))
        self.pushButton_5.setText(_translate("MainWindow", "СТАРТ"))
        self.pushButton_4.setText(_translate("MainWindow", "СТОП"))
        self.pushButton_6.setText(_translate("MainWindow", "ПАУЗА"))
        self.pushButton_7.setText(_translate("MainWindow", "СТАРТ СО СЛОЯ"))
        self.OPENFILE_pushButton.setText(_translate("MainWindow", "ОТКРЫТЬ ФАЙЛ"))
        self.b0001radioButton.setText(_translate("MainWindow", "0.01mm"))
        self.b001radioButton.setText(_translate("MainWindow", "0.1mm"))
        self.b1radioButton.setText(_translate("MainWindow", "1.0mm"))
        self.b10radioButton.setText(_translate("MainWindow", "10.0mm"))
        self.CONT_radioButton.setText(_translate("MainWindow", "cont"))
        self.UP_pushButton.setText(_translate("MainWindow", "^"))
        self.DOWN_pushButton.setText(_translate("MainWindow", "v"))
        self.pushButton_11.setText(_translate("MainWindow", "СЛОЙ"))
        self.pushButton_12.setText(_translate("MainWindow", "РАКЕЛЬ"))
        self.pushButton_13.setText(_translate("MainWindow", "ПОРОШОК"))
        self.label_5.setText(_translate("MainWindow", "ВСЕГО СЛОЕВ:"))
        self.ALL_LAYERS_label.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "ТЕКУЩИЙ СЛОЙ:"))
        self.CURRENT_LAYER_label.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "ВРЕМЯ С НАЧАЛА ЦИКЛА:"))
        self.TIME_label.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "ВРЕМЯ ДО КОНЦА ПЕЧАТИ:"))
        self.TIME_label_2.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "ПОЗ ЛИФТА:"))
        self.LIFT_POS_label.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "КИСЛОРОД"))
        self.ALL_LAYERS_label_2.setText(_translate("MainWindow", "0"))
        self.pushButton_10.setText(_translate("MainWindow", "ПОРОШОК"))
        self.pushButton_8.setText(_translate("MainWindow", "СКОРОСТЬ"))
        self.pushButton_9.setText(_translate("MainWindow", "МОЩНОСТЬ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "УПРАВЛЕНИЕ"))
        self.pushButton_2.setText(_translate("MainWindow", "сканатор жарит"))
        self.pushButton.setText(_translate("MainWindow", "сканатор забивает"))
        self.pushButton_3.setText(_translate("MainWindow", "ракель жарит"))
        self.RB_HOME_pushButton.setText(_translate("MainWindow", "РАКЕЛЬ ДОМ ^"))
        self.RF_HOME_pushButton.setText(_translate("MainWindow", "РАКЕЛЬ ДОМ v"))
        self.LT_HOME_pushButton.setText(_translate("MainWindow", "ЛИФТ ДОМ ^"))
        self.LB_HOME_pushButton.setText(_translate("MainWindow", "ЛИФТ ДОМ v"))
        self.BUNKER1_pushButton.setText(_translate("MainWindow", "БУНКЕР 1"))
        self.BUNKER2_pushButton.setText(_translate("MainWindow", "БУНКЕР 2"))
        self.FLUSH_checkBox.setText(_translate("MainWindow", "ОЧИЩАТЬ КОНСОЛЬ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TEMP"))
        self.label_7.setText(_translate("MainWindow", "ПРОСМАТРИВАЕМЫЙ СЛОЙ"))
        self.label_8.setText(_translate("MainWindow", "ВСЕГО СЛОЕВ:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "СЛОИ"))

