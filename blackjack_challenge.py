import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
scores = {
    "player": 0,
    "dealer": 0
}
hands = {
    "player": [],
    "dealer": []
}

def deal(recipient):

    new_card = random.choice(cards)
    if scores[recipient] > 10 and new_card == 11:
        return 1
    else:
        return new_card

def deal_to(recip):
    hands[recip].append(deal(recip))
    calculate_scores()

def init():
    scores["player"] = 0
    scores["dealer"] = 0
    hands["player"] = []
    hands["dealer"] = []
    deal_to("player")
    deal_to("player")
    deal_to("dealer")
    deal_to("dealer")
    play()

def play():

    player_hand = hands["player"]
    dealer_first = hands["dealer"][0]
    player_score = scores["player"]
    print(f"Your cards: {player_hand}\nYour score: {player_score}")
    print(f"Dealer's first card: {dealer_first}")
    if scores["player"] == 21:
        print("\n****************************\n       BLACKJACK\n****************************\n")
        dealers_play()
    else:
        should_continue()

def check():
    if scores["player"] > 21:
        print_totals()
        print("Dealer wins!")
        play_again()
    elif scores["dealer"] > 21:
        print_totals()
        print("You win!")
        play_again()

def calculate_scores():
    scores["player"] = sum(hands["player"])
    scores["dealer"] = sum(hands["dealer"])
    check()

def dealers_play():
    if scores["dealer"] < 17 or scores["dealer"] < scores["player"]:
        deal_to("dealer")
        dealers_play()
    elif scores["dealer"] == 21:
        print("\n****************************\n       BLACKJACK\n****************************\n")
        determine_winner()
    else:
        determine_winner()

def determine_winner():
    print_totals()
    check()
    if scores["dealer"] > scores["player"]:
        print("Dealer wins!")
        play_again()
    elif scores["dealer"] < scores["player"]:
        print("Player wins!")
        play_again()
    else:
        print("Draw!")
        play_again()

def play_again():

    replay = input("\nWould you like to play again? (Y or N)\n").upper()
    if replay == "Y":
        init()
    elif replay == "N":
        exit()
    else:
        print("Invalid answer!")
        play_again()

def should_continue():
    cont_check = input("Type \'y\' to get another card, type \'n\' to pass:\n").upper()
    if cont_check == 'Y':
        deal_to("player")
        play()
    elif cont_check == 'N':
        dealers_play()
    else:
        print("Invalid option!")
        should_continue()

def print_totals():
    for competitor in hands:
        hand_list = ' - '.join(map(str, hands[competitor]))
        gap = (15 - len(hand_list)) * " "
        print(f"{competitor.title()} : {hand_list} {gap} TOTAL: {scores[competitor]}\n")

init()