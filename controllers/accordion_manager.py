from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QPushButton, QLabel, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, Qt, QSize
import os

from controllers.stylesheet_loader import load_stylesheet
from MainWindow import MainWindow


class AccordionManager:
    def __init__(self, main_window : MainWindow):
        self.create_accordion(main_window.exampleFirstLabTab)

    def create_accordion(self, parent):
        # Создание области прокрутки
        scroll_area = QScrollArea(parent)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollArea QWidget {
                background: transparent;
            }
        """)

        vertical_scrollbar = scroll_area.verticalScrollBar()
        scroll_style = load_stylesheet("css_style/scroll.qss")
        vertical_scrollbar.setStyleSheet(scroll_style)

        scroll_area.setFixedSize(1190, 600)

        # Основной виджет аккордеона
        accordion_widget = QWidget()
        accordion_layout = QVBoxLayout(accordion_widget)
        accordion_layout.setSpacing(0)

        # Создание контейнеров (элементов) для html
        self.create_accordion_item(accordion_layout, "1-ый", "Определение параметров и постановка задачи",
                                   "documentation/FirstLab/FirstExample.html", container_height=675)
        self.create_accordion_item(accordion_layout, "2-ой", "Создание модели СМО на GPSS",
                                   "documentation/FirstLab/SecondExample.html", container_height=3010)
        self.create_accordion_item(accordion_layout, "3-ий", "Анализ результатов моделирования",
                                   "documentation/FirstLab/ThirdExample.html", container_height=1610)

        # Установка прокрутки для аккордеона
        scroll_area.setWidget(accordion_widget)

        # Основной вертикальный элемент
        layout = QVBoxLayout(parent)
        layout.setContentsMargins(135, 40, 0, 0)
        layout.addWidget(scroll_area)

    def create_accordion_item(self, layout, step, step_description, html_file_path, container_width=1150,
                              container_height=1000):
        # Кнопки аккордеона
        button = QPushButton()
        button.setFocusPolicy(Qt.NoFocus)
        button.setCheckable(True)
        accordion_style = load_stylesheet("css_style/accordion.qss")
        button.setStyleSheet(accordion_style)
        button.setFixedSize(1150, 120)

        # Настройка заголовка у кнопок
        label = QLabel()
        label_text = f"""
           <span style="font-family: 'Century Gothic'; font-size: 40px; font-weight: bold; padding: 10px; display: inline;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{step} шаг.</span>
           <span style="font-family: 'Century Gothic'; font-size: 30px; display: inline;">&nbsp;&nbsp;{step_description}</span>
           """
        label.setText(label_text)
        label.setAttribute(Qt.WA_TransparentForMouseEvents)

        triangle_icon = QIcon(QPixmap("documentation/assets/down_arrow.png"))
        button.setIcon(triangle_icon)
        button.setIconSize(QSize(45, 45))

        button_layout = QVBoxLayout()
        button_layout.addWidget(label)
        button.setLayout(button_layout)

        # Контейнер для WebView (для правильного расположения на странице)
        webview_container = QWidget()
        webview_container.setFixedSize(container_width, container_height)
        webview_container.setStyleSheet("""
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            background-color: white;  
        """)
        webview_container.setVisible(False)
        webview_container.setAttribute(Qt.WA_TransparentForMouseEvents)

        # Создание WebView
        web_view = QWebEngineView(webview_container)
        absolute_path = os.path.abspath(html_file_path)
        web_view.load(QUrl.fromLocalFile(absolute_path))

        # Добавление WebView в контейнер
        web_container_layout = QVBoxLayout(webview_container)
        web_container_layout.addWidget(web_view)

        # Связывание кнопки с функцией отображения / скрытия WebView при нажатии на кнопку
        button.clicked.connect(lambda: self.toggle_accordion(webview_container, button))

        # Вертикальное расположение для каждого элемента аккордеона
        item_layout = QVBoxLayout()
        item_layout.addWidget(button)
        item_layout.addWidget(webview_container)

        # Добавление spacer (отступа) между кнопками
        self.spacer = QSpacerItem(10, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        item_layout.addItem(self.spacer)

        # Добавление отступа в главный контейнер
        layout.addLayout(item_layout)

    def toggle_accordion(self, container, button):
        """
        Функция для переключения видимости WebView в аккордеоне
        """
        container.setVisible(not container.isVisible())

        # Меняем иконку в зависимости от видимости (верхняя\нижняя кнопка)
        if container.isVisible():
            triangle_icon = QIcon(QPixmap("documentation/assets/up_arrow.png"))
        else:
            triangle_icon = QIcon(QPixmap("documentation/assets/down_arrow.png"))

        button.setIcon(triangle_icon)

