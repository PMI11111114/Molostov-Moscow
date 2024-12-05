import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QPoint


class CircleButton(QPushButton):
    def __init__(self):
        super().__init__("Создать окружность")
        self.clicked.connect(self.create_circle)

    def create_circle(self):
        self.parent().circles.append(
            {
                "x": random.randint(20, self.parent().width() - 20),
                "y": random.randint(20, self.parent().height() - 20),
                "size": random.randint(10, 50),
                "color": self.get_random_color(),
            }
        )
        self.parent().update()

    def get_random_color(self):
        return QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.circles = []
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.button = CircleButton()
        self.layout.addWidget(self.button)

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            pen = QPen(circle["color"], 2)
            painter.setPen(pen)
            painter.drawEllipse(
                QPoint(circle["x"], circle["y"]), circle["size"], circle["size"]
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())