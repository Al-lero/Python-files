Account_balance = -1

withdraw = int(input("Enter amount to withdraw: "))

while withdraw != -1:
	if withdraw > Account_balance:
		
		print("Account balance untouched")
	else:
		withdraw == 1
		withdraw = int(input("Enter amount to withdraw: -1 to end:"))
print("withdrawal amount exceeded account balance.")		