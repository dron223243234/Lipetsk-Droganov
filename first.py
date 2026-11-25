from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
import random
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.show_circle = False
        self.pushButton = QPushButton('кнопка', self)
        self.pushButton.move(30, 30)
        self.pushButton.clicked.connect(self.famous)

    def famous(self):
        self.show_circle = True
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.show_circle:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(f'#{random.randint(10000000, 99999999)}'))
        x = random.randint(200, 1000)
        painter.drawEllipse(30, 70, x, x)
        painter.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
