total = 0
product = 1
numbers = []
smallest = numbers
largest = numbers

for number in range (4):
	number = int(input("Enter number: "))
	numbers.append(number)
	total += number
	product *= number
	smallest = min(numbers)
	largest = max(numbers)

average = total / 4


print(f"The total of number is: {total}\nThe average of number is: {average}\nThe product of number is :{product}\nThe smallest of number is:{smallest}\nThe largest number is: {largest}")
