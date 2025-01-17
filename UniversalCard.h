#pragma once

#include "BankCard.h"

class UniversalCard : public BankCard {
public:
	UniversalCard(DatabaseManager& dbManager)
		:BankCard(0.7, "Universal Card", dbManager) { }
};