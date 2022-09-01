# student_scores = {
#
#     "Chi": 85,
#     "Yau": 96,
#     "Mok": 76,
#     "David": 68,
#     "James": 71,
#     "Rollo": 65,
#
# }
#
#
# def grade_converter(score_dict):
#     student_grades = {}
#     print("Student:       Grade:\n------------------------------------")
#     for key in score_dict:
#         if score_dict[key] > 70 and score_dict[key] <= 80:
#             student_grades[key] = "Acceptable"
#         elif score_dict[key] > 80 and score_dict[key] <= 90:
#             student_grades[key] = "Exceeds Expectations"
#         elif score_dict[key] > 90 and score_dict[key] <= 100:
#             student_grades[key] = "Outstanding"
#         else:
#             student_grades[key] = "Fail"
#
#     for key in student_grades:
#         print(key + ((15-len(key)) * " ") + student_grades[key])
#
#
# grade_converter(student_scores)

# running = True
#
# travel_log = [
# {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"],
# },
# {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"],
# },
# ]
# def add_new_country(temp_country, temp_visits, temp_cities):
#     new_entry = {}
#     new_entry["country"] = temp_country
#     new_entry["visits"] = temp_visits
#     new_entry["cities"] = temp_cities
#
#     travel_log.append(new_entry)
#
# def add_to_dict():
#     new_country = input("Enter a country that you've been to: \n")
#     no_visits = int(input(f"How many times have you visited {new_country}?\n"))
#     which_cities = input(f"Which cities in {new_country} have you been to:\n").split(", ")
#     add_new_country(new_country, no_visits, which_cities)
#
#     print("Key:        Entry:")
#     print("\n************************************\n************************************\n")
#
#     for log in travel_log:
#         for key in log:
#             if type(log[key]) is list:
#                 print(key.upper() + " :" + ((20 - len(key)) * " ") + "    ".join(log[key]))
#             else:
#                 print(key.upper() + " :" + ((20 - len(key)) * " ") + str(log[key]))
#         print("\n")
#     print("\n************************************\n************************************\n")
#
# while running:
#     add_to_dict()

def clear():
    print("\n" * 1000005)

def continue_check():
    carry_on = input("Would you like to add a bidder? (Y or N) \n").upper()
    temp_bool = True
    if carry_on == "Y":
        temp_bool = True
        clear()
    elif carry_on == "N":
        temp_bool = False
    else:
        print("Invalid answer!")
        return continue_check()
    return temp_bool

def carry_on_bidding():
    return continue_check()

def log_new_entrant():

    new_bid = {}
    new_bid["name"] = input("Enter your name: \n")
    new_bid["bid"] = float(input("Enter your bid: \n£"))
    bid_entrants.append(new_bid)
    # print(bid_entrants)
    # clear()

def check_winner():
    current_high = 0
    winner = ""
    for entrant in bid_entrants:
        if entrant["bid"] > current_high:
            current_high = entrant["bid"]
            winner = entrant["name"]
    print(f"Sold to {winner} for £{current_high:.2f}! Congratulations {winner}!")

bid_entrants = []

while carry_on_bidding():
    log_new_entrant()

check_winner()




