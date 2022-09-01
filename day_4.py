import random

# random_integer = random.randint(1, 10)
#
# print(random_integer)

# command = input("Press T to toss the coin!")
# command = command.lower()
#
# toss = bool(round(random.random()))
#
# if command == "t":
#     if toss:
#         print("Heads")
#     else:
#         print("Tails")

# names = input("Enter the names of the people in your party: ")
# name_list = names.split(" ")
# num_of_people = len(name_list)
#
# sel = random.randint(0, num_of_people - 1)
#
# print(name_list[sel] + " must pay the bill today!")
# print(random.choice(name_list))

# print(names)
# print(name_list)
# print(num_of_people)

# row_1 = ["🔲", "🔲", "🔲"]
# row_2 = ["🔲", "🔲", "🔲"]
# row_3 = ["🔲", "🔲", "🔲"]
#
# map = [row_1, row_2, row_3]
# print(f"{row_1}\n{row_2}\n{row_3}")
# position = input("Where do you want to put the treasure? (column, row) ")
# pos = (position.split(", "))
#
# map[int(pos[1])][int(pos[0])] = "x"
# print(f"{row_1}\n{row_2}\n{row_3}")
#
# rand_col = random.randint(0, 2)
# rand_row = random.randint(0, 2)
#
# map[rand_row][rand_col] = "🏴️"
# print(f"\n\n\n{row_1}\n{row_2}\n{row_3}")
#
# x = map[int(pos[1])][int(pos[0])]
# y = map[rand_row][rand_col]
# if x == y:
#     print("\n\nCongratulations! You have found the treasure!")
# else:
#     print("\nUnlucky! No treasure here!")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps = [rock, paper, scissors]
rps_str = ["ROCK", "PAPER", "SCISSORS"]

user_sel = int(input("What do you choose? Rock, paper, or scissors (0, 1, or 2): "))
comp_sel = random.randint(0, 2)

print(f"You chose {rps_str[user_sel]}! \n\n {rps[user_sel]}")
print(f"The computer chose {rps_str[comp_sel]}! \n\n {rps[comp_sel]}")

if user_sel == 0 and comp_sel == 2 or user_sel == 1 and comp_sel == 0 or user_sel == 2 and comp_sel == 1:
    print(f"Congratulations! You have beaten the computer. {rps_str[user_sel]} beats {rps_str[comp_sel]}!")
elif user_sel == comp_sel:
    print("No winner! You've both chosen the same thing!")
else:
    print(f"Unlucky! You've been beaten! {rps_str[comp_sel]} beats {rps_str[user_sel]}!")


