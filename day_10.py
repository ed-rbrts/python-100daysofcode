# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(temp_year, temp_month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(temp_year):
#         month_days[1] = 29
#         return month_days[temp_month - 1]
#     else:
#         return month_days[temp_month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
#
#

#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1/n2

calc_functions = {
    "+": add,
    "/": divide,
    "-": subtract,
    "*": multiply
}

def op_check():
    op = input("What operation would you like to perform? \n")
    if op == "+" or op == "-" or op == "/" or op == "*":
        return op
    else:
        print("Enter a valid operand!\n")
        return op_check()

first_number = float(input("Enter a number: \n"))
def should_continue_check():
    should_continue = input("Would you like to continue calculating? (Y or N)\n").upper()
    if should_continue == "Y":
        return True
    elif should_continue == "N":
        return False
    else:
        print("Invalid response!")
        return should_continue_check()

def calculator(num1):
    operation = op_check()
    num2 = float(input("Enter another number: \n"))
    answer = calc_functions[operation](num1, num2)
    print("\n*********************************************")
    print(f"{num1} {operation} {num2} = {answer}")
    print("*********************************************\n")
    if should_continue_check():
        calculator(answer)
    else:
        calculator(float(input("Enter a number: \n")))

calculator(first_number)