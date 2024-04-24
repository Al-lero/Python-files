base_pay = 5000
number_of_deliveries = 100
total_pay = 0
driver_delivery = 0

driver_delivery = int(input("How many deliveries did the rider make today: "))

if driver_delivery <= 50 :
	total_pay = driver_delivery * 160 + base_pay
	print(total_pay)

elif (driver_delivery >= 50 & driver_delivery <= 59):
	total_pay = driver_delivery * 200 + base_pay
	print(total_pay)

elif (driver_delivery == 60 - 69):
	total_pay = driver_delivery * 250 + base_pay
	print(total_pay)
else:
	total_pay = driver_delivery * 500 + base_pay
	print(total_pay)