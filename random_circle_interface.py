from PyQt5.QtWidgets import QWidget, QPushButton


class My_interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 600, 600)
        self.setWindowTitle('Пятая программа')

        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(self.btn.sizeHint())

