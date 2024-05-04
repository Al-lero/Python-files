FACTORIAL = 1
i = 1
number = int(input("Enter a number: "))

if i == 1 or i <= number:
	FACTORIAL *= i
	print("Factorial of " + str(number) + " is " +  str(FACTORIAL))
	