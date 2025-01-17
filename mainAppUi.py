# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAppUi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 537)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F2994A, stop:1 #F2C94C);\n"
"font-family: Poppins")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.verticalLayout_4 = QVBoxLayout(self.main)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttons_frame = QFrame(self.main)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(255, 255, 255, 50);\n"
"border-redius: 12px;")
        self.verticalLayout_3 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.loan_button = QPushButton(self.buttons_frame)
        self.loan_button.setObjectName(u"loan_button")
        self.loan_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.loan_button)

        self.withdraw_button = QPushButton(self.buttons_frame)
        self.withdraw_button.setObjectName(u"withdraw_button")
        self.withdraw_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.withdraw_button)

        self.transfer_button = QPushButton(self.buttons_frame)
        self.transfer_button.setObjectName(u"transfer_button")
        self.transfer_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.transfer_button)

        self.sort_button = QPushButton(self.buttons_frame)
        self.sort_button.setObjectName(u"sort_button")
        self.sort_button.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 10);\n"
"} \n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.sort_button)


        self.horizontalLayout_4.addWidget(self.buttons_frame)

        self.userInfoFrame_2 = QFrame(self.main)
        self.userInfoFrame_2.setObjectName(u"userInfoFrame_2")
        self.userInfoFrame_2.setStyleSheet(u"background-color: rgba(120, 120, 120, 85);\n"
"border: 2px solid rgba(255, 255, 255, 50);\n"
"border-redius: 10px;")
        self.userInfoFrame = QVBoxLayout(self.userInfoFrame_2)
        self.userInfoFrame.setObjectName(u"userInfoFrame")
        self.balanceFrame = QFrame(self.userInfoFrame_2)
        self.balanceFrame.setObjectName(u"balanceFrame")
        self.balanceFrame.setStyleSheet(u"background-color: rgba(100, 100, 100, 85);\n"
"border: 2px solid rgba(255, 255, 255, 50);\n"
"border-redius: 12px;")
        self.verticalLayout = QVBoxLayout(self.balanceFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.balanceFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font_weight: bold;\n"
"font-size: 27pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_balance = QLabel(self.balanceFrame)
        self.label_balance.setObjectName(u"label_balance")
        self.label_balance.setStyleSheet(u"font_weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(2, 217, 98, 1);\n"
"")

        self.horizontalLayout_2.addWidget(self.label_balance)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_9 = QLabel(self.balanceFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font_weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(197, 197, 197, 0.8)")

        self.verticalLayout.addWidget(self.label_9)

        self.label_card_type = QLabel(self.balanceFrame)
        self.label_card_type.setObjectName(u"label_card_type")
        self.label_card_type.setStyleSheet(u"font_weight: bold;\n"
"font-size: 13pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(58, 79, 127, 0.8)")

        self.verticalLayout.addWidget(self.label_card_type)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.balanceFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font_weight: bold;\n"
"font-size: 13pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(197, 197, 197, 0.8)\n"
"")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_card_number = QLabel(self.balanceFrame)
        self.label_card_number.setObjectName(u"label_card_number")
        self.label_card_number.setStyleSheet(u"font_weight: bold;\n"
"border: 2px solid black;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"color: rgba(0, 0, 0, 0.8)\n"
"")

        self.horizontalLayout_3.addWidget(self.label_card_number)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.balanceFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font_weight: bold;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(197, 197, 197, 0.8)")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_income = QLabel(self.balanceFrame)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setStyleSheet(u"font_weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(70, 192, 22, 0.8)")

        self.horizontalLayout.addWidget(self.label_income)

        self.label_5 = QLabel(self.balanceFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font_weight: bold;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(197, 197, 197, 0.8)")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_outcome = QLabel(self.balanceFrame)
        self.label_outcome.setObjectName(u"label_outcome")
        self.label_outcome.setStyleSheet(u"font_weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"color: rgba(217, 31, 2, 0.8)")

        self.horizontalLayout.addWidget(self.label_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.userInfoFrame.addWidget(self.balanceFrame)


        self.horizontalLayout_4.addWidget(self.userInfoFrame_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addWidget(self.main)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 2px solid rgba(0, 0, 0, 60);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QTableView:section{\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView:item{\n"
"border-style: none;\n"
"border-bottom: rgba(0, 0, 0, 60);\n"
"}\n"
"\n"
"QTableView:item:selected{\n"
"border: none;\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(235)

        self.verticalLayout_5.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bank", None))
        self.loan_button.setText(QCoreApplication.translate("MainWindow", u"request loan", None))
        self.withdraw_button.setText(QCoreApplication.translate("MainWindow", u"withdraw", None))
        self.transfer_button.setText(QCoreApplication.translate("MainWindow", u"transfer", None))
        self.sort_button.setText(QCoreApplication.translate("MainWindow", u"sort transactions", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.label_balance.setText(QCoreApplication.translate("MainWindow", u"\u20ac500", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Card Type", None))
        self.label_card_type.setText(QCoreApplication.translate("MainWindow", u"Universal", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Card Number", None))
        self.label_card_number.setText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"in", None))
        self.label_income.setText(QCoreApplication.translate("MainWindow", u"\u20ac700", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"out", None))
        self.label_outcome.setText(QCoreApplication.translate("MainWindow", u"\u20ac200", None))
    # retranslateUi

