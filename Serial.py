import serial
from PyQt5.QtCore import QTimer, QRunnable, QThreadPool


class Serial(QRunnable):

    def run(self):
        '''
        Your code goes in this function
        '''
        print("Thread start")

        print("Thread complete")