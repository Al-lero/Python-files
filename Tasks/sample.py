def square():
	return 10 ** 2

print(square())
print(square())
print(square())


def square(number):
	return number ** 2

print(square(5))
print(square(10))                                                        
print(square(15))

def menu():
	print("""
	1. phone bppk
	2. message
	""")

menu()

def add(a, b):
	answer = a + b
	return answer

print(add(4, 5))
print(add(12, 13))

def summationx(numbers, x):
	total = 0
	for i in numbers:
		total += i
	return total + x
print(summationx([10,20,25,15,30],50))

