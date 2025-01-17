#pragma once

#include <string>
#include "DatabaseManager.h"
#include "BankCard.h"

class User {
private:
    std::string fullName;
    std::string password;
    int age;
    BankCard card;

public:
    User(std::string name, std::string pswrd, int age, BankCard card);
    User(BankCard bc);

    std::string getName() const;
    void setName(const std::string& new_name);

    int getAge() const;
    void setAge(int new_age);

    BankCard getCard() const;
    void setCard(BankCard newCard);

    std::string getPassword() const;
    void setPassword(const std::string& new_password);

    void writeUserDataToDB(DatabaseManager& dbManager);
    static User* logInFromDB(int logCardNum, const std::string& logPassword, DatabaseManager& dbManager);
};
