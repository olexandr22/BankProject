import sys
import Pybind11Module

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QDialog, QWidget, QMessageBox
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide6.QtCore import QObject, QEvent, Qt

from welcomeWidget import Ui_Form as welcomeWidgetForm
from mainAppUi import Ui_MainWindow
from LogIn import Ui_Dialog as logDialog
from register import Ui_Dialog as registerDialog
from request_loan import Ui_Dialog as loanDialog
from withdraw import Ui_Dialog as withdrawDialog
from transfer import Ui_Dialog as transferDialog

AGE_LIMIT_JUNIOR = 14
AGE_LIMIT_ADULT = 18
AGE_LIMIT_MAX = 130

class BankApp(QWidget):
    def __init__(self):
        super(BankApp, self).__init__()
        self.ui = welcomeWidgetForm()
        self.ui.setupUi(self)

        self.dbManager = Pybind11Module.DatabaseManager()
        self.dbManager.openConnection()
        self.dbManager.setupTables()
        self.sortByAsc = True

        self.ui.logIn_button.clicked.connect(self.openLoginWindow)
        self.ui.createAcc_button.clicked.connect(self.openCreateAccWindow)

    def openMainWindow(self):
        self.close()
        self.new_window.close()

        self.new_window = QtWidgets.QMainWindow()
        self.uiMain = Ui_MainWindow()
        self.uiMain.setupUi(self.new_window)
        self.new_window.setWindowTitle("Bank application")
        self.new_window.setWindowIcon(QIcon("logo.png"))

        self.refreshMainData()

        self.uiMain.loan_button.clicked.connect(self.openLoanWindow)
        self.uiMain.withdraw_button.clicked.connect(self.openWithdrawWindow)
        self.uiMain.transfer_button.clicked.connect(self.openTransferWindow)
        self.uiMain.sort_button.clicked.connect(self.transactionSort)
        self.uiMain.sort_button.installEventFilter(self)

        self.new_window.show()

    def openLoginWindow(self):
        self.new_window = QtWidgets.QDialog()
        self.uiLogIn = logDialog()
        self.uiLogIn.setupUi(self.new_window)
        self.new_window.show()

        self.uiLogIn.save_button.clicked.connect(self.logIn)

    def openCreateAccWindow(self):
        self.new_window = QtWidgets.QDialog()
        self.uiReg = registerDialog()
        self.uiReg.setupUi(self.new_window)
        self.new_window.show()

        self.uiReg.save_button.clicked.connect(self.createAcc)

    def openLoanWindow(self):
        self.new_Mainwindow = QtWidgets.QDialog()
        self.uiLoan = loanDialog()
        self.uiLoan.setupUi(self.new_Mainwindow)
        self.new_Mainwindow.show()

        self.uiLoan.save_button.clicked.connect(self.loan)

    def openWithdrawWindow(self):
        self.new_Mainwindow = QtWidgets.QDialog()
        self.uiWithdraw = withdrawDialog()
        self.uiWithdraw.setupUi(self.new_Mainwindow)
        self.new_Mainwindow.show()

        self.uiWithdraw.save_button.clicked.connect(self.withdraw)

    def openTransferWindow(self):
        self.new_Mainwindow = QtWidgets.QDialog()
        self.uiTransfer = transferDialog()
        self.uiTransfer.setupUi(self.new_Mainwindow)
        self.new_Mainwindow.show()

        self.uiTransfer.save_button.clicked.connect(self.transfer)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if obj == self.uiMain.sort_button and event.type() == QEvent.MouseButtonDblClick:
            if event.button() == Qt.LeftButton:  # Подвійний клік лівою кнопкою миші
                self.sortByAsc = False
                self.transactionSort()
                return True  # Подія оброблена
        return super().eventFilter(obj, event)

    def calculateInOut(self, transactions):
        _in = 0
        _out = 0
        for transaction in transactions:
            if 'Income' in transaction.getCategory():
                _in += transaction.getAmount()
            elif 'Outcome' in transaction.getCategory():
                _out += transaction.getAmount()

        self.uiMain.label_income.setText(f"€{_in:.2f}")
        self.uiMain.label_outcome.setText(f"€{_out:.2f}")

    def displayTransactions(self, transactions):
        self.tableView = self.uiMain.tableView

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["card number", "amount", "category"])

        for transaction in transactions:
            row = [
                QStandardItem(str(transaction.getCardNum())),  # Use getter
                QStandardItem(f"{transaction.getAmount():.2f}"),  # Format float with getter
                QStandardItem(transaction.getCategory()),  # Use getter
            ]
            model.appendRow(row)

        self.tableView.setModel(model)

    def transactionSort(self):
        transactions = self.activeTransactions
        sortedTransactions = Pybind11Module.BankTransaction.selectionSort(transactions, self.sortByAsc)
        self.displayTransactions(sortedTransactions)
        self.sortByAsc = True

    def refreshMainData(self):
        self.uiMain.label_card_number.setText(str(self.activeBankCard.getCardNum()))
        self.uiMain.label_balance.setText(f"€{self.activeBankCard.getBalance():.2f}")
        self.uiMain.label_card_type.setText(f"{self.activeBankCard.getCardType()} ({(self.activeBankCard.getPercents() / 10):.2f}%)")

        try:
            self.activeTransactions = Pybind11Module.BankTransaction.readTransactionsByCardNum(self.activeBankCard.getCardNum(), self.dbManager)
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to read transactions: {e}")

        self.displayTransactions(self.activeTransactions)
        self.calculateInOut(self.activeTransactions)

    def newTransaction(self, amount, bankCard, category):
        try:
            newTransaction = Pybind11Module.BankTransaction(bankCard.getCardNum(), amount, category)
            newTransaction.addTransactionToDB(self.dbManager)

            bankCard.addSumToBalance(amount)
            bankCard.updateBalance(self.dbManager)
            self.refreshMainData()
        except Exception as e:
            QMessageBox.critical(self, "Critical Error", f"Failed to create new transaction: {e}")

    def transfer(self):
        amount = float(self.uiTransfer.le_money_amount.text())
        cardNumber = int(self.uiTransfer.le_card_number.text())

        recieverCard = Pybind11Module.BankCard.findCardByNumber(cardNumber, self.dbManager)
        if recieverCard:
            incomeAmount = amount - amount * (self.activeBankCard.getPercents() / 10)

            self.newTransaction(-amount, self.activeBankCard, "Transfer(Outcome)")
            self.newTransaction(incomeAmount, recieverCard, "Transfer(Income)")
        else:
            QMessageBox.warning(self.new_window, "Warning", "Wrong data in transfer.")

        self.new_Mainwindow.close()

    def withdraw(self):
        amount = float(self.uiWithdraw.le_money_amount.text())

        withdrawAmount = amount - amount * (self.activeBankCard.getPercents() / 10)
        self.newTransaction(-withdrawAmount, self.activeBankCard, "Outcome")

        self.new_Mainwindow.close()

    def loan(self):
        amount = float(self.uiLoan.le_money_amount.text())

        self.newTransaction(amount, self.activeBankCard, "Income")

        self.new_Mainwindow.close()


    def createAcc(self):
        fullName = self.uiReg.le_name.text()
        password = self.uiReg.le_password.text()
        age = int(self.uiReg.le_age.text())
        cardType = self.uiReg.comboBox.currentText()

        if cardType == "Universal" and (AGE_LIMIT_ADULT <= age < AGE_LIMIT_MAX):
            self.activeBankCard = Pybind11Module.UniversalCard(self.dbManager)
        elif cardType == "Junior" and (AGE_LIMIT_JUNIOR <= age < AGE_LIMIT_MAX):
            self.activeBankCard = Pybind11Module.JuniorCard(self.dbManager)
        elif cardType == "Business" and (AGE_LIMIT_ADULT <= age < AGE_LIMIT_MAX):
            self.activeBankCard = Pybind11Module.BusinessCard(self.dbManager)

        try:
            self.activeBankCard.writeCardToDB(self.dbManager)
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error with bank Card: {e}")

        try:
            self.activeUser = Pybind11Module.User(fullName, password, age, self.activeBankCard)
            self.activeUser.writeUserDataToDB(self.dbManager)
        except Exception as e:
            QMessageBox.critical(self, "Warning", f"Failed to create an account: {e}")

        self.openMainWindow()

    def logIn(self):
        loggedIn = False

        while not loggedIn:
            cardNum = int(self.uiLogIn.le_cardNum.text())
            password = self.uiLogIn.le_password.text()
            try:
                self.activeUser = Pybind11Module.User.logInFromDB(cardNum, password, self.dbManager)

                if self.activeUser.getPassword() == password:
                    loggedIn = True
                else:
                    QMessageBox.warning(self.new_window, "Warning", "There is no such user.")

                self.uiLogIn.le_cardNum.clear()
                self.uiLogIn.le_password.clear()
            except Exception as e:
                QMessageBox.critical(self, "Warning", f"Failed to log in account: {e}")

        self.activeBankCard = self.activeUser.getCard()
        self.openMainWindow()


def main():
    app = QApplication(sys.argv)

    window = BankApp()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()

