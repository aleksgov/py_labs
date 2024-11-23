from PyQt5.QtWidgets import QWidget

from MainWindow import MainWindow
from Globals import Config

class TabManager:
    def __init__(self, main_window : MainWindow):
        self.main_window = main_window
        self.tab_widget = main_window.tab_widget

        buttonTabMap = {
            main_window.firstLabButton: (main_window.LabTab, "Лабораторная работа №1"),
            main_window.secondLabButton: (main_window.LabTab, "Лабораторная работа №2"),
            main_window.thirdLabButton: (main_window.LabTab, "Лабораторная работа №3"),
            main_window.fourthLabButton: (main_window.LabTab, "Лабораторная работа №4"),
            main_window.theoryLabButton: (main_window.htmlViewTab, "Теория"),
            main_window.exampleLabButton: (main_window.exampleTab, "Пример"),
            main_window.variantsLabButton: (main_window.variantsTab, "Задачи")
        }
        """
        Настройка подключения кнопок к методам для открытия вкладок.
        """
        for button, (tab, label) in buttonTabMap.items():
            button.clicked.connect(lambda _, _tab=tab, _label=label: self.open_tab(_tab, _label))

        variantButtonMap = {
            main_window.firstLabButton: 1,
            main_window.secondLabButton: 2,
            main_window.thirdLabButton: 3,
            main_window.fourthLabButton: 4,
        }

        for button, variant in variantButtonMap.items():
            button.clicked.connect(lambda _, _variant = variant: self.change_variant(_variant))
        
        self.tab_widget.currentChanged.connect(self.on_tab_changed)

        self.close_other_tabs()

    def change_variant(self, variant : int):
        Config.current_lab = variant
        self.main_window.LabChangeLabel.setText(Config.config[Config.current_lab]["header"])

    def open_tab(self, tab : QWidget, label : str):
        """
        Открывает вкладку, добавляя вкладку-пустышку со стрелкой в названии.
        """
        arrow_index = self.tab_widget.addTab(QWidget(), "→")
        self.tab_widget.setTabEnabled(arrow_index, False)
        index = self.tab_widget.addTab(tab, label)
        self.tab_widget.setCurrentIndex(index)

    def close_other_tabs(self):
        """
        Закрывает все вкладки, кроме текущей.
        """
        current_tab = self.tab_widget.currentWidget()
        current_tab_text = self.tab_widget.tabText(self.tab_widget.currentIndex())
        self.tab_widget.clear()
        self.tab_widget.addTab(current_tab, current_tab_text)

    def close_tabs_after(self, index : int):
        """
        Закрывает все вкладки после указанного индекса.
        """
        num_tabs = self.tab_widget.count()
        for i in range(num_tabs - 1, index, -1):
            self.tab_widget.removeTab(i)

    def on_tab_changed(self, index : int):
        """
        Обрабатывает изменение вкладки.
        """
        self.close_tabs_after(index)