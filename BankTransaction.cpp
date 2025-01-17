#include "BankTransaction.h"

BankTransaction::BankTransaction(int cardNum, double amount, std::string category)
	: cardNum(cardNum), amount(amount), category(category) { }

void BankTransaction::setAmount(double amount) {
	this->amount = amount;
}

double BankTransaction::getAmount() {
	return this->amount;
}

void BankTransaction::setCategory(std::string category) {
	this->category = category;
}

std::string BankTransaction::getCategory() {
	return category;
}

void BankTransaction::setCardNum(int cardNum) {
    this->cardNum = cardNum;
}

int BankTransaction::getCardNum() {
    return cardNum;
}

void BankTransaction::addTransactionToDB(DatabaseManager& dbManager)
{
    const char* insertSQL = "INSERT INTO BankTransaction (cardNumber, amount, category) VALUES (?, ?, ?);";
    sqlite3_stmt* stmt;

    int rc = sqlite3_prepare_v2(dbManager.db, insertSQL, -1, &stmt, nullptr);
    if (rc != SQLITE_OK)
    {
        std::cerr << "Помилка підготовки запиту: " << sqlite3_errmsg(dbManager.db) << std::endl;
    }

    sqlite3_bind_int(stmt, 1, this->cardNum);
    sqlite3_bind_double(stmt, 2, this->amount);
    sqlite3_bind_text(stmt, 3, this->category.c_str(), -1, SQLITE_STATIC);

    if (sqlite3_step(stmt) != SQLITE_DONE)
    {
        std::cerr << "Помилка виконання запиту: " << sqlite3_errmsg(dbManager.db) << std::endl;
        sqlite3_finalize(stmt);
    }

    sqlite3_reset(stmt);

    sqlite3_finalize(stmt);
}

void BankTransaction::writeTransactionToDB(const std::list<BankTransaction>& transactions, DatabaseManager& dbManager) 
{
    const char* insertSQL = "INSERT INTO BankTransaction (cardNumber, amount, category) VALUES (?, ?, ?);";
    sqlite3_stmt* stmt;

    int rc = sqlite3_prepare_v2(dbManager.db, insertSQL, -1, &stmt, nullptr);
    if (rc != SQLITE_OK) 
    {
        std::cerr << "Помилка підготовки запиту: " << sqlite3_errmsg(dbManager.db) << std::endl;
    }
    
    for (const auto& transaction : transactions)
    {
        sqlite3_bind_int(stmt, 1, transaction.cardNum);
        sqlite3_bind_double(stmt, 2, transaction.amount);
        sqlite3_bind_text(stmt, 3, transaction.category.c_str(), -1, SQLITE_STATIC);

        if (sqlite3_step(stmt) != SQLITE_DONE) 
        {
            std::cerr << "Помилка виконання запиту: " << sqlite3_errmsg(dbManager.db) << std::endl;
            sqlite3_finalize(stmt);
        }

        sqlite3_reset(stmt);
    }

    sqlite3_finalize(stmt);
}

std::list<BankTransaction> BankTransaction::readTransactionsByCardNum(int cardNum, DatabaseManager& dbManager) 
{
    std::list<BankTransaction> transactions;

    const char* query = "SELECT cardNumber, amount, category FROM BankTransaction WHERE cardNumber = ?;";
    sqlite3_stmt* stmt;

    int rc = sqlite3_prepare_v2(dbManager.db, query, -1, &stmt, nullptr);
    if (rc != SQLITE_OK) 
    {
        std::cerr << "Помилка підготовки запиту: " << sqlite3_errmsg(dbManager.db) << std::endl;
        return transactions;
    }

    sqlite3_bind_int(stmt, 1, cardNum);

    while (sqlite3_step(stmt) == SQLITE_ROW) 
    {
        int transactionId = sqlite3_column_int(stmt, 0);
        int cardNumber = sqlite3_column_int(stmt, 0);
        double amount = sqlite3_column_double(stmt, 1);
        std::string category = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 2));

        transactions.emplace_front(cardNumber, amount, category);
    }

    sqlite3_finalize(stmt);
    return transactions;
}

std::list<BankTransaction> BankTransaction::selectionSort(std::list<BankTransaction> transactions, bool asc) 
{
    if (transactions.empty()) 
    {
        return transactions;
    }

    std::list<BankTransaction>::iterator it1, it2, temp;

    for (it1 = transactions.begin(); it1 != transactions.end(); ++it1)
    {
        temp = it1;
        for (it2 = std::next(it1); it2 != transactions.end(); ++it2) 
        {
            if (asc ? (*it2 < *temp) : (*it2 > *temp)) {
                temp = it2;
            }
        }
        if (temp != it1) 
        {
            std::iter_swap(it1, temp); 
        }
    }
    return transactions;
}

bool BankTransaction::operator<(BankTransaction const& other) const
{
    return abs(this->amount) < abs(other.amount);
}

bool BankTransaction::operator>(BankTransaction const& other) const
{
    return abs(this->amount) > abs(other.amount);
}