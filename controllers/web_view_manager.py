from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import os

class WebViewManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.web_views = {
            main_window.theoryFirstLabTab: QWebEngineView(main_window.theoryFirstLabTab),
            main_window.taskFirstLabTab: QWebEngineView(main_window.taskFirstLabTab)
        }

        self.web_views_config = {
            main_window.theoryFirstLabTab: {'size': (1100, 650), 'position': (210, 110)},
            main_window.taskFirstLabTab: {'size': (1100, 768), 'position': (210, 110)}
        }

    def load_initial_content(self):
        self.load_html_from_file("documentation/FirstLab/Theory.html", self.main_window.theoryFirstLabTab)

    def load_html_from_file(self, file_path, tab, variant_index=None):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        if variant_index is not None:
            html_content = html_content.replace('<body onload="showVariant(1)">',
                                                f'<body onload="showVariant({variant_index})">')

        self.web_views[tab].setHtml(html_content)
        self.set_transparent_background(self.web_views[tab])
        self.adjust_web_view(tab)

    def set_transparent_background(self, web_view):
        """
        Устанавливает прозрачный фон для страницы в QWebEngineView.
        """
        page = web_view.page()
        page.setBackgroundColor(Qt.transparent)

    def adjust_web_view(self, tab):
        """
        Настроить размер и позицию WebView на вкладке.
        """
        web_view = self.web_views[tab]
        config = self.web_views_config.get(tab, {'size': (800, 600), 'position': (10, 10)})

        # Размер WebView
        width, height = config['size']
        web_view.resize(width, height)

        # Позиция на странице
        x, y = config['position']
        web_view.move(x, y)
