import sys
from metal3DUI import *
from PyQt5 import QtWidgets
from time import sleep
import serial
from serial_test import serial_ports
import threading
from PyQt5.QtCore import QTimer, QRunnable, QThreadPool
import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon

SCALE = [3200,3200,3200,3200]##rak lift bunk1 bunk2





def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):





        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Здесь прописываем событие нажатия на кнопку
        self.ui.REFRESHpushButton.clicked.connect(self.Refresh)
        self.ui.CONNECTpushButton.clicked.connect(self.Connect)

        self.ui.RB_HOME_pushButton.clicked.connect(self.RB_HOME)
        self.ui.RF_HOME_pushButton.clicked.connect(self.RF_HOME)
        self.ui.LT_HOME_pushButton.clicked.connect(self.LT_HOME)
        self.ui.LB_HOME_pushButton.clicked.connect(self.LB_HOME)

        self.ui.UP_pushButton.clicked.connect(self.UP)
        self.ui.DOWN_pushButton.clicked.connect(self.DOWN)

        self.ui.b0001radioButton.clicked.connect(self.b001)
        self.ui.b001radioButton.clicked.connect(self.b01)
        self.ui.b1radioButton.clicked.connect(self.b1)
        self.ui.b10radioButton.clicked.connect(self.b10)

        self.ui.FLUSH_checkBox.stateChanged.connect(self.FLUSH)

        self.clInfoTimer = QTimer()
        self.clInfoTimer.timeout.connect(self.InfoClear)

        self.serTimer = QTimer()
        # self.serTimer.timeout.connect(self.UpdateInfo)
        self.serTimer.timeout.connect(self.SerialRead)

        self.ui.openFile = QAction(QIcon('open.png'), 'Open', self)
        self.ui.openFile.setShortcut('Ctrl+O')
        self.ui.openFile.setStatusTip('Open new File')
        self.ui.OPENFILE_pushButton.clicked.connect(self.showDialog)

        self.ui.menubar = self.menuBar()
        self.ui.fileMenu = self.ui.menubar.addMenu('&File')
        self.ui.fileMenu.addAction(self.ui.openFile)


        self.move_step = 0.01
        self.RAK_SENSE_BACK = '30'
        self.RAK_SENSE_FRONT = '31'
        self.LIFT_SENSE_BOT = '32'
        self.LIFT_SENSE_TOP = '33'

        self.RAK_STEP = '1'
        self.LIFT_STEP = '2'
        self.BUNK1_STEP ='3'
        self.BUNK2_STEP ='4'

        self.flush = True

        self.answ_msg=''

        self.lift_down = 0.01 * SCALE[1]*5
        self.time_from_start = 0

        self.bunk_doze = 10 * SCALE[0]
        self.current_layer = 0
        self.layer_list=[]

    def showDialog(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]


        # f =

            with open(fname, 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

        except Exception as e:
            print(e)

    def InfoClear(self):
        self.ui.textBrowser.clear()
        self.ui.CONN_textBrowser.clear()
        self.clInfoTimer.stop()

    def StartSelfCl(self):
        self.clInfoTimer.start(5000)

    def DebugUI(self,msg):
        self.ui.textBrowser.setText(msg +  '\n' +self.ui.textBrowser.toPlainText())
        self.ui.CONN_textBrowser.setText(msg +  '\n' +self.ui.CONN_textBrowser.toPlainText())
        if self.flush:
            self.StartSelfCl()

    def Refresh(self):

        self.ui.PORTlistWidget.clear()

        com_list = serial_ports()

        for key in com_list:
            self.ui.PORTlistWidget.addItem(key)

    def Connect(self):
        if (len(self.ui.PORTlistWidget.selectedItems()) > 0):
            # if (len(self.ui.RATElistWidget.selectedItems()) > 0):
            port = self.ui.PORTlistWidget.selectedItems()[0].text()
            rate = int(self.ui.RATE_comboBox.currentText())
            try:

                self.ser = serial.Serial(port, rate)
                self.DebugUI('connected')

                # self.SerialRead()
                # self.threadpool.start(self.SerialRead)
                self.serTimer.start(100)
            except Exception as e:
                print(e)
                print('connection exeption')

            # else:
            #     self.DebugUI('choose RATE first')
        else:
            self.DebugUI('choose PORT first')

    def SerialRead(self):
        while self.ser.inWaiting():
                msg = str(self.ser.readline())
                msg = msg.replace("b'", '')
                msg = msg.replace("\\r\\n", '')
                msg = msg.replace("'", '')
                # print(msg)
                self.answ_msg = msg
                # self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText()+msg+'\n')
                self.DebugUI(msg)
                # msg = msg.split(':')

    def UpdateInfo(self):
        # print('check')
        if len(self.answ_msg)>0:
            self.DebugUI(self.answ_msg)
            self.answ_msg = ""

    def UP(self):
        self.move_stepper( '1', int(self.move_step*float(SCALE[0])))

    def DOWN(self):
        self.move_stepper( '1', int(-self.move_step * float(SCALE[0])))

    def RB_HOME(self):
        self.move_stepper_sw('1','1000',self.RAK_SENSE_BACK)

    def RF_HOME(self):
        self.move_stepper_sw('1', '-1000', self.RAK_SENSE_FRONT)

    def LT_HOME(self):
        self.move_stepper_sw('2', '1000', self.LIFT_SENSE_TOP)

    def LB_HOME(self):
        self.move_stepper_sw('2', '-1000', self.LIFT_SENSE_BOT)

    def move_stepper(self, motor_num, steps):
        try:
            self.ser.write('c02:{}:{}\n'.format( motor_num, steps).encode('utf-8'))
        except AttributeError as e:
            print(e)
            self.DebugUI('НЕТ СОЕДИНЕНИЯ')

    def move_stepper_sw(self, motor_num, steps, endstop_pin):
        try:
            self.ser.write('c01:{}:{}:{}\n'.format(motor_num,steps,endstop_pin).encode('utf-8'))
        except AttributeError as e:
            print (e)
            self.DebugUI('НЕТ СОЕДИНЕНИЯ')

    def FLUSH(self):
        if self.ui.FLUSH_checkBox.isChecked():
            self.flush = True
        else:
            self.flush = False

    def b001(self):
        self.move_step = 0.01
        print(self.move_step)

    def b01(self):
        self.move_step = 0.1
        print(self.move_step)

    def b1(self):
        self.move_step = 1.0
        print(self.move_step)

    def b10(self):
        self.move_step = 10.0
        print(self.move_step)

    def LiftDown(self):
        self.move_stepper('1', int(self.move_step * float(SCALE[0])))

    def LoadScan(self,current_layer):



        self.ui.ALL_LAYERS_label.setText(str(len(self.layer_list)))

    def LoadMaterial(self):
        self.move_stepper('3',int(self.bunk_doze))

    def StartScan(self):
        pass

    def StartFromLayer(self,layer_num):
        self.layer_list = self.layer_list[layer_num:]
        self.RUN()

    def RUN(self):
        for layer_num, layer in enumerate(self.layer_list):
            self.LiftDown()
            self.LoadScan(self.layer_list)
            self.LoadMaterial()
            self.RB_HOME()
            self.StartScan()
            self.current_layer = layer_num









if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    with open("lar.qss", "r") as fh:
        myapp.setStyleSheet(fh.read())
    myapp.show()
    sys.exit(app.exec_())