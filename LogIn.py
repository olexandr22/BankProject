# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogIn.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(490, 368)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F2994A, stop:1 #F2C94C);\n"
"font-family: Poppins")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(255, 255, 255, 50);\n"
"border-redius: 12px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 121, 51))
        self.label.setStyleSheet(u"font_weight: bold;\n"
"font-size: 27pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(0, 0, 0, 0.7)\n"
"")
        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(180, 310, 101, 31))
        self.save_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 70, 281, 41))
        self.label_2.setStyleSheet(u"font_weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.le_cardNum = QLineEdit(self.frame)
        self.le_cardNum.setObjectName(u"le_cardNum")
        self.le_cardNum.setGeometry(QRect(120, 120, 221, 31))
        self.le_password = QLineEdit(self.frame)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setGeometry(QRect(120, 210, 221, 31))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 160, 241, 41))
        self.label_3.setStyleSheet(u"font_weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Log in", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Enter your card number", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Enter your password", None))
    # retranslateUi

