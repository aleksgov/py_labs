from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTabWidget, QWidget, QLabel
from PyQt5 import uic
from controllers.tab_manager import TabManager
from controllers.web_view_manager import WebViewManager
from controllers.shadow_effect_manager import ShadowEffectManager
from controllers.accordion_manager import AccordionManager
from controllers.variants_manager import VariantsManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.setMinimumSize(1440, 810)

        # Кнопки и вкладки из interface.ui
        self.firstLabButton = self.findChild(QPushButton, 'FirstLabButton')
        self.theoryFirstLabButton = self.findChild(QPushButton, 'TheoryFirstLabButton')
        self.exampleFirstLabButton = self.findChild(QPushButton, 'ExampleFirstLabButton')
        self.variantsFirstLabButton = self.findChild(QPushButton, 'VariantsFirstLabButton')
        self.tab_widget = self.findChild(QTabWidget, 'tabWidget')
        self.firstLabTab = self.findChild(QWidget, 'FirstLabTab')
        self.theoryFirstLabTab = self.findChild(QWidget, 'TheoryFirstLabTab')
        self.exampleFirstLabTab = self.findChild(QWidget, 'ExampleFirstLabTab')
        self.variantsFirstLabTab = self.findChild(QWidget, 'VariantsFirstLabTab')
        self.taskFirstLabTab = self.findChild(QWidget, 'TaskFirstLabTab')

        for i in range(1, 9):
            label = self.findChild(QLabel, f"label{i}")
            label.setAttribute(Qt.WA_TransparentForMouseEvents)

        # Менеджеры
        self.tab_manager = TabManager(self)
        self.web_view_manager = WebViewManager(self)
        self.shadow_manager = ShadowEffectManager(self)
        self.accordion_manager = AccordionManager(self)
        self.variants_manager = VariantsManager(
            self.variantsFirstLabTab,
            self.taskFirstLabTab,
            self.tab_manager.open_tab,
            self.web_view_manager.load_html_from_file,
            self.shadow_manager
        )

        # Коннекты
        self.tab_manager.setup_tab_connections()
        self.web_view_manager.load_initial_content()
        self.shadow_manager.apply_shadow_effects()
        self.accordion_manager.create_accordion(self.exampleFirstLabTab)
        self.tab_widget.currentChanged.connect(self.tab_manager.on_tab_changed)
        self.tab_manager.close_other_tabs()
        self.variants_manager.create_buttons_in_variants_tab()
