# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'withdraw.ui'
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
        Dialog.resize(390, 300)
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
        self.label.setGeometry(QRect(100, 10, 181, 31))
        self.label.setStyleSheet(u"font_weight: bold;\n"
"font-size: 27pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(217, 31, 2, 0.8)\n"
"")
        self.le_money_amount = QLineEdit(self.frame)
        self.le_money_amount.setObjectName(u"le_money_amount")
        self.le_money_amount.setGeometry(QRect(120, 150, 141, 31))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 90, 241, 41))
        self.label_2.setStyleSheet(u"font_weight: bold;\n"
"font-size: 17pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(140, 220, 101, 31))
        self.save_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Withdraw", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Enter money amount", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

