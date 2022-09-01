import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
scores = {}
hands = {}
playing = 1

"""**************************************************************************************"""

def card(active_player):

    pick = random.choice(cards)
    # print(f"{pick} to {active_player}")
    if pick == 1 and scores[active_player] <= 10:
        scores[active_player] += 11
        hands[active_player].append(11)

    elif pick == 1 and scores[active_player] > 10:
        scores[active_player] += pick
        hands[active_player].append(pick)
    else:
        scores[active_player] += pick
        hands[active_player].append(pick)
    if scores[active_player] > 21:
        playing = 0
        if active_player == "user":
            card_totals()
            print("Unlucky! You lose!")
            play_again()
        else:
            card_totals()
            print("Congratulations! You win!")
            play_again()



def play_again():

    replay = input("Would you like to play again? (Y or N)\n").upper()
    if replay == "Y":
        init()
    elif replay == "N":
        exit()
    else:
        print("Invalid answer!")
        play_again()


def init():
    playing = 1
    scores.clear()
    scores['user'] = 0
    scores['computer'] = 0
    hands.clear()
    hands['user'] = []
    hands['computer'] = []
    card("user")
    card("user")
    card("computer")
    card("computer")
    play()




def should_continue():
    cont_check = input("Type \'y\' to get another card, type \'n\' to pass:\n").upper()
    if cont_check == 'Y':
        card("user")
        play()
    elif cont_check == 'N':
        playing = 0
        if scores["computer"] < 17:
            while scores["computer"] < 17:
                card("computer")
        else:
            coin_toss = random.randint(0, 1)
            if coin_toss == 1:
                card("computer")
        find_winner()
    else:
        should_continue()

def play():

    card_totals()
    should_continue()

def find_winner():

    if scores["user"] > scores["computer"]:
        card_totals()
        print("Congratulations! You have won the game!")
        play_again()
    elif scores["user"] < scores["computer"]:
        card_totals()
        print("Unlucky! You lose!")
        play_again()
    elif scores["user"] == scores["computer"]:
        card_totals()
        print("It's a draw!")
        play_again()
    else:
        print("Error! Something's gone wrong here!")
        play_again()

def card_totals():
    user_score = scores["user"]
    comp_score = scores["computer"]
    user_cards = hands["user"]
    comp_cards = hands["computer"]
    print(f"Your cards: {user_cards}\nYour current score: {user_score}")
    if bool(playing):
        print(f"Computer's first card: {comp_cards[0]}")
    else:
        print(f"Computer's cards: {comp_cards} \nComputer's current score: {comp_score}")


"""***************************************************************************************"""

init()





