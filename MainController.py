import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QScrollArea, QPushButton, QTabWidget, QWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QGridLayout, QFrame, QGroupBox, QSizePolicy, QSpacerItem
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl
from PyQt5 import uic
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.setMinimumSize(1440, 810)

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

        self.load_html_from_file("Documentation/FirstLab/FirstLabTheory.html", self.theoryFirstLabTab)


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

        shadow_buttons = [self.FirstLabWidget, self.SecondLabWidget, self.ThirdLabWidget, self.FourthLabWidget,
                       self.theoryFirstLabButton, self.exampleFirstLabButton, self.variantsFirstLabButton]
        for button in shadow_buttons:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setOffset(0, 0)
            shadow.setColor(QColor(0, 0, 0, 50))
            button.setGraphicsEffect(shadow)

        shadow_frame = [self.TheoryFrame, self.TaskFrame]
        for frame in shadow_frame:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)
            shadow.setOffset(0, 0)
            shadow.setColor(QColor(0, 0, 0, 50))
            frame.setGraphicsEffect(shadow)

        for i in range(1, 9):
            label = self.findChild(QLabel, f"label{i}")
            label.setAttribute(Qt.WA_TransparentForMouseEvents)

        for button, (tab, label) in self.buttonTabMap.items():
            button.clicked.connect(lambda checked, _tab=tab, _label=label: self.open_tab(_tab, _label))

        self.close_other_tabs()
        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        self.create_buttons_in_variants_tab()
        self.create_accordion(self.exampleFirstLabTab)

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

    def load_html_from_file(self, file_path, tab, variant_index=None):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        if variant_index is not None:
            html_content = html_content.replace('<body onload="showVariant(1)">',
                                                f'<body onload="showVariant({variant_index})">')
        self.web_views[tab].setHtml(html_content)
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
        container_widget.setStyleSheet("background: transparent; border: none;")
        container_widget.setLayout(QVBoxLayout())
        container_widget.layout().addWidget(scroll_area)
        container_widget.resize(1267, 700)
        container_widget.move(87, 60)

    def button_action(self, index):
        self.open_tab(self.taskFirstLabTab, f"Вариант №{index}")
        file_path = "Documentation/FirstLab/FirstLabVariants.html"
        self.load_html_from_file(file_path, self.taskFirstLabTab, index)

    def create_accordion(self, parent):
        scroll_area = QScrollArea(parent)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedSize(1190, 600)
        scroll_area.setStyleSheet("background: transparent; border: none;")

        accordion_widget = QWidget()
        accordion_layout = QVBoxLayout(accordion_widget)

        accordion_layout.setSpacing(0)
        self.create_accordion_item(accordion_layout,"1-ый", "Определение параметров и постановка задачи", "Documentation/FirstLab/test.html")
        self.create_accordion_item(accordion_layout,"2-ой", "Создание модели СМО на GPSS", "Documentation/FirstLab/test.html")
        self.create_accordion_item(accordion_layout,"3-ий", "Анализ результатов моделирования", "Documentation/FirstLab/test.html")

        scroll_area.setWidget(accordion_widget)

        layout = QVBoxLayout(parent)
        layout.setContentsMargins(145, 40, 0, 0)
        layout.addWidget(scroll_area)

    def create_accordion_item(self, layout, step, step_description, html_file_path):
        button = QPushButton()
        button.setCheckable(True)
        accordion_style = load_stylesheet("css_style/accordion.qss")
        button.setStyleSheet(accordion_style)
        button.setFixedSize(1150, 120)

        label = QLabel()
        label_text = f"""
           <span style="font-family: 'Century Gothic'; font-size: 40px; font-weight: bold; padding: 10px; display: inline;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{step} шаг.</span>
           <span style="font-family: 'Century Gothic'; font-size: 30px; display: inline;">&nbsp;&nbsp;{step_description}</span>
           """
        label.setText(label_text)
        label.setAttribute(Qt.WA_TransparentForMouseEvents)

        button_layout = QVBoxLayout()
        button_layout.addWidget(label)
        button.setLayout(button_layout)

        web_view = QWebEngineView()
        web_view.setFixedSize(1150, 1000)

        absolute_path = os.path.abspath(html_file_path)
        web_view.load(QUrl.fromLocalFile(absolute_path))
        web_view.setVisible(False)

        button.clicked.connect(lambda: self.toggle_accordion(web_view))

        item_layout = QVBoxLayout()
        item_layout.addWidget(button)
        item_layout.addWidget(web_view)

        self.spacer = QSpacerItem(10, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        item_layout.addItem(self.spacer)

        layout.addLayout(item_layout)

    def toggle_accordion(self, label):
        label.setVisible(not label.isVisible())

def load_stylesheet(self):
    with open(self, 'r') as f:
        return f.read()
