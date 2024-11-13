from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QPushButton, QTabWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)

        self.firstLabButton = self.findChild(QPushButton, 'FirstLabButton')
        self.theoryFirstLabButton = self.findChild(QPushButton, 'TheoryFirstLabButton')
        self.exampleFirstLabButton = self.findChild(QPushButton, 'ExampleFirstLabButton')
        self.variantsFirstLabButton = self.findChild(QPushButton, 'VariantsFirstLabButton')
        self.tab_widget = self.findChild(QTabWidget, 'tabWidget')
        self.firstLabTab = self.findChild(QWidget, 'FirstLabTab')
        self.theoryFirstLabTab = self.findChild(QWidget, 'TheoryFirstLabTab')
        self.exampleFirstLabTab = self.findChild(QWidget, 'ExampleFirstLabTab')
        self.variantsFirstLabTab = self.findChild(QWidget, 'VariantsFirstLabTab')
        self.taskFirstLabTab = self.findChild(QWidget, 'TaskFirstLabTab')

        self.web_views = {
            self.theoryFirstLabTab: QWebEngineView(self.theoryFirstLabTab),
            self.exampleFirstLabTab: QWebEngineView(self.exampleFirstLabTab),
            self.taskFirstLabTab: QWebEngineView(self.taskFirstLabTab)
        }

        self.load_html_from_file("Lab1.html", self.theoryFirstLabTab)

        for web_view in self.web_views.values():
            web_view.setGeometry(210, 110, 1100, 650)
            page = web_view.page()
            page.setBackgroundColor(Qt.transparent)

        self.buttonTabMap = {
            self.firstLabButton: (self.firstLabTab, "Лабораторная работа №1"),
            self.theoryFirstLabButton: (self.theoryFirstLabTab, "Теория"),
            self.exampleFirstLabButton: (self.exampleFirstLabTab, "Пример"),
            self.variantsFirstLabButton: (self.variantsFirstLabTab, "Задачи")
        }

        for i in range(1, 9):
            label = self.findChild(QLabel, f"label{i}")
            label.setAttribute(Qt.WA_TransparentForMouseEvents)

        for button, (tab, label) in self.buttonTabMap.items():
            button.clicked.connect(lambda checked, _tab=tab, _label=label: self.open_tab(_tab, _label))

        self.close_other_tabs()
        self.tab_widget.currentChanged.connect(self.on_tab_changed)

        self.create_buttons_in_variants_tab()

    def close_other_tabs(self):
        num_tabs = self.tab_widget.count()
        for i in range(num_tabs - 1, 0, -1):
            self.tab_widget.removeTab(i)

    def close_tabs_after(self, index):
        num_tabs = self.tab_widget.count()
        for i in range(num_tabs - 1, index, -1):
            self.tab_widget.removeTab(i)

    def create_arrow_tab(self):
        arrow_tab = QWidget()
        layout = QVBoxLayout(arrow_tab)
        arrow_label = QLabel("→", arrow_tab)
        arrow_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(arrow_label)
        return arrow_tab

    def open_tab(self, tab, label):
        index = self.tab_widget.indexOf(tab)
        if index == -1:
            arrow_tab = self.create_arrow_tab()
            arrow_index = self.tab_widget.addTab(arrow_tab, "→")
            self.tab_widget.setTabEnabled(arrow_index, False)
            index = self.tab_widget.addTab(tab, label)
        self.tab_widget.setCurrentIndex(index)

    def on_tab_changed(self, index):
        self.close_tabs_after(index)

    def load_html_from_file(self, file_path, tab):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            self.web_views[tab].setHtml(html_content)

    def create_buttons_in_variants_tab(self):
        scroll_area = QScrollArea(self.variantsFirstLabTab)
        scroll_area.setWidgetResizable(True)
        qss = load_stylesheet("css_style\\scroll.qss")
        scroll_area.setStyleSheet(qss)
        scroll_area_widget = QWidget()
        layout = QGridLayout(scroll_area_widget)
        layout.setHorizontalSpacing(53)
        layout.setVerticalSpacing(48)

        for i in range(30):
            btn = QPushButton("", scroll_area_widget)

            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)
            shadow.setOffset(0, 0)
            shadow.setColor(QColor(0, 0, 0, 50))
            btn.setGraphicsEffect(shadow)

            label_number = QLabel(f"{i + 1}", scroll_area_widget)
            label_text = QLabel("Вариант", scroll_area_widget)

            font_number = QFont("Century Gothic", 40)
            label_number.setFont(font_number)

            font_text = QFont("Century Gothic", 16)
            label_text.setFont(font_text)

            if i + 1 >= 10:
                label_number.setContentsMargins(0, 0, 10, 0)
                label_number.setFixedWidth(75)
            else:
                label_number.setContentsMargins(17, 0, 0, 0)
                label_number.setFixedWidth(65)

            label_text.setFixedWidth(110)
            label_text.setContentsMargins(0, 0, 7, 0)

            h_layout = QHBoxLayout()
            h_layout.addWidget(label_number)
            h_layout.addWidget(label_text)
            h_layout.setSpacing(0)

            btn.setLayout(h_layout)
            btn.setFixedSize(200, 90)
            btn.setStyleSheet("""
                background-color: white;
                border-radius: 30px;
            """)
            btn.clicked.connect(lambda checked, index=i + 1: self.button_action(index))

            row = i // 5
            col = i % 5
            layout.addWidget(btn, row, col)

        scroll_area.setWidget(scroll_area_widget)

        container_widget = QWidget(self.variantsFirstLabTab)
        container_widget.setStyleSheet("background: transparent;")
        container_widget.setLayout(QVBoxLayout())
        container_widget.layout().addWidget(scroll_area)
        container_widget.resize(1267, 700)
        container_widget.move(87, 60)

    def button_action(self, index):
        self.open_tab(self.taskFirstLabTab, f"Вариант №{index}")
        file_path = f"FirstLabVariants\\Variant{index}.html"
        self.load_html_from_file(file_path, self.taskFirstLabTab)

def load_stylesheet(self):
    with open(self, 'r') as f:
        return f.read()
