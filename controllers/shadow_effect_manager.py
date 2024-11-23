from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QPushButton
from PyQt5.QtGui import QColor

from MainWindow import MainWindow

class ShadowEffectManager:
    def __init__(self, main_window : MainWindow):
        self.main_window = main_window
        self.apply_shadow_effects()

    # Настройка теней для элементов
    def apply_shadow_effects(self):
        shadow_buttons = [
            self.main_window.firstLabButton,
            self.main_window.secondLabButton,
            self.main_window.thirdLabButton,
            self.main_window.fourthLabButton,
            self.main_window.theoryLabButton,
            self.main_window.exampleLabButton,
            self.main_window.variantsLabButton
        ]
        for button in shadow_buttons:
            self.apply_shadow_effects_to_button(button)

    # Применение тени к кнопкам вариантов
    def apply_shadow_effects_to_button(self, button : QPushButton):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(0, 0, 0, 50))
        button.setGraphicsEffect(shadow)
