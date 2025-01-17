#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "DatabaseManager.h"
#include "User.h"
#include "BankCard.h"
#include "UniversalCard.h"
#include "JuniorCard.h"
#include "BankTransaction.h"
#include "BusinessCard.h"

namespace py = pybind11;

PYBIND11_MODULE(Pybind11Module, m) {
    m.doc() = "A Pybind11 module";

    py::class_<BankTransaction>(m, "BankTransaction")
        .def(py::init<int, double, std::string>(), py::arg("cardNum"), py::arg("amount"), py::arg("category"))
        .def("setAmount", &BankTransaction::setAmount)
        .def("getAmount", &BankTransaction::getAmount)
        .def("setCategory", &BankTransaction::setCategory)
        .def("getCategory", &BankTransaction::getCategory)
        .def("setCardNum", &BankTransaction::setCardNum)
        .def("getCardNum", &BankTransaction::getCardNum)
        .def("addTransactionToDB", &BankTransaction::addTransactionToDB)
        .def_static("writeTransactionToDB", &BankTransaction::writeTransactionToDB)
        .def_static("readTransactionsByCardNum", &BankTransaction::readTransactionsByCardNum)
        .def_static("selectionSort", &BankTransaction::selectionSort, py::arg("transactions"), py::arg("asc"))
        .def("__lt__", &BankTransaction::operator<)
        .def("__gt__", &BankTransaction::operator>);

    py::class_<BankCard>(m, "BankCard")
        .def(py::init<double, std::string, DatabaseManager&>())
        .def(py::init<DatabaseManager&>())
        .def("getCardNum", &BankCard::getCardNum)
        .def("setCardNum", &BankCard::setCardNum)
        .def("getBalance", &BankCard::getBalance)
        .def("setBalance", &BankCard::setBalance)
        .def("getPercents", &BankCard::getPercents)
        .def("setPercents", &BankCard::setPercents)
        .def("getCardType", &BankCard::getCardType)
        .def_static("generateRandomUniqueCardNum", &BankCard::generateRandomUniqueCardNum)
        .def("writeCardToDB", &BankCard::writeCardToDB)
        .def_static("findCardByNumber", &BankCard::findCardByNumber)
        .def("addSumToBalance", &BankCard::addSumToBalance)
        .def("updateBalance", &BankCard::updateBalance)
        .def("setCardType", &BankCard::setCardType);

    py::class_<UniversalCard, BankCard>(m, "UniversalCard")
        .def(py::init<DatabaseManager&>());

    py::class_<JuniorCard, BankCard>(m, "JuniorCard")
        .def(py::init<DatabaseManager&>());

    py::class_<BusinessCard, BankCard>(m, "BusinessCard")
        .def(py::init<DatabaseManager&>());

    py::class_<DatabaseManager>(m, "DatabaseManager")
        .def(py::init<>())
        .def("executeQuery", &DatabaseManager::executeQuery, "Execute a simple SQL query")
        .def("openConnection", &DatabaseManager::openConnection)
        .def("setupTables", &DatabaseManager::setupTables)
        .def("closeConnection", &DatabaseManager::closeConnection, "Close the database connection");

    py::class_<User>(m, "User")
        .def(py::init<std::string, std::string, int, BankCard>(), "Initialize User with name, password, age, and card")
        .def(py::init<BankCard>(), "Initialize User with card")
        .def("getName", &User::getName, "Get user's full name")
        .def("setName", &User::setName, "Set user's full name")
        .def("getAge", &User::getAge, "Get user's age")
        .def("setAge", &User::setAge, "Set user's age")
        .def("getCard", &User::getCard, "Get user's card number")
        .def("setCard", &User::setCard, "Set user's card number")
        .def("getPassword", &User::getPassword, "Get user's password")
        .def("setPassword", &User::setPassword, "Set user's password")
        .def("writeUserDataToDB", &User::writeUserDataToDB, "Write user data to the database")
        .def_static("logInFromDB", &User::logInFromDB, "Log in to the database with card number and password");
}
