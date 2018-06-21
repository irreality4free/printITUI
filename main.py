import sys
from metal3DUI import *
from PyQt5 import QtWidgets
from time import sleep
import serial
from serial_test import serial_ports
import threading
from PyQt5.QtCore import QTimer, QRunnable, QThreadPool

SCALE = [3200,1600,1600,1600]



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

        self.move_step = 0.01

        # Здесь прописываем событие нажатия на кнопку
        self.ui.REFRESHpushButton.clicked.connect(self.Refresh)
        self.ui.CONNECTpushButton.clicked.connect(self.Connect)

        self.ui.RB_HOME_pushButton.clicked.connect(self.RB_HOME)
        self.ui.RF_HOME_pushButton.clicked.connect(self.RF_HOME)
        self.ui.LT_HOME_pushButton.clicked.connect(self.LT_HOME)
        self.ui.LB_HOME_pushButton.clicked.connect(self.LB_HOME)

        self.ui.UP_pushButton.clicked.connect(self.UP)
        self.ui.DOWN_pushButton.clicked.connect(self.DOWN)
        self.ui.LEFT_pushButton.clicked.connect(self.LEFT)
        self.ui.RIGHT_pushButton.clicked.connect(self.RIGHT)



        self.RAK_SENSE_BACK = '30'
        self.RAK_SENSE_FRONT = '31'
        self.LIFT_SENSE_BOT = '32'
        self.LIFT_SENSE_TOP = '33'

        self.RAK_STEP = '1'
        self.LIFT_STEP = '2'
        self.BUNK1_STEP ='3'
        self.BUNK2_STEP ='4'

        self.answ_msg=''



        self.ui.b0001radioButton.clicked.connect(self.b001)
        self.ui.b001radioButton.clicked.connect(self.b01)
        self.ui.b1radioButton.clicked.connect(self.b1)
        self.ui.b10radioButton.clicked.connect(self.b10)


        self.ui.BUNKER1_checkBox.stateChanged.connect(self.BUNK1)
        self.ui.BUNKER2_checkBox.stateChanged.connect(self.BUNK2)

        self.clInfoTimer = QTimer()
        self.clInfoTimer.timeout.connect(self.InfoClear)

        self.serTimer = QTimer()
        # self.serTimer.timeout.connect(self.UpdateInfo)
        self.serTimer.timeout.connect(self.SerialRead)

        # self.threadpool = QThreadPool()
        # print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def InfoClear(self):
        self.ui.textBrowser.clear()
        self.clInfoTimer.stop()

    def StartSelfCl(self):
        self.clInfoTimer.start(5000)

    def DebugUI(self,msg):
        self.ui.textBrowser.setText(self.ui.textBrowser.toPlainText() + msg + '\n')
        self.StartSelfCl()


    def Refresh(self):

        self.ui.PORTlistWidget.clear()

        com_list = serial_ports()

        for key in com_list:
            self.ui.PORTlistWidget.addItem(key)

    def Connect(self):
        if (len(self.ui.RATElistWidget.selectedItems()) > 0):
            port = self.ui.PORTlistWidget.selectedItems()[0].text()
            rate = self.ui.RATElistWidget.selectedItems()[0].text()
            try:

                self.ser = serial.Serial(port, rate)
                print('connected')

                # self.SerialRead()
                # self.threadpool.start(self.SerialRead)
                self.serTimer.start(100)
            except Exception as e:
                print(e)
                print('connection exeption')

    # @threaded
    def SerialRead(self):
        while self.ser.inWaiting():
                msg = str(self.ser.readline())
                msg = msg.replace("b'", '')
                msg = msg.replace("\\r\\n", '')
                msg = msg.replace("'", '')
                print(msg)
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
        self.ser.write('c02:1:{}\n'.format(int(self.move_step*float(SCALE[0]))).encode('utf-8'))
    def DOWN(self):
        self.ser.write('c02:1:{}\n'.format(int(-self.move_step * float(SCALE[0]))).encode('utf-8'))
    def LEFT(self):
        self.ser.write('c02:2:{}\n'.format(int(self.move_step * float(SCALE[0]))).encode('utf-8'))
    def RIGHT(self):
        self.ser.write('c02:2:{}\n'.format(int(-self.move_step * float(SCALE[0]))).encode('utf-8'))



    def RB_HOME(self):
        self.ser.write('c01:1:1000:30\n'.encode('utf-8'))
    def RF_HOME(self):
        self.ser.write('com:9\n'.encode('utf-8'))
    def LT_HOME(self):
        self.ser.write('com:1\n'.encode('utf-8'))
    def LB_HOME(self):
        self.ser.write('com:1\n'.encode('utf-8'))

    def BUNK1(self):
        if self.ui.BUNKER1_checkBox.isChecked():
            self.ser.write('com:1\n'.encode('utf-8'))
        else:
            self.ser.write('com:2\n'.encode('utf-8'))

    def BUNK2(self):
        if self.ui.BUNKER1_checkBox.isChecked():
            self.ser.write('com:7\n'.encode('utf-8'))
        else:
            self.ser.write('com:8\n'.encode('utf-8'))



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



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())