WINNING = 5

for number in range (3):
	
	user_input = int(input("Enter guess number "))
	if user_input == WINNING:
		print("You won")
		break
	if user_input != WINNING:
		print("Try Again")


