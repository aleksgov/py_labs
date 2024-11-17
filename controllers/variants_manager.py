from PyQt5.QtWidgets import QScrollArea, QPushButton, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QFont
from controllers.stylesheet_loader import load_stylesheet

class VariantsManager:
    def __init__(self, variantsFirstLabTab, taskFirstLabTab, open_tab, load_html_from_file, shadow_effect_manager):
        self.variantsFirstLabTab = variantsFirstLabTab
        self.taskFirstLabTab = taskFirstLabTab
        self.open_tab = open_tab
        self.load_html_from_file = load_html_from_file
        self.shadow_effect_manager = shadow_effect_manager  # Новый параметр для shadow_manager

    def create_buttons_in_variants_tab(self):
        scroll_area = QScrollArea(self.variantsFirstLabTab)
        scroll_area.setWidgetResizable(True)
        qss = load_stylesheet("css_style/scroll.qss")
        scroll_area.setStyleSheet(qss)
        scroll_area_widget = QWidget()
        layout = QGridLayout(scroll_area_widget)
        layout.setHorizontalSpacing(53)
        layout.setVerticalSpacing(48)

        for i in range(30):
            btn = QPushButton("", scroll_area_widget)

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

            # Применяем тень с помощью ShadowEffectManager
            self.shadow_effect_manager.apply_shadow_effects_to_button(btn)

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
        file_path = "documentation/FirstLab/Variants.html"
        self.load_html_from_file(file_path, self.taskFirstLabTab, index)
