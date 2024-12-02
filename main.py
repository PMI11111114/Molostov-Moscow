import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import QPoint
from PyQt6 import uic
from random import randint

form_class = uic.loadUiType('SqPyLMS.ui')[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.pushButton.clicked.connect(self.create_circle)

    def create_circle(self):
        self.x = self.width() // 2
        self.y = self.height() // 2
        self.circles.append(QPoint(self.x, self.y))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(255, 255, 0), 2)
        painter.setPen(pen)
        for circle in self.circles:
            a = randint(1, 100)
            painter.drawEllipse(circle, a, a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
