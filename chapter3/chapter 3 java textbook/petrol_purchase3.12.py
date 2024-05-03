
print("No 20 ope street, Agboju.Lagos")
print("Gas petrol")

liters = int(input("how many liters are you buying: "))
price = float(input("how much per liter: "))
discount = float(input("how much discount: "))


percentage_discount = (discount / 100)
get_purchase_amount = (liters * price) - percentage_discount

print(f"Amount to pay: {get_purchase_amount: .2f}")






