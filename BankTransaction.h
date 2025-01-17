#pragma once

#include "DatabaseManager.h"
#include <list>
#include <algorithm>

class BankTransaction {
	int cardNum;
	double amount;
	std::string category;
public:
	BankTransaction(int cardNum, double amount, std::string category);

	void setAmount(double amount);
	double getAmount();

	void setCategory(std::string category);
	std::string getCategory();

	void setCardNum(int cardNum);
	int getCardNum();

	void addTransactionToDB(DatabaseManager& dbManager);

	static void writeTransactionToDB(const std::list<BankTransaction>& transactions, DatabaseManager& dbManager);
	static std::list<BankTransaction> readTransactionsByCardNum(int cardNum, DatabaseManager& dbManager);
	static std::list<BankTransaction> selectionSort(std::list<BankTransaction> transactions, bool asc);

	bool operator<(BankTransaction const& other) const;
	bool operator>(BankTransaction const& other) const;
};