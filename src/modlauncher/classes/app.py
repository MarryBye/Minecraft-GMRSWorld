from PySide6.QtWidgets import QApplication

from src.modlauncher.classes.resources_controller import ResourcesController

from src.modlauncher.classes.window_main import MainWindow
from src.modlauncher.classes.window_installs import InstallsWindow
from src.modlauncher.classes.window_play import PlayWindow
from src.modlauncher.classes.window_settings import SettingsWindow

from PySide6.QtMultimedia import QSoundEffect

class ModlauncherApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.main_window = MainWindow()
        
        self.installs_window = InstallsWindow()
        self.play_window = PlayWindow()
        self.settings_window = SettingsWindow()
        
        self.pages = [self.installs_window, self.play_window, self.settings_window]
        self.page_now = 0
        
        for page in self.pages:
            self.main_window.ui.layout_content.addWidget(page)
            page.hide()
            
        self.set_page(page_id=0)
        self.connect_buttons()
        
        style = ResourcesController.get_style("Base") % ResourcesController.get_font("Base").family()
        self.setStyleSheet(style)
            
    def get_page(self) -> object:
        return self.pages[self.page_now]
        
    def set_page(self, page_id: int):
        for page in self.pages:
            page.hide() if page != self.pages[page_id] else page.show()
            
    def connect_buttons(self):
        self.main_window.ui.btn_installs.clicked.connect(lambda: self.set_page(0))
        self.main_window.ui.btn_settings.clicked.connect(lambda: self.set_page(2))
        self.main_window.ui.btn_play.clicked.connect(lambda: self.set_page(1))
            
    def exec(self, *args, **kwargs):
        self.main_window.show()
        
        super().exec(*args, **kwargs)
        
        
    