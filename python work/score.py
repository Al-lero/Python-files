PASSMARK = 45
score = int(input("Enter score: "))
if PASSMARK >= score:
	print("your score is", score, "you passed")
else:
	print("your score is", score, "you failed")