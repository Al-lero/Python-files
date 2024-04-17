total_sum = 0

for number in range(1, 20_0000):
	if number % 10 == 0:
		total_sum += number
	

print(f"The sum of multiples of 10 between 1 and 20000 is :{total_sum}")