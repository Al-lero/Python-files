customer_name = input("Enter customer's name: ")
cashie_name = input("Enter cashier's name: ")


item = input("what do you want to buy: ")

quantity = int(input("How many pieces: "))

price = double(input("How much per unit: "))


result = (quantity * price)
sub_total += result
discount = (sub_total * discount) / 100
VAT = (sub_total * 17.50) / 100
