import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QLineEdit , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtGui import * 

class app_2(QWidget):

    def __init__(self):
        super().__init__()
        self.ui()
     
    def ui(self):
        self.setGeometry(10 , 10 , 234 , 338)
        self.setWindowTitle("Simple calculator")
        self.setStyleSheet("background-color:#384147;color:white")
        button1 = QPushButton('1' , self)
        button2 = QPushButton('2' , self)
        button3 = QPushButton('3' , self)
        button4 = QPushButton('4' , self)
        button5 = QPushButton('5' , self)
        button6 = QPushButton('6' , self)
        button7 = QPushButton('7' , self)
        button8 = QPushButton('8' , self)
        button9 = QPushButton('9' , self)
        button0 = QPushButton('0' , self)
        buttonplus = QPushButton('+' , self)
        buttonminus = QPushButton('-' , self)
        buttonx = QPushButton('x' , self)
        button_ = QPushButton('/' , self)
        buttonresult = QPushButton('=' , self)
        buttondot = QPushButton("." , self)
        buttonclear = QPushButton("C" , self)
        button1.resize(55 , 55)
        button2.resize(55 , 55)
        button3.resize(55 , 55)
        button4.resize(55 , 55)
        button5.resize(55 , 55)
        button6.resize(55 , 55)
        button7.resize(55 , 55)
        button8.resize(55 , 55)
        button9.resize(55 , 55)
        button0.resize(55 , 55)
        buttonplus.resize(55 , 55)
        buttonx.resize(55 , 55)
        button_.resize(55 , 55)
        buttonresult.resize(55 , 55)
        buttondot.resize(55 , 55)
        buttonclear.resize(55 , 55)
        buttonminus.resize(55 , 55)
        self.textbox1 = QLineEdit(self)
        self.textbox1.resize(220 , 55)
        self.textbox1.setStyleSheet("font-size:25px;background-color:white;color:black")
        self.textbox1.move(7,1)
        button1.clicked.connect(lambda:self.add_text('1'))
        button2.clicked.connect(lambda:self.add_text('2'))
        button3.clicked.connect(lambda:self.add_text('3'))
        button4.clicked.connect(lambda:self.add_text('4'))
        button5.clicked.connect(lambda:self.add_text('5'))
        button6.clicked.connect(lambda:self.add_text('6'))
        button7.clicked.connect(lambda:self.add_text('7'))
        button8.clicked.connect(lambda:self.add_text('8'))
        button9.clicked.connect(lambda:self.add_text('9'))
        button0.clicked.connect(lambda:self.add_text('0'))
        buttonplus.clicked.connect(lambda:self.add_text('+'))
        buttonminus.clicked.connect(lambda:self.add_text('-'))
        buttonx.clicked.connect(lambda:self.add_text('*'))
        button_.clicked.connect(lambda:self.add_text('/'))
        buttondot.clicked.connect(lambda:self.add_text('.'))
        buttonclear.clicked.connect(self.clear)
        buttonresult.clicked.connect(self.result)
        x = 7
        y = 55
        button1.move(x , y)
        x += 55
        button2.move(x, y)
        x += 55
        button3.move(x , y)
        x += 55
        button4.move(x , y)
        x = 7
        y += 55
        button5.move(x , y)
        x += 55
        button6.move(x , y)
        x += 55
        button7.move(x , y)
        x += 55
        button8.move(x , y)
        x = 7
        y += 55
        button9.move(x , y)
        x += 55
        button0.move(x , y)
        x += 55
        buttonplus.move(x , y)
        x += 55
        buttonminus.move(x , y)
        x = 7
        y += 55
        buttonx.move(x , y)
        x += 55
        button_.move(x , y)
        x += 55
        buttondot.move(x , y)
        x += 55
        buttonresult.move(x , y)
        x = 7
        y += 55
        buttonclear.move(x , y)

    def add_text(self , x):
        text = self.textbox1.text()
        self.textbox1.setText(str(text) + str(x))

    def clear(self):
        self.textbox1.setText("")

    def result(self):
        text = self.textbox1.text()
        result = 0
        try:
            result = eval(text)
        except ZeroDivisionError:
            result = 0
        self.textbox1.setText(str(result))

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
        label1 = QLabel("First number : " , self)
        label1.setStyleSheet("font-family:'Arial';")
        label1.resize(100 , 30)
        label2 = QLabel("Second number : " , self)
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
        
class main_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple calculator")
        self.setStyleSheet("background-color:#384147;color:white")
        self.setGeometry(10 , 10 , 250 , 150)
        self.button1 = QPushButton("Basic mode" , self)
        self.button1.resize(200 , 50)
        self.button2 = QPushButton("Advanced mode" , self)
        self.button2.resize(200 , 50)
        self.button1.move(10 , 10)
        self.button2.move(10 , 60)
        self.button1.clicked.connect(lambda:self.show1(1))
        self.button2.clicked.connect(lambda:self.show1(2))

    def show1(self , x):
        if x == 1:
            ex = App()
            ex.show()
        elif x == 2:
            ex = app_2()
            ex.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_menu()
    ex.show()
    sys.exit(app.exec_())