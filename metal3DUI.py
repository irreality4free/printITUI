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
        MainWindow.resize(1362, 796)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1361, 781))
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1325, 731))
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
        self.START_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.START_pushButton.sizePolicy().hasHeightForWidth())
        self.START_pushButton.setSizePolicy(sizePolicy)
        self.START_pushButton.setObjectName("START_pushButton")
        self.verticalLayout.addWidget(self.START_pushButton)
        self.STOP_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.STOP_pushButton.sizePolicy().hasHeightForWidth())
        self.STOP_pushButton.setSizePolicy(sizePolicy)
        self.STOP_pushButton.setObjectName("STOP_pushButton")
        self.verticalLayout.addWidget(self.STOP_pushButton)
        self.PAUSE_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PAUSE_pushButton.sizePolicy().hasHeightForWidth())
        self.PAUSE_pushButton.setSizePolicy(sizePolicy)
        self.PAUSE_pushButton.setCheckable(True)
        self.PAUSE_pushButton.setObjectName("PAUSE_pushButton")
        self.verticalLayout.addWidget(self.PAUSE_pushButton)
        self.START_FR_L_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.START_FR_L_pushButton.sizePolicy().hasHeightForWidth())
        self.START_FR_L_pushButton.setSizePolicy(sizePolicy)
        self.START_FR_L_pushButton.setObjectName("START_FR_L_pushButton")
        self.verticalLayout.addWidget(self.START_FR_L_pushButton)
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
        self.LAYER_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LAYER_pushButton.setObjectName("LAYER_pushButton")
        self.verticalLayout.addWidget(self.LAYER_pushButton)
        self.RAK_HOME_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.RAK_HOME_pushButton.setObjectName("RAK_HOME_pushButton")
        self.verticalLayout.addWidget(self.RAK_HOME_pushButton)
        self.POWDER_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.POWDER_pushButton.setObjectName("POWDER_pushButton")
        self.verticalLayout.addWidget(self.POWDER_pushButton)
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
        self.END_TIME_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.END_TIME_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.END_TIME_label.setObjectName("END_TIME_label")
        self.horizontalLayout_4.addWidget(self.END_TIME_label)
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
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.POWDER_DOZE_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.POWDER_DOZE_spinBox.setObjectName("POWDER_DOZE_spinBox")
        self.horizontalLayout_2.addWidget(self.POWDER_DOZE_spinBox)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.SPEED_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.SPEED_spinBox.setObjectName("SPEED_spinBox")
        self.horizontalLayout_12.addWidget(self.SPEED_spinBox)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_13.addWidget(self.label_7)
        self.POWER_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.POWER_spinBox.setObjectName("POWER_spinBox")
        self.horizontalLayout_13.addWidget(self.POWER_spinBox)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_7.addWidget(self.verticalSlider)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openGLWidget.sizePolicy().hasHeightForWidth())
        self.openGLWidget.setSizePolicy(sizePolicy)
        self.openGLWidget.setMinimumSize(QtCore.QSize(998, 0))
        self.openGLWidget.setMaximumSize(QtCore.QSize(600, 800))
        self.openGLWidget.setObjectName("openGLWidget")
        self.horizontalLayout_7.addWidget(self.openGLWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.FLUSH_checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.FLUSH_checkBox.setCheckable(True)
        self.FLUSH_checkBox.setChecked(True)
        self.FLUSH_checkBox.setObjectName("FLUSH_checkBox")
        self.verticalLayout_2.addWidget(self.FLUSH_checkBox)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_4, "")
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
        self.START_pushButton.setText(_translate("MainWindow", "СТАРТ"))
        self.STOP_pushButton.setText(_translate("MainWindow", "СТОП"))
        self.PAUSE_pushButton.setText(_translate("MainWindow", "ПАУЗА"))
        self.START_FR_L_pushButton.setText(_translate("MainWindow", "СТАРТ СО СЛОЯ"))
        self.OPENFILE_pushButton.setText(_translate("MainWindow", "ОТКРЫТЬ ФАЙЛ"))
        self.b0001radioButton.setText(_translate("MainWindow", "0.01mm"))
        self.b001radioButton.setText(_translate("MainWindow", "0.1mm"))
        self.b1radioButton.setText(_translate("MainWindow", "1.0mm"))
        self.b10radioButton.setText(_translate("MainWindow", "10.0mm"))
        self.CONT_radioButton.setText(_translate("MainWindow", ">>>"))
        self.UP_pushButton.setText(_translate("MainWindow", "^"))
        self.DOWN_pushButton.setText(_translate("MainWindow", "v"))
        self.LAYER_pushButton.setText(_translate("MainWindow", "СЛОЙ"))
        self.RAK_HOME_pushButton.setText(_translate("MainWindow", "РАКЕЛЬ"))
        self.POWDER_pushButton.setText(_translate("MainWindow", "ПОРОШОК"))
        self.label_5.setText(_translate("MainWindow", "ВСЕГО СЛОЕВ:"))
        self.ALL_LAYERS_label.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "ТЕКУЩИЙ СЛОЙ:"))
        self.CURRENT_LAYER_label.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "ВРЕМЯ С НАЧАЛА ЦИКЛА:"))
        self.TIME_label.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "ВРЕМЯ ДО КОНЦА ПЕЧАТИ:"))
        self.END_TIME_label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "ПОЗ ЛИФТА:"))
        self.LIFT_POS_label.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "КИСЛОРОД"))
        self.ALL_LAYERS_label_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "ДОЗА"))
        self.label_4.setText(_translate("MainWindow", "СКОРОСТЬ"))
        self.label_7.setText(_translate("MainWindow", "КИСЛОРОД"))
        self.FLUSH_checkBox.setText(_translate("MainWindow", "ОЧИЩАТЬ КОНСОЛЬ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "УПРАВЛЕНИЕ"))

