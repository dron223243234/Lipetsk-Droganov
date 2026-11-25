import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(["ID", "Сорт", "Обжарка", "Помол", "Вкус", "Цена", "Объём"])
        self.tableView.setModel(self.model)
        self.pushButton.clicked.connect(self.load_coffee)
        self.pushButton.setText('Обновление')
        self.load_coffee()


    def load_coffee(self):
        db = sqlite3.connect('coffee.sqlite')
        rows = db.execute('''
            SELECT id, variety, roast, grind, taste, price, package_grams
            FROM coffee ORDER BY id
        ''').fetchall()
        db.close()

        self.model.removeRows(0, self.model.rowCount())
        for row in rows:
            self.model.appendRow([QStandardItem(str(value)) for value in row])

        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())