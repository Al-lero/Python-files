import random

LUCKYNUMBER = random.randrange(1,10)


number = int(input("Enter guess number "))

while number != LUCKYNUMBER:
	guess_number = int(input("Enter guess number "))
	if guess_number == LUCKYNUMBER:
		print("You won")  
		break
	else:
		print("Try Again")



