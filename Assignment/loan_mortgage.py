amount = float(input("amount: "))
rate = float(input("monthly_interest_rate: "))
time = float(input("Loan_duration: "))

MONTH = 12

PERCENTAGE = 100

X = time * 12

K = (rate / 12) / 100


Numerator = amount * K * (1 + K) ** X

Denominator = ((1 + K) ** (X)) - 1

monthly_payment = Numerator / Denominator

print("$", monthly_payment)