VAT = 17.50
total = 0
discount = 0
sub_total = 0
balance = 0
amount_paid = 0
pieces = 0
unit = 0
buy = 0



sub_total += pieces * unit
VAT = (sub_total * 17.50) / 100
bill_total = sub_total + VAT - discount
balance = amount_paid - bill_total
discount = (sub_total * discount) / 100


customer_name = input("Enter customer's name : ")

cashier_name = input("Enter Cashier's name: ")


buy = input("what do you want to buy?: ")

pieces = input("How many pieces? : ")

unit = input("How much per unit[]: " )



while continue_shopping == input("Do you want to buy something else? (yes/no)? : "):
	buy
	continue_shopping = buy

if (continue_shopping.casefold("yes")):
	break

elif (continue_shopping.casefold("no")):
	break

else:

		discount = int(input("How much discount : "))
		
			

print("WELCOME TO SEMICOLON STORE\n\nMAIN BRANCH\n\nLOCATION: 312, HERBERT MARCAULY WAY, SABO YABA LAGOS.\n\nTEL:09014465195")
print("Cashier's Name: "+ name);
print("Customer name: " + customerName);
print("====================================================")
print("\tITEM\tQTY\tPRICE\tTOTAL(NGN)")
print("\n---------------------------------------------------")
print("\t" + buy + "\t" + pieces + "\t" + unit + "\t" + pieces * unit )
print("\nSubTotal: " + subTotal)
print("\n---------------------------------------------------")
print("Discount: " + discount)
print("\nVAT: " + VAT)
print("\nBill Total: " + billTotal)
print("\n====================================================")
print("THIS IS NOT AN RECEIPT KINDLY PAY: " + billTotal);
amount = input("How much did the Customer give to you: ")
print(amount)
print("\nBalance: " + (amountPaid - billTotal))
print("\n====================================================")
print("THANK YOU FOR YOUR PATRONAGE")
			



