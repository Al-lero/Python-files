first_name = input("Enter first name: " )

surname = input("Enter surname: ")

gender = input("Enter gender: ")

day = int (input("Enter day of birth: "))
month = input("Enter a month of birth: ")
year = int(input("Enter a year of birth: "))

height_in_inches = float(input("Enter height: "))

weight_in_pounds = float(input("Enter weight: "))

seconds = 60

Age = (2024 - year)

maximum_heart_beat = (220 - Age)

targeted_heart_rate = (maximum_heart_beat * 0.70)

BMI = (weight_in_pounds / ( height_in_inches * height_in_inches)) * 703

print(f"{first_name}, {surname}, {Age}, {BMI: .2f}, {maximum_heart_beat}, {targeted_heart_rate: .2f}")