import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)

        self.button = self.findChild(QPushButton, 'FirstLabButton')
        self.tab_widget = self.findChild(QTabWidget, 'tabWidget')
        self.firstLabTab = self.findChild(QWidget, 'FirstLabTab')

        self.button.clicked.connect(self.open_tab)
        self.close_other_tabs()
        self.tab_widget.currentChanged.connect(self.on_tab_changed)

    def close_other_tabs(self):
        num_tabs = self.tab_widget.count()

        for i in range(1, num_tabs):
            self.tab_widget.removeTab(i)

    def open_tab(self):
        self.tab_widget.insertTab(1, self.firstLabTab, "Лабораторная работа №1")
        self.tab_widget.setCurrentIndex(1)

    def open_main_tab(self):
        # Открываем главную вкладку и закрываем все остальные
        self.close_other_tabs()
        self.tab_widget.setCurrentIndex(0)  # Переходим на главную вкладку (индекс 0)

    def on_tab_changed(self, index):
        # Если активируется главная вкладка (индекс 0), закрываем все остальные
        if index == 0:
            self.close_other_tabs()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
