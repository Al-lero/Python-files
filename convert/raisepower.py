RESULT = 1
i = 1

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))


if i == 1 or i <= number2:
	RESULT = number2 ** number1
	print(str(number1) + " raised to power of " + str(number2) + " is ", str(RESULT))