user_input = -1

while user_input == -1:
	miles = int(input("enter miles driven: "))
	gallon =  int(input("enter gallon used: (-1 to end)"))
	miles_per_gallon = (miles / gallon) 
	print(miles_per_gallon)
	user_input = input("enter gallon used: (-1 to end)")
print("The overall average miles/gallon was: ", miles_per_gallon)


