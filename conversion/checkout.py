VAT = 17.50
total = 0
discount = 0
sub_total = 0
balance = 0
amount_paid = 0
price = 0
quantity = 0
sub_total = 0
bill_total = 0
VAT = 17.50
continue_shopping = 0
result = 0






		

item_list = []

customer_name = input("Enter customer's name : ")

cashier_name = input("Enter Cashier's name: ")


item = input("what do you want to buy?: ")
item_list.append(0)

quantity = int(input("How many pieces?: "))
item_list.append(0)

price = float(input("How much per unit: " ))
item_list.append(0)

result = (quantity * price)
sub_total += result
VAT = (sub_total * 17.50) / 100	
bill_total = sub_total + VAT - discount
balance = (amount_paid - bill_total)

							

input("Do you want to buy something else? (yes/no)? : ")
while 'yes':
	'yes' == continue_shopping
	

	input("what do you want to buy?: ")
	item_list.append(0)
		
	quantity = int(input("How many pieces?: "))
	item_list.append(0)

	price = float(input("How much per unit: " ))
	item_list.append(0)

	input("Do you want to buy something else? (yes/no)? : ")	

	if input != 'yes':
		break
		




input = discount = int(input("How much discount : "))
	

		
discount = (sub_total * discount) / 100	

print("WELCOME TO SEMICOLON STORE\n\nMAIN BRANCH\n\nLOCATION: 312, HERBERT MARCAULY WAY, SABO YABA LAGOS.\n\nTEL:09014465195")
print("Cashier's Name: "+ cashier_name);
print("Customer name: " + customer_name);
print("====================================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")
print("\n---------------------------------------------------")
for i in (item_list):
	if item_list.index(i):
		print(i)

print("\t",item, "/t",quantity,  "/t",price, + (quantity * price))
print("\nSubTotal: ",  sub_total)
print("\n---------------------------------------------------")		
print("Discount: ", discount)
print("\nVAT: ", VAT)
print("\nBill Total: ", bill_total)
print("\n====================================================")
print("THIS IS NOT AN RECEIPT KINDLY PAY: " , bill_total);
amount_paid = int(input("How much did the Customer give to you: "))

print("\nBalance: ", balance)

print("\n====================================================")
print("THANK YOU FOR YOUR PATRONAGE")


	


	
