import webbrowser

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import Qt, QUrl
import os

from Globals import Config

from MainWindow import MainWindow
from controllers.html_view_types import HtmlViewTypes

class WebViewManager:
    def __init__(self, main_window : MainWindow):
        self.web_view = QWebEngineView(main_window.htmlViewTab)

        self.web_view.setPage(CustomWebEnginePage(self.web_view))

        profile = self.web_view.page().profile()
        profile.clearHttpCache()
        profile.clearAllVisitedLinks()

        self.web_views_config = {
            HtmlViewTypes.Theory: {'size': (1100, 650), 'position': (210, 110)},
            HtmlViewTypes.LabVariant: {'size': (1100, 650), 'position': (210, 110)}
        }
        html_path_getter = lambda: Config.config[Config.current_lab]["theory_path"]
        button_type = HtmlViewTypes.Theory

        main_window.theoryLabButton.clicked.connect(
            lambda: self.load_html_from_file(html_path_getter(), button_type)
        )

    def load_html_from_file(self, file_path: str, type: HtmlViewTypes, variant_index: int = -1):
        absolute_path = os.path.abspath(file_path)

        if variant_index > -1:
            with open(absolute_path, 'r', encoding='utf-8') as file:
                html_content = file.read()

            html_content = html_content.replace('<body onload="showVariant(1)">',
                                                f'<body onload="showVariant({variant_index})">')

            self.web_view.setHtml(html_content)
        else:
            self.web_view.load(QUrl.fromLocalFile(absolute_path))

        self.set_transparent_background()
        self.adjust_web_view_style(type)

        self.web_view.setVisible(False)
        self.web_view.loadFinished.connect(lambda : self.web_view.setVisible(True))

    def set_transparent_background(self):
        """
        Устанавливает прозрачный фон для страницы в QWebEngineView.
        """
        page = self.web_view.page()
        page.setBackgroundColor(Qt.transparent)

    def adjust_web_view_style(self, type : HtmlViewTypes):
        """
        Настроить размер и позицию WebView на вкладке.
        """
        config = self.web_views_config.get(type, {'size': (800, 600), 'position': (10, 10)})

        # Размер WebView
        width, height = config['size']
        self.web_view.resize(width, height)

        # Позиция на странице
        x, y = config['position']
        self.web_view.move(x, y)

class CustomWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, nav_type, is_main_frame):
        """
        Переопределяем обработку запросов на навигацию.
        Если URL относится к внешнему ресурсу, открываем его в системном браузере.
        """
        if url.scheme() in ["http", "https"]:
            webbrowser.open(url.toString())
            return False
        return super().acceptNavigationRequest(url, nav_type, is_main_frame)
