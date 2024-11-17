from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class ShadowEffectManager:
    def __init__(self, main_window):
        self.main_window = main_window

    # Настройка теней для элементов
    def apply_shadow_effects(self):
        shadow_buttons = [
            self.main_window.firstLabButton,
            self.main_window.theoryFirstLabButton,
            self.main_window.exampleFirstLabButton,
            self.main_window.variantsFirstLabButton
        ]
        for button in shadow_buttons:
            self.apply_shadow_effects_to_button(button)

    # Применение тени к отдельной кнопке
    def apply_shadow_effects_to_button(self, button):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(0, 0, 0, 50))
        button.setGraphicsEffect(shadow)
