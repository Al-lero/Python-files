first_name = input("Enter first name: " )

surname = input("Enter surname: ")

gender = input("Enter gender: ")

day = int (input("Enter day of birth: "))
month = input("Enter a month of birth: ")
year = int(input("Enter a year of birth: "))


Age = (2024 - year)

maximum_heart_beat = ( 220 - Age)


targeted_heart_beat = (220 - Age) * 70 / 100

 

print(first_name, surname, day, month, year,  Age,  maximum_heart_beat, targeted_heart_beat)