from MainWindow import MainWindow
from controllers.tab_manager import TabManager
from controllers.web_view_manager import WebViewManager
from controllers.shadow_effect_manager import ShadowEffectManager
from controllers.accordion_manager import AccordionManager
from controllers.variants_manager import VariantsManager
from controllers.html_view_types import HtmlViewTypes
from controllers.background_color_controller import BackgroundController
from Globals import Config

class MainController():
    def __init__(self):
        self.mainWindow = MainWindow()
              
        # Менеджеры
        self.variants_manager = VariantsManager()
        self.mainWindow.tasksFrame.layout().addWidget(self.variants_manager.get_scroll_area())
        self.tab_manager = TabManager(self.mainWindow)
        self.web_view_manager = WebViewManager(self.mainWindow)
        self.shadow_manager = ShadowEffectManager(self.mainWindow)
        self.accordion_manager = AccordionManager()
        self.backgound_controller = BackgroundController(self.mainWindow)

        self.tab_manager.tab_widget.currentChanged.connect(self.on_tab_changed)

        # Коннекты
        for i, btn in enumerate(self.variants_manager.buttons):
            btn.clicked.connect(lambda _, index=i: self.bind_variant_button(index + 1))
            self.shadow_manager.apply_shadow_effects_to_button(btn)

    def on_tab_changed(self, index : int):
        self.variants_manager.set_buttons_count(Config.config[Config.current_lab]["variants_count"])
        current_tab = self.tab_manager.tab_widget.currentWidget()
        if current_tab is self.mainWindow.exampleTab:
            self.accordion_manager.create_accordion(current_tab)
            
    def bind_variant_button(self, index : int):
        variants_path = Config.config[Config.current_lab]["variants_path"]
        self.web_view_manager.load_html_from_file(variants_path, HtmlViewTypes.LabVariant, index)
        self.tab_manager.open_tab(self.mainWindow.htmlViewTab, f"Вариант №{index}")