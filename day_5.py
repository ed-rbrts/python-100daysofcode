# students_heights = input("Input a list of heights: ").split(" ")
# for n in range(0, len(students_heights)):
#     students_heights[n] =  int(students_heights[n])
# print(students_heights)
#
# cumHeight = 0
# ind = 0
#
# for h in students_heights:
#     cumHeight += h
#     ind += 1
#
# sumHeights = cumHeight
# numberOfStudents = ind
# avgHeights = int(cumHeight/ind)
#
# print(f"The sum of the heights is: {sumHeights}")
# print(f"There are {numberOfStudents} in this list.")
# print(f"The average of the heights is: {avgHeights}")

# students_scores = input("Input a list of student scores: ").split(" ")
# for n in range(0, len(students_scores)):
#     students_scores[n] = int(students_scores[n])
# print(students_scores)
#
# currentMax = 0
# for i in students_scores:
#     if i > currentMax:
#         currentMax = i
#
# highestScore = currentMax
#
# print(f"The highest score in the class is: {highestScore}")

# sum = 0
# for i in range(0, 101):
#     sum += i
#
# print(sum)

# sum = 0
# for i in range(0, 101):
#     if (i%2) == 0:
#         sum += i
#
# print(sum)

# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

l = int(input("How many letters would you like in your password? \n"))
s = int(input("How many symbols would you like in your password? \n"))
n = int(input("How many numbers would you like in your password? \n"))

totalCharacters = l + s + n
# keys = [letters, numbers, symbols]

lettersList = []
numbersList = []
symbolsList = []

for i in range(0, l):
    lettersIndex = random.randint(0, len(letters) - 1)
    lettersList.append(letters[lettersIndex])

for j in range(0, n):
    numIndex = random.randint(0, len(numbers) - 1)
    numbersList.append(numbers[numIndex])

for k in range(0, s):
    symIndex = random.randint(0, len(symbols) - 1)
    symbolsList.append(symbols[symIndex])

# print(lettersList, numbersList, symbolsList)
possibleCharacters = lettersList + symbolsList + numbersList
random.shuffle(possibleCharacters)
# print(possibleCharacters)
password_as_str = ""
for char in possibleCharacters:
    password_as_str += f"{char}"
# for c in range(0, totalCharacters):
#     charIndex = random.randint(0, len(possibleCharacters) - 1)
#     password += f"{password} + {possibleCharacters[charIndex]}"
#     possibleCharacters.pop(charIndex)


# currentLetters = 0
# currentSymbols = 0
# currentNumbers = 0
#
# tallies = [currentLetters, currentNumbers, currentSymbols]
#
# password = ""
#
# for i in range(0, totalCharacters):
#     charType = random.randint(0, 2)
#     if
#     tallies[charType] += 1
#
#
#
#     for j in keys[charType]:
#         charIndex = random.randint(0, keys[charType])
#         newChar = keys[charType][charIndex]
#         password.append(newChar)

print(f"Here is your password: {password_as_str}")
