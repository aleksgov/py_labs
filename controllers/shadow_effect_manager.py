from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

from MainWindow import MainWindow

class ShadowEffectManager:
    def __init__(self, main_window : MainWindow):
        self.main_window = main_window
        self.apply_shadow_effects()

    # Настройка теней для элементов
    def apply_shadow_effects(self):
        shadow_buttons = [
            self.main_window.FirstLabWidget,
            self.main_window.FourthLabWidget,
            self.main_window.SecondLabWidget,
            self.main_window.ThirdLabWidget,
            self.main_window.theoryFirstLabButton,
            self.main_window.exampleFirstLabButton,
            self.main_window.variantsFirstLabButton
        ]
        for button in shadow_buttons:
            self.apply_shadow_effects_to_button(button)

    # Применение тени к кнопкам вариантов
    def apply_shadow_effects_to_button(self, button):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(0, 0, 0, 50))
        button.setGraphicsEffect(shadow)
