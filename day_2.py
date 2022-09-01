print("Welcome to the tip calculator!\n")
total = input("What was the total bill? £")
num_people = input("How many people to split the bill? ")
perc_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")


tip_per_person = (float(total) * (float(perc_tip)/100))/float(num_people)

print(f"Each person should tip: £{tip_per_person:.2f}")
#
# num_str = input("Type in a two-digit number: ")
# a = int(num_str[0]) + int(num_str[1])
# print(a)

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
#
# bmi = weight/height ** 2
#
# print("Your BMI is : " + str(round(bmi, 2)))
#
#
#

# age = int(input("What is your current age? "))
#
# x = (90 - age) * 365
# y = (90 - age) * 52
# z = (90 - age) * 12
#
# print(f'You have {x} days, {y} weeks, and {z} months left of your life.')







