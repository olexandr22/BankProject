#pragma once

#include "BankCard.h"

class BusinessCard : public BankCard {
public:
	BusinessCard(DatabaseManager& dbManager)
		:BankCard(0.1, "Business Card", dbManager) {
	}
};