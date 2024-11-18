import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QRectF

class ColoredCircleButton(QPushButton):
    def __init__(self, color1, color2, size, args, *kwargs):
        super().__init__(args, *kwargs)
        self.color1 = color1
        self.color2 = color2
        self.setFixedSize(size, size)
        self.setFocusPolicy(Qt.NoFocus)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect().adjusted(4, 4, -4, -4)
        diameter = min(rect.width(), rect.height())
        rect = QRectF(rect.x() + (rect.width() - diameter) / 2,
                      rect.y() + (rect.height() - diameter) / 2,
                      diameter, diameter)

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.color1)
        painter.drawPie(rect, 45 * 16, 180 * 16)

        painter.setBrush(self.color2)
        painter.drawPie(rect, 225 * 16, 180 * 16)