import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint

from random_circle_interface import My_interface


class MyWidget(QMainWindow, My_interface):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.flag = False
        self.btn.clicked.connect(self.onClicked)

    def onClicked(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        first_color = randint(0, 255)
        second_color = randint(0, 255)
        third_color = randint(0, 255)
        color = QColor(first_color, second_color, third_color)
        pen = QPen(color, 4)
        qp.setPen(pen)
        x_coor = randint(40, 400)
        y_coor = randint(40, 400)
        diameter = randint(5, 400)
        qp.drawEllipse(x_coor, y_coor, diameter, diameter)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
