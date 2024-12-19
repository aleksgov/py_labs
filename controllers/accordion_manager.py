from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QPushButton, QLabel, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, Qt, QSize
import os

from controllers.stylesheet_loader import load_stylesheet
from Globals import Config

class AccordionManager:

    def create_accordion(self, parent : QWidget):
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
        vertical_scrollbar.setStyleSheet(load_stylesheet("css_style/scroll.qss"))

        scroll_area.setFixedSize(1190, 640)

        # Основной виджет аккордеона
        accordion_widget = QWidget()
        self.accordion_layout = QVBoxLayout(accordion_widget)
        self.accordion_layout.setSpacing(0)

        # Создание контейнеров (элементов) для html
        for i in range(Config.config[Config.current_lab]["example"]["steps_count"]):
            temp = Config.config[Config.current_lab]["example"]
            self.create_accordion_item(temp["steps_counters"][i],
                                       temp["steps_headers"][i],
                                       temp["steps_paths"][i])

        # Установка прокрутки для аккордеона
        scroll_area.setWidget(accordion_widget)

        # Прикрепление layout к другому родителю, чтобы освободить место под новый
        if parent.layout():
            QWidget().setLayout(parent.layout())

        # Основной вертикальный элемент
        layout = QVBoxLayout()
        layout.setContentsMargins(135, 140, 0, 0)
        layout.addWidget(scroll_area)
        parent.setLayout(layout)

    def create_accordion_item(self, step, step_description, html_file_path, container_width=1150,
                              container_height=1000):
        # Кнопки аккордеона
        button = QPushButton()
        button.setFocusPolicy(Qt.NoFocus)
        button.setCheckable(True)
        accordion_style = load_stylesheet("css_style/accordion.qss")
        button.setStyleSheet(accordion_style)
        button.setFixedSize(1150, 120)

        # Настройка заголовка у кнопок
        label_text = f"""
           <span style="font-family: 'Century Gothic'; font-size: 40px; color: #333; font-weight: bold; padding: 10px; display: inline;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{step} шаг.</span>
           <span style="font-family: 'Century Gothic'; font-size: 30px; color: #333; display: inline;">&nbsp;&nbsp;{step_description}</span>
           """
        button_label = QLabel(label_text)
        button_label.setAttribute(Qt.WA_TransparentForMouseEvents)

        triangle_icon = QIcon(QPixmap("documentation/assets/down_arrow.png"))
        button.setIcon(triangle_icon)
        button.setIconSize(QSize(45, 45))

        button_layout = QVBoxLayout()
        button_layout.addWidget(button_label)
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

        web_view.loadFinished.connect(lambda: self.resize_web_view_to_contents(web_view, webview_container))

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
        spacer = QSpacerItem(10, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)
        item_layout.addItem(spacer)

        # Добавление отступа в главный контейнер
        self.accordion_layout.addLayout(item_layout)
        
    def resize_web_view_to_contents(self, web_view : QWebEngineView, webview_container : QWidget):
        script = """
        var textSize = document.body.getBoundingClientRect();

        size = { width: textSize.right, height: textSize.bottom};
        """
        web_view.page().runJavaScript(script, lambda size: self.resize_web_view(size, webview_container))

    def resize_web_view(self, size, webview_container : QWidget):
        webview_container.setFixedSize(webview_container.geometry().width(), int(size['height']) + 40)

    def toggle_accordion(self, container : QWidget, button : QPushButton):
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

