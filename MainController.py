from PyQt5.QtWidgets import QMainWindow, QPushButton, QTabWidget, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)

        self.firstLabButton = self.findChild(QPushButton, 'FirstLabButton')
        self.theoryFirstLabButton = self.findChild(QPushButton, 'TheoryFirstLabButton')
        self.exampleFirstLabButton = self.findChild(QPushButton, 'ExampleFirstLabButton')
        self.tab_widget = self.findChild(QTabWidget, 'tabWidget')
        self.firstLabTab = self.findChild(QWidget, 'FirstLabTab')
        self.theoryFirstLabTab = self.findChild(QWidget, 'TheoryFirstLabTab')
        self.exampleFirstLabTab = self.findChild(QWidget, 'ExampleFirstLabTab')

        self.web_view = QWebEngineView(self.theoryFirstLabTab)
        self.web_view.setGeometry(210, 110, 1100, 650)

        page = self.web_view.page()
        page.setBackgroundColor(Qt.transparent)

        self.buttonTabMap = {
            self.firstLabButton: (self.firstLabTab, "Лабораторная работа №1"),
            self.theoryFirstLabButton: (self.theoryFirstLabTab, "Теория"),
            self.exampleFirstLabButton: (self.exampleFirstLabTab, "Пример")
        }
        for button, (tab, label) in self.buttonTabMap.items():
            button.clicked.connect(lambda checked, _tab=tab, _label=label: self.open_tab(_tab, _label))

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

    def open_tab(self, tab, label):
        index = self.tab_widget.indexOf(tab)
        if index == -1:
            index = self.tab_widget.addTab(tab, label)
        self.tab_widget.setCurrentIndex(index)

    def on_tab_changed(self, index):
        self.close_tabs_after(index)
        if index == 2:
            self.load_html_from_file()

    def load_html_from_file(self):
        with open('Lab1.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
            self.web_view.setHtml(html_content)
