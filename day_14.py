# while loop. Function that returns true or false. false is returned when answer is wrong
# would you like to play again function
# get two different entries from the dictionary with randint
# make sure they are not the same
# who has more followers

from random import randint
from game_data import data
from art import logo
from art import vs

score = 0

#extract the number of followers from both options and give a description of both
def display(option):
    """ Displays the person/thing from DATA """
    name = option["name"]
    description = option["description"]
    country = option["country"]
    followers = option["follower_count"]
    sp_n = (20 - len("name")) * " "
    sp_d = (20 - len("description")) * " "
    sp_c = (20 - len("country")) * " "
    sp_f = (20 - len("followers")) * " "
    return (f"Name: {sp_n} {name} \nDescription: {sp_d} {description} \nCountry: {sp_c} {country}\nFollowers: {sp_f} {followers}")

# define function to get user's choice
def get_choice():
    """ Function to ask user who they think has more followers.
    Returns true if response matches correct answer. """
    global option_A, option_B
    # get the number of followers for each option
    followers_A = option_A["follower_count"]
    followers_B = option_B["follower_count"]
    # print the logo
    print(logo)
    # display options and VS sign
    print(f"           Compare A: \n{display(option_A)}")
    print(vs)
    print(f"           Against B: \n{display(option_B)}")
    # compare the follower counts and set answer equal to "A" or "B"
    def choice_check():
        """ function to ensure user's input is valid """
        if followers_A > followers_B:
            answer = "A"
        else:
            answer = "B"
        # prompt user
        user_choice = input("\nWho has more followers? Type \'A\' or \'B\'\n").upper()
        # if user enters a valid response, compare user choice to answer and return true if correct
        if user_choice == "A" or user_choice == "B":
            return (answer == user_choice)
        else:
            print("\nInvalid option!")
            return choice_check()
    return choice_check()

def clear():
    print("\n" * 80)
def looper():
    """ The main function that prompts the user to play again or to exit the program. """
    global option_A, option_B, score
    while get_choice():
        # set option_A equal to option_B

        option_A = option_B
        # choose the first person
        randint_B = randint(0, len(data) - 1)
        option_B = data[randint_B]
        # increment score and display
        score += 1
        print(f" You're right! Current score: {score}")
        clear()

    print(f"Sorry, that's wrong! Final score {score}")
    # choose the first person
    randint_A = randint(0, len(data) - 1)
    option_A = data[randint_A]
    # choose the second option
    randint_B = randint(0, len(data) - 1)
    option_B = data[randint_B]

    replay()

def replay():
    """ Function asking user if they would like to play again or to exit.   """
    should_replay = input("Would you like to play again? \'Y\' or \'N\'").upper()
    if should_replay == "Y":
        looper()
        clear()
    elif should_replay == "N":
        exit()
    else:
        replay()

# choose the first person
randint_A = randint(0, len(data) - 1)
option_A = data[randint_A]
# choose the second option
randint_B = randint(0, len(data) - 1)
option_B = data[randint_B]

looper()





