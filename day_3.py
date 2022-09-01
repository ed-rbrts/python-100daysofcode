# print("Welcome to ToneParticle Land!")
# height = int(input("What is your height in cm? "))
# if height > 150:
#     print("Enjoy the ride!")
# else:
#     print("Unfortunately you are too small to enjoy this ride safely. Sorry!")

# number = int(input("Enter a number: "))
# rem = bool(number % 2)
#
# if rem:
#     print(f"{number} is odd")
# else:
#     print(f"{number} is even")

print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

names = name1 + name2

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
l = names.count("l")
o = names.count("o")
v = names.count("v")

tr = t + r + u + e
lv = l + o + v + e

score = str(tr) + str(lv)

print("Your compatibility score is " + score + "% \n")

score_as_int = int(score)

if score_as_int > 90 or score_as_int < 10:
    print("You go together like coke and mentos")
elif 50 > score_as_int > 40:
    print("You are okay together")
else:
    print("Your score is above average but nothing special!")


