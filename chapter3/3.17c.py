number = 10
i = number

while i >= 1:
	j = number
	while j > i:
		print( end=' ')
		j -= 1
	c = 1
	while c <= i:
		print('*', end='')
		c += 1
	print()
	i -= 1