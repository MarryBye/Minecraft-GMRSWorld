import sys

from PySide6.QtCore import QFile, QIODevice, QTextStream, QUrl
from PySide6.QtGui import QFontDatabase, QFont, QIcon, QImage, QPixmap
from PySide6.QtMultimedia import QSoundEffect

class ResourcesController:
    @staticmethod
    def get_font(font_name: str) -> QFont:
        font_id = QFontDatabase.addApplicationFont(f":/fonts/{font_name}")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(font_family)
            return QFont(font_family)
        
    @staticmethod
    def get_image(image_name: str) -> QImage:
        return QImage(f":/images/{image_name}")
    
    @staticmethod
    def get_icon(icon_name: str) -> QIcon:
        return QIcon(f":/images/{icon_name}")
    
    @staticmethod
    def get_pixmap(pixmap_name: str) -> QPixmap:
        return QPixmap(f":/images/{pixmap_name}")
    
    @staticmethod
    def get_sound(sound_name: str) -> QSoundEffect:
        sound = QSoundEffect()
        sound.setSource(f":/sounds/{sound_name}")
        sound.setVolume(1)
        sound.setLoopCount(2)
        
        return sound
    
    @staticmethod
    def get_style(style_name: str) -> str:
        stylesheet = QFile(f":/styles/{style_name}")
        style_string = ""
        
        if stylesheet.open(QIODevice.ReadOnly | QIODevice.Text):
            stream = QTextStream(stylesheet)
            style_string = stream.readAll()
            stylesheet.close()
        
        return style_string