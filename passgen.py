import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup, QPushButton, QGroupBox,
QHBoxLayout, QVBoxLayout, QTextEdit, QLineEdit, QLabel, QMessageBox, QRadioButton, QCheckBox, QSystemTrayIcon, QMenu)
from PyQt5.QtGui import QIntValidator, QIcon, QPixmap
import random
import ctypes

let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'l',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb = ['%', '*', '-', '_', '@', '?', '#', '$', '~']


def gen():
    pas = []
    if numbers.isChecked():
        pas.extend(num)
    if letters.isChecked():
        pas.extend(let)
    if lettersl.isChecked():
        pas.extend(letl)
    if symbols.isChecked():
        pas.extend(symb)
    if numbers.isChecked() == False and letters.isChecked() == False\
            and lettersl.isChecked() == False and symbols.isChecked() == False:
        error = QMessageBox()
        error.setWindowTitle('Ошибка')
        error.setText('Опции не выбраны')
        error.exec_()
    if length.text() == '':
        error = QMessageBox()
        error.setWindowTitle('Ошибка')
        error.setText('Введите длину пароля')
        error.exec_()
    else:
        pswrd = ''
        for i in range(int(length.text())):
            pswrd += random.choice(pas)
        password.setText(pswrd)


# Создание окна
app = QApplication([])
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('очень уникальная строка')
app.setWindowIcon(QIcon('C:\\Users\\miron\\Documents\\Twwan\\Programming\\passgen\\key.png')) #
app.setStyle('Fusion')
main_win = QWidget()
main_win.setWindowIcon(QIcon('C:\\Users\\miron\\Documents\\Twwan\\Programming\\passgen\\key.png')) #
main_win.setFixedSize(400, 350)
main_win.setWindowTitle('Генератор паролей')

#
start = QPushButton('Сгенерировать')
password = QTextEdit()

tip = QLabel()
tip.setFixedWidth(15)
pic = QPixmap('C:\\Users\\miron\\Documents\\Twwan\\Programming\\passgen\\info.png')
tip.setGeometry(10, 10, 300, 300)
tip.setPixmap(pic)


tip.setToolTip('Каким считается хороший пароль? \n'
               '- Длиной от 8 символов и выше. \n'
               '- Имеющий большие и маленькие буквы. \n'
               '- Содержащий в себе цифры. \n'
               '- Имеющий хотя бы один спец. символ: $%#@. \n'
               '- Желательно без повторяющихся символов.')
# Выбор опций
numbers = QCheckBox('Цифры (0 - 9)')
letters = QCheckBox('Прописные буквы (ABC)')
lettersl = QCheckBox('Строчные буквы (abc)')
symbols = QCheckBox('Спец. символы (%*-_?#$@~)')
length = QLineEdit()
validator = QIntValidator(1, 100)
length.setValidator(validator)
length.setFixedWidth(50)
length.setPlaceholderText('Длина')


# Создание layout
layout_main = QVBoxLayout()
layoutH = QHBoxLayout()
layoutHbutton = QHBoxLayout()
layoutVopt = QVBoxLayout()
layoutHoptions = QHBoxLayout()
layoutHoptions2 = QHBoxLayout()

options = QGroupBox()
options.setTitle('Выберите опции:')

options.setLayout(layoutVopt)


main_win.setLayout(layout_main)
layout_main.addLayout(layoutH)
layout_main.addWidget(options, alignment=Qt.AlignCenter)
layout_main.addLayout(layoutHbutton)
layout_main.addWidget(password, alignment=Qt.AlignCenter)
layout_main.addWidget(tip)
#
# layoutH.addWidget(welcome, alignment=Qt.AlignCenter)
layoutHbutton.addWidget(start, alignment=Qt.AlignCenter)
#
layoutVopt.addLayout(layoutHoptions)
layoutVopt.addLayout(layoutHoptions2)
layoutHoptions.addWidget(letters, alignment=Qt.AlignCenter)
layoutHoptions.addWidget(lettersl, alignment=Qt.AlignCenter)
layoutHoptions2.addWidget(numbers, alignment=Qt.AlignCenter)
layoutHoptions2.addWidget(symbols, alignment=Qt.AlignCenter)
layoutVopt.addWidget(length, alignment=Qt.AlignCenter)


main_win.setLayout(layout_main)

start.clicked.connect(gen)

main_win.show()
app.exec_()
