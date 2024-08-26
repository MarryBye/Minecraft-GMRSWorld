# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_installs.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_all_installs_2 = QLabel(self.centralwidget)
        self.lbl_all_installs_2.setObjectName(u"lbl_all_installs_2")
        font = QFont()
        self.lbl_all_installs_2.setFont(font)
        self.lbl_all_installs_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_all_installs_2)

        self.lis_not_installed_2 = QListWidget(self.centralwidget)
        self.lis_not_installed_2.setObjectName(u"lis_not_installed_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lis_not_installed_2.sizePolicy().hasHeightForWidth())
        self.lis_not_installed_2.setSizePolicy(sizePolicy)
        self.lis_not_installed_2.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_5.addWidget(self.lis_not_installed_2)

        self.btn_add_install_2 = QPushButton(self.centralwidget)
        self.btn_add_install_2.setObjectName(u"btn_add_install_2")
        self.btn_add_install_2.setFont(font)
        self.btn_add_install_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_add_install_2)

        self.lbl_installs_2 = QLabel(self.centralwidget)
        self.lbl_installs_2.setObjectName(u"lbl_installs_2")
        self.lbl_installs_2.setFont(font)
        self.lbl_installs_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_installs_2)

        self.list_installed_2 = QListWidget(self.centralwidget)
        self.list_installed_2.setObjectName(u"list_installed_2")

        self.verticalLayout_5.addWidget(self.list_installed_2)

        self.btn_delete_install_2 = QPushButton(self.centralwidget)
        self.btn_delete_install_2.setObjectName(u"btn_delete_install_2")
        self.btn_delete_install_2.setFont(font)
        self.btn_delete_install_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_delete_install_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setFont(font)

        self.verticalLayout_6.addWidget(self.textBrowser_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.lbl_install_status = QLabel(self.centralwidget)
        self.lbl_install_status.setObjectName(u"lbl_install_status")
        self.lbl_install_status.setFont(font)
        self.lbl_install_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_install_status)

        self.progress_install = QProgressBar(self.centralwidget)
        self.progress_install.setObjectName(u"progress_install")
        self.progress_install.setFont(font)
        self.progress_install.setValue(0)
        self.progress_install.setTextVisible(False)
        self.progress_install.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_4.addWidget(self.progress_install)

        self.btn_accept_changes = QPushButton(self.centralwidget)
        self.btn_accept_changes.setObjectName(u"btn_accept_changes")
        self.btn_accept_changes.setFont(font)
        self.btn_accept_changes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_accept_changes)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

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
        self.lbl_all_installs_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0441\u0431\u043e\u0440\u043a\u0438", None))
        self.btn_add_install_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.lbl_installs_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043e", None))
        self.btn_delete_install_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14px;\"><br /></p></body></html>", None))
        self.lbl_install_status.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a\u0430\u043a\u0438\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b \u043d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u044e\u0442\u0441\u044f", None))
        self.btn_accept_changes.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
    # retranslateUi

