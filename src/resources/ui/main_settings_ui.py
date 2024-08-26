# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_install_path = QLineEdit(self.centralwidget)
        self.line_install_path.setObjectName(u"line_install_path")
        self.line_install_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.line_install_path)

        self.btn_choose_install_path = QToolButton(self.centralwidget)
        self.btn_choose_install_path.setObjectName(u"btn_choose_install_path")
        self.btn_choose_install_path.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_choose_install_path)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.Label = QLabel(self.centralwidget)
        self.Label.setObjectName(u"Label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.Label)

        self.Label_2 = QLabel(self.centralwidget)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.Label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_minecraft_path = QLineEdit(self.centralwidget)
        self.line_minecraft_path.setObjectName(u"line_minecraft_path")

        self.horizontalLayout_2.addWidget(self.line_minecraft_path)

        self.btn_choose_minecraft_path = QToolButton(self.centralwidget)
        self.btn_choose_minecraft_path.setObjectName(u"btn_choose_minecraft_path")
        self.btn_choose_minecraft_path.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_choose_minecraft_path)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.ComboBox = QComboBox(self.centralwidget)
        self.ComboBox.setObjectName(u"ComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ComboBox)

        self.Label_3 = QLabel(self.centralwidget)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.Label_3)

        self.Label_4 = QLabel(self.centralwidget)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Label_4)

        self.CheckBox = QCheckBox(self.centralwidget)
        self.CheckBox.setObjectName(u"CheckBox")
        self.CheckBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.CheckBox)


        self.verticalLayout_2.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.line_install_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0441\u0431\u043e\u0440\u043a\u0430\u043c...", None))
        self.btn_choose_install_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.Label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043c\u0430\u0439\u043d\u043a\u0440\u0430\u0444\u0442\u0443", None))
        self.line_minecraft_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043c\u0430\u0439\u043d\u043a\u0440\u0430\u0444\u0442\u0443...", None))
        self.btn_choose_minecraft_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Label_3.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.Label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043c\u0430\u0439\u043d\u0435\u0440?", None))
    # retranslateUi

