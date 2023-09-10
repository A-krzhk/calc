import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor
from cmath import sqrt as sqrt_c
from math import sqrt



MISTAKE = ["ОШИБКА", 'ERROR', 'ERROR', '错误']
LANG_NUM = 1
ERROR_STATUS = False
DEGREE = 2

class LangForm(QWidget):
    global MISTAKE
    global ERROR_STATUS
    global DEGREE
    global LANG_NUM
    global mistake_text
    def __init__(self):
        super(LangForm, self).__init__()
        uic.loadUi('draw_form_saved3.ui', self)
        self.setWindowTitle('Калькулятор')
        self.label_2.setText('Введите число:')
        self.rus_button.clicked.connect(self.rus_form)
        self.eng_button.clicked.connect(self.eng_form)
        self.esp_button.clicked.connect(self.esp_form)
        self.chinese_button.clicked.connect(self.chinese_form)
        self.get_result.clicked.connect(self.print_result)
        self.padding.setStyleSheet('background-color: rgb(199, 187, 255);border-radius: 20px;')
        self.rus_button.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.eng_button.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.esp_button.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.chinese_button.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.k_dots.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.k_dots2.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.degree_box.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.line.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.output_line.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.get_result.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.padding_complex.setStyleSheet('background-color: rgb(221, 218, 232);border-radius: 20px;')
        self.textBrowser.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.padding3.setStyleSheet('background-color: rgb(205,205,215)')
        self.textBrowser.setStyleSheet('background-color: rgb(220,220,225)')
        
        self.real_line.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.img_line.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.get_result_complex.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.output_complex.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 6px;')
        self.get_result_complex.clicked.connect(self.get_complex_result)
        
    
    def get_complex_result(self):
        try:
            real = self.real_line.text()
            try:
                real = real.replace(',', '.')
            except Exception:
                pass
            img = self.img_line.text()
            try:
                img = img.replace(',', '.')
            except Exception:
                pass
            try:
                img = img.replace('+', '')
            except Exception:
                pass
            s = ((float(real) + float(float(img))*1j))
            print(s)
            result = (sqrt_c(s))
            print(result.real, result.imag)
            round_num = self.k_dots2.value()
            if float(str(result.imag)) >= 0:
                result_complex = '± (' + str(round(result.real, round_num)) + ' + ' + str(round(result.imag, round_num)) + 'i)'
            else:
                result_complex = '± (' + str(round(result.real, round_num)) + str(round(result.imag, round_num)) + 'i)'
            print('=')
            self.output_complex.setText(str(result_complex))
        except Exception:
            self.output_complex.setText('ОШИБКА/ERROR')

        
    def rus_form(self):
        self.label.setText('Выберите язык:')
        self.label_2.setText('Введите число:')
        #self.get_result.setText('Вычислить')
        self.dots_num_label.setText('Цифр после запятой:')
        self.dots_num_label2.setText('Цифр после запятой:')
        self.result_label.setText('Результат:')
        self.choose_degree_label.setText('Выберите степень:')
        self.contact_label_2.setText('Контакты:')
        self.complex_label.setText('Квадратный корень из комплексного числа:')
        LANG_NUM = 1
        
    def eng_form(self):
        self.label.setText('Choose your language:')
        self.label_2.setText('Enter the number:')
        #self.get_result.setText('Calculate')
        self.dots_num_label.setText('Numbers after dot:')
        self.dots_num_label2.setText('Numbers after dot:')
        self.result_label.setText('Result:')
        self.choose_degree_label.setText('Select degree:')
        self.contact_label_2.setText('Contacts:')
        self.complex_label.setText('Square root of a complex number:')
        LANG_NUM = 2
        
    def esp_form(self):
        self.label.setText('Elige tu idioma:')
        self.label_2.setText('Introduce el número:')
        #self.get_result.setText('Calcular')
        self.dots_num_label.setText('Números después del punto:')
        self.dots_num_label2.setText('Números después del punto:')
        self.result_label.setText('Resultado:')
        self.choose_degree_label.setText('Seleccionar grado:')
        self.contact_label_2.setText('Contactos:')
        self.complex_label.setText('Raíz cuadrada de un número complejo:')
        LANG_NUM = 3
        
    def chinese_form(self):
        self.label.setText('选择你的语言:')
        self.label_2.setText('输入号码:')
        #self.get_result.setText('计算')
        self.dots_num_label.setText('小数点后的数字:')
        self.dots_num_label2.setText('小数点后的数字:')
        self.result_label.setText('结果:')
        self.choose_degree_label.setText('选择学位:')
        self.contact_label_2.setText('联系人:')
        self.complex_label.setText('复数的平方根:')
        LANG_NUM = 4
        
    def print_result(self):
        DEGREE = self.degree_box.value()
        try:
            text = self.line.text()
            try:
                text = text.replace(',', '.')
            except Exception:
                1 == 1
            text = float(text)
            if float(text) > 0:
                if self.k_dots.value() == int(self.k_dots.value()):
                    output = str(round(float(text) ** (1 / DEGREE), self.k_dots.value()))
            else:
                output = str(float(text) ** (1 / DEGREE)).split('+')[1][0:-2]
                output = str(round(float(output), self.k_dots.value())) + 'i'

            self.output_line.setText(str(output))
            ERROR_STATUS = False
        except Exception:
            self.output_line.setText('ОШИБКА/ERROR')
            ERROR_STATUS = True

            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LangForm()
    form.show()
    form.setWindowFlags(form.windowFlags())
    form.setFixedSize(form.size())
    sys.exit(app.exec())
