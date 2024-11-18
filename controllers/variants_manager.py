from PyQt5.QtWidgets import QScrollArea, QPushButton, QLabel, QGridLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

from controllers.stylesheet_loader import load_stylesheet

class VariantsManager:
    def __init__(self):
        self.buttons : list[QPushButton] = []
        self.create_buttons_in_variants_tab()

    def create_buttons_in_variants_tab(self):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        qss = load_stylesheet("css_style/scroll.qss")
        self.scroll_area.setStyleSheet(qss)
        scroll_area_widget = QWidget()
        layout = QGridLayout(scroll_area_widget)
        layout.setHorizontalSpacing(53)
        layout.setVerticalSpacing(48)

        for i in range(30):
            btn = self.create_button(i)

            row = i // 5
            col = i % 5
            layout.addWidget(btn, row, col)

        self.scroll_area.setWidget(scroll_area_widget)

    def create_button(self, index : int) -> QPushButton:
        btn = QPushButton("")
        self.buttons.append(btn)

        label_number = QLabel(f"{index + 1}")
        label_number.setStyleSheet("font-size: 53px; font-family: 'Century Gothic';")

        label_text = QLabel("Вариант")
        label_text.setStyleSheet("font-size: 21px; font-family: 'Century Gothic';")

        if index + 1 >= 10:
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
        btn.setFixedSize(199, 90)
        btn.setStyleSheet("""
            background-color: white;
            border-radius: 30px;
        """)

        btn.setFocusPolicy(Qt.NoFocus)

        return btn

    def set_buttons_count(self, count : int):
        for i in range(len(self.buttons)):
            if count <= i:
                self.buttons[i].setHidden(True)
            else:
                self.buttons[i].setHidden(False)

    def get_scroll_area(self, count : int) -> QScrollArea:
        self.set_buttons_count(count)
        return self.scroll_area
