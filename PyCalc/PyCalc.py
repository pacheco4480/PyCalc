
import sys
import numpy as np

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QGridLayout, QWidget, QLabel, QAction, qApp, QSizePolicy, QToolButton, QMenu
from PyQt5.QtGui import QFont, QPalette, QColor, QKeyEvent, QIcon
from PyQt5.QtCore import Qt



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_number = ''
        self.result = 0
        self.operator = ''

    def initUI(self):
        # Cria um widget para conter os botões
        widget = QWidget(self)

        # Cria um layout grid para organizar os botões
        layout = QGridLayout(widget)
        layout.setSpacing(5)  # Define o espaçamento desejado entre os botões


        ########## Toolbar

        exitAct = QAction(QIcon('cancel.png'), 'Sair', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        otherMenu = QMenu(self)
        otherMenu.addAction('Padrão')
        otherMenu.addAction('Cientifica')
        otherMenu.addAction('Representação gráfica')
        otherMenu.addAction('Programador')
        otherMenu.addAction('Cálculo de data')

        otherButton = QToolButton(self)
        otherButton.setIcon(QIcon('menu.png'))
        otherButton.setPopupMode(QToolButton.InstantPopup)
        otherButton.setMenu(otherMenu)

        self.toolbar = self.addToolBar('')


        self.toolbar.addWidget(otherButton)

        spacer_right = QWidget(self)
        spacer_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer_right)
        self.toolbar.addAction(exitAct)



        # Define as cores do Toolbar
        cor_texto_padrao = "#FFFFFF"  
        cor_texto_hover = "#FFFFFF"  

        # Aplica o estilo ao menu
        otherMenu.setStyleSheet("QMenu::item { color: %s; }"
                                "QMenu::item:selected { background-color: #454343; color: %s; }"
                                "QMenu::item:pressed { background-color: #302f2f; color: %s; }"
                                % (cor_texto_padrao, cor_texto_hover, cor_texto_hover))



        
        ########## LCD
        
        self.lcd = QLabel("0")  # Cria um QLabel para exibir os resultados
        self.lcd.setFixedSize(253, 60)  # Define o tamanho do visor
        self.lcd.setFont(QFont('Arial', 26))
        self.lcd.setAlignment(Qt.AlignRight)  # Alinha o texto à direita
        layout.addWidget(self.lcd, 0, 0, 1, 4)  # Adiciona o visor no layout
        self.lcd.setStyleSheet("background-color: #302f2f; color: #ffffff")

        ##########



        #1º fila
        btn1 = QPushButton("%")
        btn1.setFixedSize(60, 40)
        btn1.setFont(QFont('Arial', 12))
        btn1.clicked.connect(lambda: self.handle_operation('%'))
        layout.addWidget(btn1, 1, 0)  # adiciona o botão na primeira linha, primeira coluna

        btn2 = QPushButton("CE")
        btn2.setFixedSize(60, 40)
        btn2.setFont(QFont('Arial', 12))
        btn2.clicked.connect(self.clear_entry)
        layout.addWidget(btn2, 1, 1)

        btn3 = QPushButton("C")
        btn3.setFixedSize(60, 40)
        btn3.setFont(QFont('Arial', 12))
        btn3.clicked.connect(self.clear_all)
        layout.addWidget(btn3, 1, 2)

        btn4 = QPushButton("")
        btn4.setIcon(QIcon('clear.png'))
        btn4.setFixedSize(60, 40)
        btn4.clicked.connect(self.clear_last)
        layout.addWidget(btn4, 1, 3)

        #2º fila
        btn5 = QPushButton("1/x")
        btn5.setFixedSize(60, 40)
        btn5.setFont(QFont('Arial', 12))
        btn5.clicked.connect(self.inverse)
        layout.addWidget(btn5, 2, 0)

        btn6 = QPushButton("x²")
        btn6.setFixedSize(60, 40)
        btn6.setFont(QFont('Arial', 12))
        btn6.clicked.connect(self.square)
        layout.addWidget(btn6, 2, 1)

        btn7 = QPushButton("√x")
        btn7.setFixedSize(60, 40)
        btn7.setFont(QFont('Arial', 12))
        btn7.clicked.connect(self.square_root)
        layout.addWidget(btn7, 2, 2)

        btn8 = QPushButton("÷")
        btn8.setFixedSize(60, 40)
        btn8.setFont(QFont('Arial', 12))
        btn8.clicked.connect(lambda: self.handle_operation('/'))
        layout.addWidget(btn8, 2, 3)

        #3º fila
        btn9 = QPushButton("7")
        btn9.setFixedSize(60, 40)
        btn9.setFont(QFont('Arial', 12))
        btn9.clicked.connect(lambda: self.handle_number('7'))
        layout.addWidget(btn9, 3, 0)

        btn10 = QPushButton("8")
        btn10.setFixedSize(60, 40)
        btn10.setFont(QFont('Arial', 12))
        btn10.clicked.connect(lambda: self.handle_number('8'))
        layout.addWidget(btn10, 3, 1)

        btn11 = QPushButton("9")
        btn11.setFixedSize(60, 40)
        btn11.setFont(QFont('Arial', 12))
        btn11.clicked.connect(lambda: self.handle_number('9'))
        layout.addWidget(btn11, 3, 2)

        btn12 = QPushButton("×")
        btn12.setFixedSize(60, 40)
        btn12.setFont(QFont('Arial', 12))
        btn12.clicked.connect(lambda: self.handle_operation('*'))
        layout.addWidget(btn12, 3, 3)

        #4º fila
        btn13 = QPushButton("4")
        btn13.setFixedSize(60, 40)
        btn13.setFont(QFont('Arial', 12))
        btn13.clicked.connect(lambda: self.handle_number('4'))
        layout.addWidget(btn13, 4, 0)

        btn14 = QPushButton("5")
        btn14.setFixedSize(60, 40)
        btn14.setFont(QFont('Arial', 12))
        btn14.clicked.connect(lambda: self.handle_number('5'))
        layout.addWidget(btn14, 4, 1)

        btn15 = QPushButton("6")
        btn15.setFixedSize(60, 40)
        btn15.setFont(QFont('Arial', 12))
        btn15.clicked.connect(lambda: self.handle_number('6'))
        layout.addWidget(btn15, 4, 2)

        btn16 = QPushButton("-")
        btn16.setFixedSize(60, 40)
        btn16.setFont(QFont('Arial', 12))
        btn16.clicked.connect(lambda: self.handle_operation('-'))
        layout.addWidget(btn16, 4, 3)

        #5º fila
        btn17 = QPushButton("1")
        btn17.setFixedSize(60, 40)
        btn17.setFont(QFont('Arial', 12))
        btn17.clicked.connect(lambda: self.handle_number('1'))
        layout.addWidget(btn17, 5, 0)

        btn18 = QPushButton("2")
        btn18.setFixedSize(60, 40)
        btn18.setFont(QFont('Arial', 12))
        btn18.clicked.connect(lambda: self.handle_number('2'))
        layout.addWidget(btn18, 5, 1)

        btn19 = QPushButton("3")
        btn19.setFixedSize(60, 40)
        btn19.setFont(QFont('Arial', 12))
        btn19.clicked.connect(lambda: self.handle_number('3'))
        layout.addWidget(btn19, 5, 2)

        btn20 = QPushButton("+")
        btn20.setFixedSize(60, 40)
        btn20.setFont(QFont('Arial', 12))
        btn20.clicked.connect(lambda: self.handle_operation('+'))
        layout.addWidget(btn20, 5, 3)

        #6º fila
        btn21 = QPushButton("+/-")
        btn21.setFixedSize(60, 40)
        btn21.setFont(QFont('Arial', 12))
        btn21.clicked.connect(self.toggle_sign)
        layout.addWidget(btn21, 6, 0)

        btn22 = QPushButton("0")
        btn22.setFixedSize(60, 40)
        btn22.setFont(QFont('Arial', 12))
        btn22.clicked.connect(lambda: self.handle_number('0'))
        layout.addWidget(btn22, 6, 1)

        btn23 = QPushButton(".")
        btn23.setFixedSize(60, 40)
        btn23.setFont(QFont('Arial', 12))
        btn23.clicked.connect(self.add_decimal_point)
        layout.addWidget(btn23, 6, 2)

        btn24 = QPushButton("=")
        btn24.setFixedSize(60, 40)
        btn24.setFont(QFont('Arial', 12))
        btn24.clicked.connect(self.calculate_result)
        layout.addWidget(btn24, 6, 3)




        # Modifica a cor de fundo do layout
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(28, 28, 27))
        widget.setAutoFillBackground(True)
        widget.setPalette(palette)
        

        # Modifica a cor de fundo e a cor do texto dos botões
        btn1.setStyleSheet ("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")       
        btn2.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        btn3.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        btn4.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        btn5.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        btn6.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        btn7.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        btn8.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")        
        btn9.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn10.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn11.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")        
        btn12.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")        
        btn13.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn14.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn15.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")        
        btn16.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")        
        btn17.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn18.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn19.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")        
        btn20.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        btn21.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn22.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn23.setStyleSheet("QPushButton { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:hover { background-color: #302f2f; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #454343; color: #ffffff; }")
        btn24.setStyleSheet("QPushButton { background-color: #454343; color: #ffffff; }"
                   "QPushButton:hover { background-color: #454343; color: #ffffff; }"
                   "QPushButton:!hover { background-color: #302f2f; color: #ffffff; }")
        



        # Altera a cor de fundo da janela (barra de título e borda)
        self.setStyleSheet("background-color: #1c1b1b;")




        widget.setLayout(layout)

        # Define o widget como o centralWidget da QMainWindow
        self.setCentralWidget(widget)

        self.setGeometry(800, 300, 100, 400)
        self.setWindowTitle('Calculadora')
        self.show()

