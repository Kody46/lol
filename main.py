from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Испытай удачу, друг!')
main_win.resize(700,700)
button1 = QPushButton('Нажми')
button2 = QPushButton('Нажми')
button3 = QPushButton('Нажми')
button4 = QPushButton('Нажми')
button5 = QPushButton('Нажми')
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
v_line = QVBoxLayout()
h_line1.addWidget(button2,alignment = Qt.AlignLeft) 
h_line1.addWidget(button3,alignment = Qt.AlignRight) 

h_line2.addWidget(button1,alignment = Qt.AlignCenter) 

h_line3.addWidget(button4,alignment =  Qt.AlignLeft) 
h_line3.addWidget(button5,alignment = Qt.AlignRight)
main_win.setLayout(v_line)
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

def friend():
    number = randint(0,6)
    button1.setText(str(number))
button1.clicked.connect(friend)
button2.clicked.connect(friend)
button3.clicked.connect(friend)
button4.clicked.connect(friend)
button5.clicked.connect(friend)
main_win.show()
app.exec_()