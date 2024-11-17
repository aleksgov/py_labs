from MainWindow import MainWindow
from controllers.tab_manager import TabManager
from controllers.web_view_manager import WebViewManager
from controllers.shadow_effect_manager import ShadowEffectManager
from controllers.accordion_manager import AccordionManager
from controllers.variants_manager import VariantsManager
from controllers.html_view_types import HtmlViewTypes

class MainController():
    def __init__(self):
        self.mainWindow = MainWindow()
              
        # Менеджеры
        self.variants_manager = VariantsManager()
        self.mainWindow.tasksFrame.layout().addWidget(self.variants_manager.get_scroll_area(19))

        self.tab_manager = TabManager(self.mainWindow)
        self.web_view_manager = WebViewManager(self.mainWindow)
        self.shadow_manager = ShadowEffectManager(self.mainWindow)
        self.accordion_manager = AccordionManager(self.mainWindow)

        # Коннекты
        for i, btn in enumerate(self.variants_manager.buttons):
            btn.clicked.connect(lambda _, index=i: self.bind_variant_button(index + 1))
            self.shadow_manager.apply_shadow_effects_to_button(btn)
            
    def bind_variant_button(self, index):
        self.web_view_manager.load_html_from_file("documentation/FirstLab/Variants.html", HtmlViewTypes.LabVariant, index)
        self.tab_manager.open_tab(self.mainWindow.htmlViewTab, f"Вариант №{index}")