# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomeWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(390, 307)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F2994A, stop:1 #F2C94C);\n"
"font-family: Poppins")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(255, 255, 255, 50);\n"
"border-redius: 12px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 171, 31))
        self.label.setStyleSheet(u"font_weight: bold;\n"
"font-size: 27pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(0, 0, 0, 0.7)\n"
"")
        self.logIn_button = QPushButton(self.frame)
        self.logIn_button.setObjectName(u"logIn_button")
        self.logIn_button.setGeometry(QRect(100, 90, 191, 41))
        self.logIn_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}")
        self.createAcc_button = QPushButton(self.frame)
        self.createAcc_button.setObjectName(u"createAcc_button")
        self.createAcc_button.setGeometry(QRect(100, 160, 191, 41))
        self.createAcc_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Welcome", None))
        self.logIn_button.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.createAcc_button.setText(QCoreApplication.translate("Form", u"Create new Account", None))
    # retranslateUi

