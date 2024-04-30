VAT = 17.50
discount_amount = 0
sub_total = 0
balance = 0
amount_paid = 0
price = 0
quantity = 0
bill_total = 0
VAT_amount = 0
total_price = 0
bill_total = 0



item_list = []

customer_name = input("Enter customer's name : ")
cashier_name = input("Enter Cashier's name: ")

user_input = "yes"
while user_input == "yes":
	item = []
	item_name = input("what do you want to buy?: ")
	item.append(item_name)
		
	quantity = int(input("How many pieces?: "))
	item.append(quantity)

	price = int(input("How much per unit: " ))
	item.append(price)
	item_list.append(item)

	user_input= input("Do you want to buy something else? (yes/no)? : ")	

for items in item_list:
	total_for_items = items[1] * items[2]
	total_price += total_for_items

discount = int(input("How much discount : "))
discounted_amount = (total_price * discount) / 100
VAT_amount = (total_price * 17.50) / 100

bill_total = total_price + discounted_amount  + VAT_amount
balance = (amount_paid - bill_total)




print("WELCOME TO SEMICOLON STORE\n\nMAIN BRANCH\n\nLOCATION: 312, HERBERT MARCAULY WAY, SABO YABA LAGOS.\n\nTEL:09014465195")
print("Cashier's Name: "+ cashier_name);
print("Customer name: " + customer_name);
print("====================================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")
print("---------------------------------------------------")
for items in item_list:
    print(f"\t{items[0]}\t{items[1]}\t{items[2]}\t{items[1] * items[2]}")
print("---------------------------------------------------")
print(f"Sub Total:\t{total_price}")
print(f"Discount:\t{discounted_amount}")
print(f"VAT:\t\t{VAT_amount}")
print("Bill Total:\t", bill_total)
print("====================================================")
print("THIS IS NOT AN RECEIPT KINDLY PAY: " , bill_total);
amount_paid = int(input("How much did the Customer give to you: "))
print(f"Balance:\t{amount_paid - bill_total}")
print("\n====================================================")
print("THANK YOU FOR YOUR PATRONAGE")


	


	
