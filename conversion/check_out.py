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
amount_paid = 0
continue_shopping = 0
result = 0






		

mylist = []

customer_name = input("Enter customer's name : ")

cashier_name = input("Enter Cashier's name: ")


item = input("what do you want to buy?: ")
mylist.append(0)

quantity = int(input("How many pieces?: "))
mylist.append(0)

price = float(input("How much per unit: " ))
mylist.append(0)

result = (quantity * price)
sub_total += result
VAT = (sub_total * 17.50) / 100	
bill_total = sub_total + VAT - discount
balance = (amount_paid - bill_total)

							

while continue_shopping == input("Do you want to buy something else? (yes/no)? : "):
	mylist.append(shopping)
	
if (continue_shopping == "yes"):
	yes == input("Do you want to buy something else? (yes/no)? : ")
	continue_shopping
	mylist.append("\t" + item + "\t" + quantity + "\t" + price + "\t" + (quantity * price))


else:


	discount = int(input("How much discount : "))
	discount = (sub_total * discount) / 100	

print("WELCOME TO SEMICOLON STORE\n\nMAIN BRANCH\n\nLOCATION: 312, HERBERT MARCAULY WAY, SABO YABA LAGOS.\n\nTEL:09014465195")
print("Cashier's Name: "+ cashier_name);
print("Customer name: " + customer_name);
print("====================================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")
print("\n---------------------------------------------------")

print(mylist)
print("\t",item, "/t",quantity,  "/t",price, + (quantity * price))
print("\nSubTotal: ",  sub_total)
print("\n---------------------------------------------------")		
print("Discount: ", discount)
print("\nVAT: ", VAT)
print("\nBill Total: ", bill_total)
print("\n====================================================")
print("THIS IS NOT AN RECEIPT KINDLY PAY: " , bill_total);
amount = input("How much did the Customer give to you: ")
print(amount_paid)
print("\nBalance: ", balance)

print("\n====================================================")
print("THANK YOU FOR YOUR PATRONAGE")

