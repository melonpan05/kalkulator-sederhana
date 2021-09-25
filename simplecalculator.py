import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QLineEdit , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtGui import * 
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Simple calculator'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:#384147;color:white")
        label1 = QLabel("Angka pertama" , self)
        label1.setStyleSheet("font-family:'Arial';")
        label1.resize(100 , 30)
        label2 = QLabel("Angka kedua" , self)
        label2.resize(100 , 30)
        self.result = QLineEdit(self)
        self.result.resize(100,30)
        button1 = QPushButton('+', self)
        button1.resize(30,30)
        button2 = QPushButton('-', self)
        button2.resize(30,30)
        button3 = QPushButton('x' , self)
        button3.resize(30,30)
        button4 = QPushButton('/' , self)
        button4.resize(30,30)
        button1.clicked.connect(lambda :self.on_click('+'))
        button2.clicked.connect(lambda :self.on_click('-'))
        button3.clicked.connect(lambda :self.on_click('*'))
        button4.clicked.connect(lambda :self.on_click('/'))
        self.first_number = QLineEdit(self)
        self.first_number.resize(100 , 30)
        self.second_number = QLineEdit(self)
        self.second_number.resize(100 , 30)
        label1.move(0 , 1)
        self.first_number.move(101 , 1)
        label2.move(0,31)
        self.second_number.move(101,31)
        button1.move(0,62)
        button2.move(31 , 62)
        button3.move(61 , 62)
        button4.move(92 , 62)
        self.result.move(0,93)

        

        
        self.show()

    @pyqtSlot()
    def on_click(self , operation):
        number_1 = float(self.first_number.text())
        number_2 = float(self.second_number.text())
        result = str(number_1) + str(operation) + str(number_2)
        result = eval(result)
        self.result.setText(str(result))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())