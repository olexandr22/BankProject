#pragma once

#include <sqlite3.h>
#include <string>
#include <iostream>

#define DBNAME "C://Users//Olexandro//PycharmProjects//bankProjectPyQt//bank_operations.db"

class DatabaseManager {
private:
    std::string dbName = DBNAME;

public:
    sqlite3* db;

    DatabaseManager();
    ~DatabaseManager();

    void openConnection();
    void closeConnection();
    void executeQuery(const std::string& query);

    void setupTables();
};

