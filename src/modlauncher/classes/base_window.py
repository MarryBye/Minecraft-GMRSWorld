from PySide6.QtWidgets import QMainWindow

class BaseWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = None
        
    def setupUi(self, ui_object: object):
        self.ui = ui_object()
        self.ui.setupUi(self)