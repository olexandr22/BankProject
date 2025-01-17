#pragma once

#include "DatabaseManager.h"

#include <string>
#include <sqlite3.h>
#include <cstdlib>
#include <ctime>
#include <iostream>

class BankCard {
protected:
    int cardNum;
    double balance = 0.0;
    double percents;
    std::string cardType;

public:
    BankCard(double pr, std::string ct, DatabaseManager& dbManager);
    BankCard(DatabaseManager& dbManager);

    static int generateRandomUniqueCardNum(DatabaseManager& dbManager);

    int getCardNum() const;
    void setCardNum(int cardNum);

    double getBalance() const;
    void setBalance(double balance);

    double getPercents() const;
    void setPercents(double percents);

    std::string getCardType() const;
    void setCardType(const std::string& cardType);

    void addSumToBalance(double sum);

    static BankCard* findCardByNumber(int cardNum, DatabaseManager& dbManager);
    void writeCardToDB(DatabaseManager& dbManager);
    void updateBalance(DatabaseManager& dbManager);
};