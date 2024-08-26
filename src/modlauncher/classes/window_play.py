from src.modlauncher.classes.base_window import BaseWindow
from src.resources.ui.main_play_ui import Ui_MainWindow

class PlayWindow(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setupUi(ui_object=Ui_MainWindow)
        self.connect_buttons()
        
    def connect_buttons(self):
        pass