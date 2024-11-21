from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor

from MainWindow import MainWindow
from ColoredCircleButton import ColoredCircleButton
from controllers.stylesheet_loader import load_stylesheet

class BackgroundController:
    def __init__(self, main_window : MainWindow):
        self.main_window = main_window
        self.button_size = 46
        self.color_buttons : dict[ColoredCircleButton, str] = {
            ColoredCircleButton(QColor(255, 144, 0, 76), QColor(0, 102, 174, 76), self.button_size, ""): "css_style/window_bg_colors/blue_yellow.qss",
            ColoredCircleButton(QColor(255, 108, 0, 76), QColor(0, 158, 142, 76), self.button_size, ""): "css_style/window_bg_colors/green_orange.qss",
            ColoredCircleButton(QColor(144, 255, 0, 76), QColor(145, 24, 237, 76), self.button_size,""): "css_style/window_bg_colors/green_purple.qss",
            ColoredCircleButton(QColor(180, 13, 0, 76), QColor(0, 102, 174, 76), self.button_size, ""): "css_style/window_bg_colors/red_blue.qss",
        }

        for button, path in self.color_buttons.items():
            button.clicked.connect(lambda _, _path = path, _button = button: self.bind_button(_button, _path))
            self.main_window.colorButtonsLayout.addWidget(button)

        self.displayed_button = None
        list(self.color_buttons.keys())[0].click()

    def bind_button(self, button : ColoredCircleButton, path : str):
        if self.displayed_button is None:
            self.displayed_button = button
            self.hide_undisplayed_buttons()
            
            self.main_window.setStyleSheet(load_stylesheet(path))

            self.main_window.colorButtonsLayout.parentWidget().setStyleSheet("background: rgba(255, 255, 255, 0.3); border-radius: 30px;")
            self.main_window.colorButtonsLayout.parentWidget().setFixedSize(QSize(60, 60))
        else:
            self.show_all_buttons()
        
    def show_all_buttons(self):
        self.main_window.colorButtonsLayout.parentWidget().setStyleSheet("background: white; border-radius: 30px;")
        self.main_window.colorButtonsLayout.parentWidget().setFixedSize(QSize(60, self.color_buttons.__len__() * 60))

        for button in self.color_buttons.keys():
            if button is self.displayed_button:
                continue
            self.main_window.colorButtonsLayout.addWidget(button, alignment=Qt.AlignHCenter)
            button.setHidden(False)

        self.displayed_button = None
        
    def hide_undisplayed_buttons(self):
        for button in self.color_buttons.keys():
            self.main_window.colorButtonsLayout.removeWidget(button)
            button.setHidden(True)

        self.main_window.colorButtonsLayout.addWidget(self.displayed_button, alignment=Qt.AlignHCenter)
        self.displayed_button.setHidden(False)