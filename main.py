import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QTextBrowser
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)

        self.firstLabButton = self.findChild(QPushButton, 'FirstLabButton')
        self.theoryFirstLabButton = self.findChild(QPushButton, 'TheoryFirstLabButton')
        self.tab_widget = self.findChild(QTabWidget, 'tabWidget')
        self.firstLabTab = self.findChild(QWidget, 'FirstLabTab')
        self.theoryFirstLabTab = self.findChild(QWidget, 'TheoryFirstLabTab')

        self.text_browser = self.findChild(QTextBrowser, 'textBrowser_3')

        self.firstLabButton.clicked.connect(self.open_tab)
        self.theoryFirstLabButton.clicked.connect(self.open_theory)
        self.close_other_tabs()
        self.tab_widget.currentChanged.connect(self.on_tab_changed)

    def close_other_tabs(self):
        num_tabs = self.tab_widget.count()
        for i in range(num_tabs - 1, 0, -1):
            self.tab_widget.removeTab(i)

    def close_tabs_after(self, index):
        num_tabs = self.tab_widget.count()
        for i in range(num_tabs - 1, index, -1):
            self.tab_widget.removeTab(i)

    def open_tab(self):
        self.tab_widget.insertTab(1, self.firstLabTab, "Лабораторная работа №1")
        self.tab_widget.setCurrentIndex(1)

    def open_theory(self):
        self.tab_widget.insertTab(2, self.theoryFirstLabTab, "Теория")
        self.tab_widget.setCurrentIndex(2)

    def open_main_tab(self):
        self.close_other_tabs()
        self.tab_widget.setCurrentIndex(0)

    def on_tab_changed(self, index):
        self.close_tabs_after(index)
        if index == 2:
            self.load_html_from_file()

    def load_html_from_file(self):
        with open('Lab1.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
            self.text_browser.setHtml(html_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())