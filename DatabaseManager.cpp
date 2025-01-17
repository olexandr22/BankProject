#include "DatabaseManager.h"
#include <iostream>

DatabaseManager::DatabaseManager() : db(nullptr) {}

DatabaseManager::~DatabaseManager() {
    closeConnection();
}

void DatabaseManager::openConnection() {
    if (sqlite3_open(dbName.c_str(), &db) != SQLITE_OK) {
        std::cerr << "Error opening database: " << sqlite3_errmsg(db) << std::endl;
    }
}

void DatabaseManager::closeConnection() {
    if (db) {
        sqlite3_close(db);
        db = nullptr;
    }
}

void DatabaseManager::executeQuery(const std::string& query) {
    char* errMsg = nullptr;
    if (sqlite3_exec(db, query.c_str(), nullptr, nullptr, &errMsg) != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    }
}

void DatabaseManager::setupTables() {
    const char* createTableSQL =
        "CREATE TABLE IF NOT EXISTS User ("
        "cardNumber INTEGER PRIMARY KEY, "
        "fullName TEXT NOT NULL, "
        "password TEXT NOT NULL, "
        "age INT NOT NULL"
        ");"

        "CREATE TABLE IF NOT EXISTS BankCard ("
        "cardNumber INTEGER PRIMARY KEY,"
        "balance REAL NOT NULL,"
        "percents REAL NOT NULL,"
        "cardType TEXT NOT NULL,"
        "FOREIGN KEY (cardNumber) REFERENCES User(cardNumber));"

        "CREATE TABLE IF NOT EXISTS BankTransaction ("
        "transactionID INTEGER PRIMARY KEY AUTOINCREMENT,"
        "cardNumber INTEGER,"
        "amount REAL NOT NULL,"
        "category TEXT NOT NULL,"
        "FOREIGN KEY (cardNumber) REFERENCES BankCard(cardNumber));";

    this->executeQuery(createTableSQL);
}