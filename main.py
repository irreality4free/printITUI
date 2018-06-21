import sys
from metal3DUI import *
from PyQt5 import QtWidgets
from time import sleep
import serial
from serial_test import serial_ports
import threading



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


        self.ui.b0001radioButton.clicked.connect(self.b001)
        self.ui.b001radioButton.clicked.connect(self.b01)
        self.ui.b1radioButton.clicked.connect(self.b1)
        self.ui.b10radioButton.clicked.connect(self.b10)


        self.ui.BUNKER1_checkBox.stateChanged.connect(self.BUNK1)
        self.ui.BUNKER2_checkBox.stateChanged.connect(self.BUNK2)


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

                self.SerialRead()
                # self.upTimer.start(2000)

            except Exception as e:
                print(e)
                print('connection exeption')

    @threaded
    def SerialRead(self):
        while True:
            if self.ser.inWaiting():
                msg = str(self.ser.readline())
                msg = msg.replace("b'", '')
                msg = msg.replace("\\r\\n", '')
                msg = msg.replace("'", '')
                print(msg)
                # self.ui.textBrowser.setText(msg)

                # msg = msg.split(':')

    def RB_HOME(self):
        self.ser.write('com:1\n'.encode('utf-8'))
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
    def b01(self):
        self.move_step = 0.1
    def b1(self):
        self.move_step = 1.0
    def b10(self):
        self.move_step = 10.0



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())