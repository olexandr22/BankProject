#include "User.h"

User::User(std::string name, std::string pswrd, int age, BankCard card)
    : fullName(std::move(name)), password(pswrd), age(age), card(card) {
}

User::User(BankCard bc) : fullName(""), password("0"), age(0), card(bc) {}

std::string User::getName() const {
    return fullName;
}

void User::setName(const std::string& new_name) {
    fullName = new_name;
}

int User::getAge() const {
    return age;
}

void User::setAge(int new_age) {
    age = new_age;
}

BankCard User::getCard() const {
    return card;
}

void User::setCard(BankCard newCard) {
    card = newCard;
}

std::string User::getPassword() const {
    return password;
}

void User::setPassword(const std::string& new_password) {
    password = new_password;
}

void User::writeUserDataToDB(DatabaseManager& dbManager) {
    std::string query = "INSERT INTO User (cardNumber, fullName, password, age) VALUES (" +
        std::to_string(card.getCardNum()) + ", '" + fullName + "', '" + password + "', " + std::to_string(age) + ");";
    dbManager.executeQuery(query);
}

User* User::logInFromDB(int logCardNum, const std::string& logPassword, DatabaseManager& dbManager) {
    std::string sqlQuery = "SELECT cardNumber, fullName, password, age FROM User WHERE cardNumber = ? AND password = ?;";

    sqlite3_stmt* stmt = nullptr;
    int exitCode = sqlite3_prepare_v2(dbManager.db, sqlQuery.c_str(), -1, &stmt, nullptr);
    if (exitCode != SQLITE_OK) {
        std::cerr << "Error preparing statement: " << sqlite3_errmsg(dbManager.db) << std::endl;
    }

    sqlite3_bind_int(stmt, 1, logCardNum);
    sqlite3_bind_text(stmt, 2, logPassword.c_str(), -1, SQLITE_STATIC);

    exitCode = sqlite3_step(stmt);
    BankCard* userCard = BankCard::findCardByNumber(logCardNum, dbManager);
    User* resultUser = new User(*userCard);

    if (exitCode == SQLITE_ROW) {
        int cardNumber = sqlite3_column_int(stmt, 0);
        const char* fullName = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 1));
        const char* password = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 2));
        int age = sqlite3_column_int(stmt, 3);

        resultUser->setName(fullName);
        resultUser->setPassword(password);
        resultUser->setAge(age);
    }

    sqlite3_finalize(stmt);
    return resultUser;
}