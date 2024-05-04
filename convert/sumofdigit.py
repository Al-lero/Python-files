SUM = 0

number = int(input("Enter number between 0 and 1000: "))

if number != 0:
	SUM = SUM + (number % 10)
	number = number/ 10
	print(SUM)