###################################### Teclado

        
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_0:
            self.handle_number('0')
        elif key == Qt.Key_1:
            self.handle_number('1')
        elif key == Qt.Key_2:
            self.handle_number('2')
        elif key == Qt.Key_3:
            self.handle_number('3')
        elif key == Qt.Key_4:
            self.handle_number('4')
        elif key == Qt.Key_5:
            self.handle_number('5')
        elif key == Qt.Key_6:
            self.handle_number('6')
        elif key == Qt.Key_7:
            self.handle_number('7')
        elif key == Qt.Key_8:
            self.handle_number('8')
        elif key == Qt.Key_9:
            self.handle_number('9')
        elif key == Qt.Key_Plus:
            self.handle_operation('+')
        elif key == Qt.Key_Minus:
            self.handle_operation('-')
        elif key == Qt.Key_Asterisk:
            self.handle_operation('*')
        elif key == Qt.Key_Slash:
            self.handle_operation('/')
        elif key == Qt.Key_Percent:
            self.handle_operation('%')
        elif key == Qt.Key_Backspace:
            self.clear_last()
        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            self.calculate_result()
        elif key == Qt.Key_Escape:
            self.clear_all()




###################################### Operaçoes


    def handle_number(self, number):
        self.current_number += number
        self.update_lcd()

    def handle_operation(self, operator):
        self.operator = operator
        self.result = np.float64(self.current_number)
        self.current_number = ''
        self.update_lcd()

    def calculate_result(self):
        if self.operator == '+':
            self.result += np.float64(self.current_number)
        elif self.operator == '-':
            self.result -= np.float64(self.current_number)
        elif self.operator == '*':
            self.result *= np.float64(self.current_number)
        elif self.operator == '/':
            self.result /= np.float64(self.current_number)
        elif self.operator == '%':
            self.result %= np.float64(self.current_number)

        self.current_number = str(self.result)
        self.update_lcd()

    def clear_entry(self):
        self.current_number = ''
        self.update_lcd()

    def clear_all(self):
        self.current_number = ''
        self.result = 0
        self.operator = ''
        self.update_lcd()

    def clear_last(self):
        if self.current_number:
            self.current_number = self.current_number[:-1]
            self.update_lcd()

    def inverse(self):
        if self.current_number:
            self.current_number = str(1 / np.float64(self.current_number))
            self.update_lcd()

    def square(self):
        if self.current_number:
            self.current_number = str(np.float64(self.current_number) ** 2)
            self.update_lcd()

    def square_root(self):
        if self.current_number:
            self.current_number = str(np.sqrt(np.float64(self.current_number)))
            self.update_lcd()

    def toggle_sign(self):
        if self.current_number:
            self.current_number = str(-np.float64(self.current_number))
            self.update_lcd()

    def add_decimal_point(self):
        if '.' not in self.current_number:
            self.current_number += '.'
            self.update_lcd()

    def update_lcd(self):
        self.lcd.setText(self.current_number)


###################################### 


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
