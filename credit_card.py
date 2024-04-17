sum = 0
alternate = false
number = int(input("Hello' Kindly Enter Card Number to verify: "))
print("credit card Type: " + card_type)
print("Validity Status: " + (is_valid, " Valid", "Invalid"))


	
if(credit_card_Number.length() < 13, credit_card_number.length() > 16):
	return flase



for(i == credit_card_number.legth() -1, i >= 0, i--):
	int digit = integer.parse_int(credit_card_number.substring(i, i + i))


	if(alternat):
		digit = digit % 10 + 1


	sum += digit
	alternate = !alternate
	
return sum % 10 == 0:


	if (credit_card_number.stars_with("4")):
		return "visa"

	if (credit_card_number.stars_with("5")):
		return "Master_Card"

	if (credit_card_number.stars_with("37")):
		return "American_Express"

	if (credit_card_number.stars_with("6")):
		return "Discovery"

	else:
		return "Unknown"






