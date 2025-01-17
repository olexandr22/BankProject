# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(453, 499)
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
        self.label.setGeometry(QRect(150, 20, 151, 51))
        self.label.setStyleSheet(u"font_weight: bold;\n"
"font-size: 27pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(0, 0, 0, 0.7)\n"
"")
        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(180, 420, 101, 31))
        self.save_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 70, 241, 41))
        self.label_2.setStyleSheet(u"font_weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.le_name = QLineEdit(self.frame)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setGeometry(QRect(120, 120, 221, 31))
        self.le_password = QLineEdit(self.frame)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setGeometry(QRect(120, 190, 221, 31))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 150, 241, 41))
        self.label_3.setStyleSheet(u"font_weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.le_age = QLineEdit(self.frame)
        self.le_age.setObjectName(u"le_age")
        self.le_age.setGeometry(QRect(120, 270, 221, 31))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 230, 181, 41))
        self.label_4.setStyleSheet(u"font_weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 300, 271, 41))
        self.label_5.setStyleSheet(u"font_weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 350, 201, 31))

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Enter your full name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Enter your password", None))
        self.le_age.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Enter your age", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Choose your card type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Junior", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Universal", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Business", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Junior", None))
        self.comboBox.setPlaceholderText("")
    # retranslateUi

