from PyQt5.QtWidgets import QWidget

from MainWindow import MainWindow

class TabManager:
    def __init__(self, main_window : MainWindow):
        self.main_window = main_window
        self.tab_widget = main_window.tab_widget
        self.buttonTabMap = {
            main_window.firstLabButton: (main_window.LabTab, "Лабораторная работа №1"),
            main_window.secondLabButton: (main_window.LabTab, "Лабораторная работа №2"),
            main_window.thirdLabButton: (main_window.LabTab, "Лабораторная работа №3"),
            main_window.fourthLabButton: (main_window.LabTab, "Лабораторная работа №4"),
            main_window.theoryFirstLabButton: (main_window.htmlViewTab, "Теория"),
            main_window.exampleFirstLabButton: (main_window.exampleTab, "Пример"),
            main_window.variantsFirstLabButton: (main_window.variantsTab, "Задачи")
        }

        """
        Настройка подключения кнопок к методам для открытия вкладок.
        """
        for button, (tab, label) in self.buttonTabMap.items():
            button.clicked.connect(lambda _, _tab=tab, _label=label: self.open_tab(_tab, _label))
        
        self.tab_widget.currentChanged.connect(self.on_tab_changed)

        self.close_other_tabs()

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
        tab_name = self.tab_widget.tabText(index)
        self.main_window.LabChangeLabel.setText(tab_name)
        self.close_tabs_after(index)