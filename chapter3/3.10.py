Rate = 7
year = 30



Amount = int(input("Enter amount: "))

number_of_years = int(input("Enter number of years: "))


for number in range(number_of_years):
	Rate = 7 / 100

	monthly_payment = ( Rate * Amount  )
	Amount = (monthly_payment + Amount)
	 
	print(f"number_of_years: {number +1} {Amount: .2f}")


