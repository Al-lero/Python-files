grade = int(input("Enter grade: "))

if grade > 80 and grade >= 100:
	print("your grade is A")

elif grade > 65 and grade <= 79:
	print("your grade is B")

elif grade > 50 and grade <= 64:
	print("your grade is C")

elif grade > 40 and grade <= 49:
	print("your grade is D")
else:
	print("your grade is F") 