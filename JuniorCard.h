#pragma once

#include "BankCard.h"

class JuniorCard : public BankCard {
public:
	JuniorCard(DatabaseManager& dbManager)
		:BankCard(0.3, "Junior Card", dbManager) {
	}
};