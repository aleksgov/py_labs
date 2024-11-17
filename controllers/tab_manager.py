from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class TabManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.tab_widget = main_window.tab_widget
        self.buttonTabMap = {
            main_window.firstLabButton: (main_window.firstLabTab, "Лабораторная работа №1"),
            main_window.theoryFirstLabButton: (main_window.theoryFirstLabTab, "Теория"),
            main_window.exampleFirstLabButton: (main_window.exampleFirstLabTab, "Пример"),
            main_window.variantsFirstLabButton: (main_window.variantsFirstLabTab, "Задачи")
        }

    def setup_tab_connections(self):
        """
        Настроить подключение кнопок к методам для открытия вкладок.
        """
        for button, (tab, label) in self.buttonTabMap.items():
            button.clicked.connect(lambda checked, _tab=tab, _label=label: self.open_tab(_tab, _label))

    def open_tab(self, tab, label):
        """
        Открывает вкладку, если она еще не открыта. Если вкладка уже существует,
        переключает на нее.
        """
        index = self.tab_widget.indexOf(tab)
        if index == -1:
            arrow_tab = self.create_arrow_tab()
            arrow_index = self.tab_widget.addTab(arrow_tab, "→")
            self.tab_widget.setTabEnabled(arrow_index, False)
            index = self.tab_widget.addTab(tab, label)
        self.tab_widget.setCurrentIndex(index)

    def close_other_tabs(self):
        """
        Закрывает все вкладки, кроме текущей.
        """
        num_tabs = self.tab_widget.count()
        current_index = self.tab_widget.currentIndex()
        for i in range(num_tabs - 1, -1, -1):
            if i != current_index:
                self.tab_widget.removeTab(i)

    def close_tabs_after(self, index):
        """
        Закрывает все вкладки после указанного индекса.
        """
        num_tabs = self.tab_widget.count()
        for i in range(num_tabs - 1, index, -1):
            self.tab_widget.removeTab(i)

    def create_arrow_tab(self):
        """
        Создает вкладку со стрелкой, которая используется для индикатора процесса открытия вкладки.
        """
        arrow_tab = QWidget()
        layout = QVBoxLayout(arrow_tab)
        arrow_label = QLabel("→", arrow_tab)
        arrow_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(arrow_label)
        return arrow_tab

    def on_tab_changed(self, index):
        """
        Обрабатывает изменение вкладки и закрывает все вкладки, кроме текущей.
        """
        self.close_tabs_after(index)