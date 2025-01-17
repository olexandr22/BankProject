#include "BankCard.h"

BankCard::BankCard(double pr, std::string ct, DatabaseManager& dbManager)
    : percents(pr), cardType(ct), cardNum(this->generateRandomUniqueCardNum(dbManager)){}

BankCard::BankCard(DatabaseManager& dbManager)
    : cardNum(0), balance(0.0), percents(0.0), cardType("") { }

int BankCard::generateRandomUniqueCardNum(DatabaseManager& dbManager) {
    std::srand(static_cast<unsigned>(std::time(nullptr)));

    int newCardNum;
    bool isUnique = false;

    while (!isUnique) {
        newCardNum = 100000 + std::rand() % 900000;

        BankCard* temp = findCardByNumber(newCardNum, dbManager);
        if (temp == nullptr) {
            isUnique = true;
        }
    }
    return newCardNum;
}

BankCard* BankCard::findCardByNumber(int cardNum, DatabaseManager& dbManager) {
    BankCard* resultCard = new BankCard(dbManager);

    const char* query = "SELECT cardNumber, balance, percents, cardType FROM BankCard WHERE cardNumber = ?";
    sqlite3_stmt* stmt;
    int rc = sqlite3_prepare_v2(dbManager.db, query, -1, &stmt, nullptr);

    if (rc != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(dbManager.db) << std::endl;
    }

    sqlite3_bind_int(stmt, 1, cardNum);

    if (sqlite3_step(stmt) == SQLITE_ROW) {
        int fetchedCardNum = sqlite3_column_int(stmt, 0);
        double balance = sqlite3_column_double(stmt, 1);
        double percents = sqlite3_column_double(stmt, 2);
        std::string cardType(reinterpret_cast<const char*>(sqlite3_column_text(stmt, 3)));

        sqlite3_finalize(stmt);
        resultCard->setBalance(balance);
        resultCard->setCardNum(fetchedCardNum);
        resultCard->setCardType(cardType);
        resultCard->setPercents(percents);
    }
    else {
        resultCard = nullptr;
        sqlite3_finalize(stmt);
    }

    return resultCard;
}

void BankCard::writeCardToDB(DatabaseManager& dbManager) {
    std::string query = "INSERT INTO BankCard (cardNumber, balance, percents, cardType) VALUES (" +
        std::to_string(cardNum) + ", '" + std::to_string(balance) + "', '" + std::to_string(percents) + "', " + "'" + cardType + "'"");";

    dbManager.executeQuery(query);
}

void BankCard::updateBalance(DatabaseManager& dbManager) {
    const char* sql = "UPDATE BankCard SET balance = ? WHERE cardNumber = ?;";
    sqlite3_stmt* stmt;

    if (sqlite3_prepare_v2(dbManager.db, sql, -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Помилка підготовки SQL запиту: " << sqlite3_errmsg(dbManager.db) << std::endl;
    }

    sqlite3_bind_double(stmt, 1, this->balance); 
    sqlite3_bind_int(stmt, 2, this->cardNum);        

    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Помилка виконання SQL запиту: " << sqlite3_errmsg(dbManager.db) << std::endl;
        sqlite3_finalize(stmt);
    }

    sqlite3_finalize(stmt);
}

int BankCard::getCardNum() const { return cardNum; }
void BankCard::setCardNum(int cardNum) { this->cardNum = cardNum; }

double BankCard::getBalance() const { return balance; }
void BankCard::setBalance(double balance) { this->balance = balance; }

double BankCard::getPercents() const { return percents; }
void BankCard::setPercents(double percents) { this->percents = percents; }

std::string BankCard::getCardType() const { return cardType; }
void BankCard::setCardType(const std::string& cardType) { this->cardType = cardType; }

void BankCard::addSumToBalance(double sum) { this->balance += sum; }
