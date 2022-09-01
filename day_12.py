import random
random_number = random.randint(1, 100)
def difficulty_selector():
    difficulty = int(input("Select a difficulty level: Easy or Hard (1 or 2).\n"))
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 5
    else:
        print("Enter a valid number!")
        difficulty_selector()
no_lives = difficulty_selector()

def wrong(last_guess):
    global no_lives
    global random_number
    new_no_lives = no_lives - 1
    if new_no_lives == 0:
        print("Unlucky! You lose!")
        play_again()
    else:
        beginning = "Nope!"
        middle = ""
        ending = " "
        if last_guess > random_number:
            middle = "Too high!"
        elif last_guess < random_number:
            middle = "Too low!"
        diff = abs(last_guess - random_number)
        if diff < 10:
            ending = "You're warm though!"
        elif diff > 50:
            ending = "You're way off!"
        else:
            ending = "Keep guessing"
        print(beginning + " " + middle + " " + ending)
        no_lives = new_no_lives
        prompt_user()

def correct():
    print("Congratulations! You have guessed my number!")
    play_again()

def prompt_user():
    global random_number
    global no_lives
    print(f"You have {no_lives} lives remaining.")
    guess = int(input("Guess a number:\n"))
    if guess == random_number:
        correct()
    else:
        wrong(guess)

def play_again():
    should_replay = input("Would you like to play again? (Y or N) \n").upper()
    if should_replay == "Y":
        init()
    elif should_replay == "N":
        exit()
    else:
        print("Oops! I didn't understand that.")
        play_again()

def init():
    global random_number
    global no_lives
    random_number = random.randint(1, 100)
    no_lives = difficulty_selector()
    print(f"Hint: The number is {random_number}")
    prompt_user()

print(f"Hint: The number is {random_number}")
prompt_user()





