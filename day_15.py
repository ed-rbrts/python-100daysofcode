from coffee import MENU
from coffee import resources

kitty = 0
on = True

# TODO 1. Prompt user by asking "What would you like?" espresso/latte/cappucino
def get_command():

    global MENU, resources

    command = input("Please select your coffee: ESPRESSO, LATTE, or CAPPUCCINO.\n").lower()

    if command == "espresso" or command == "latte" or command == "cappuccino":
        if check_resources(command):
            if process_coins(command):
                print("Available resources:")
                print(report())
                return make(command)
            else:
                get_command()
        else:
            get_command()

    # TODO 2. Turn off the machine by entering "off"
    elif command == "off":
        global on
        on = False
        return "Machine turning off. Goodbye!"

    # TODO 3. Print report -on command "report" - to print the current resource values
    elif command == "report":
        return report()

    else:
        print(f"Sorry we don't have {command}. Please enter ESPRESSO, LATTE, or CAPPUCCINO")
        return get_command()

def report():

    global resources, kitty

    formatted_resources = ""

    for key in resources:
        formatted_resources += "           " + key.title() + ":" + ((10 - len(key)) * " ") + str(resources[key]) + "\n"
    formatted_resources += ("\nFloat: £" + "{:.2f}".format(kitty) + "\n")
    formatted_formatted_resources = f"*******************************************\n{formatted_resources}*******************************************\n"
    return formatted_formatted_resources

# TODO 4. Check resources sufficient
def check_resources(coffee_type):

    global MENU, resources
    menu_ingredients = MENU[coffee_type]["ingredients"]
    not_enough = []
    for ingredient in menu_ingredients:
        if menu_ingredients[ingredient] > resources[ingredient]:
            not_enough.append(ingredient)
    if len(not_enough) > 0:
        print(f"Sorry there is not enough {' and '.join(not_enough)}.")
        return False
    else:
        print("HINT: There's enough of everything!")
        return True

# TODO 5. Process coins
def process_coins(coffee_type):

    global MENU, kitty
    price = "{:.2f}".format(MENU[coffee_type]["cost"])
    coins = input(f"Price: £{price}\nInsert coins: (1ps  2ps  5ps  10ps 20ps 50ps £1s)\n").split(" ")
    amount_received = (int(coins[0]) * 0.01) + (int(coins[1]) * 0.02) + (int(coins[2]) * 0.05) + (int(coins[3]) * 0.1) + (int(coins[4]) * 0.2) + (int(coins[5]) * 0.5) + (int(coins[6]) * 1)
    # TODO 6. Check transaction was successful
    change = "{:.2f}".format(amount_received - float(price))
    print("Amount received: £" + "{:.2f}".format(amount_received))
    if amount_received < float(price):
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif amount_received > float(price):
        print(f"Transaction successful! Here is your £{change} change.")
        kitty += float(price)
        return True
    else:
        print("Transaction successful!")
        kitty += float(price)
        return True

# TODO 7. Make the coffee
def make(coffee_type):

    global MENU, resources

    menu_ingredient = MENU[coffee_type]["ingredients"]

    for ingredient in menu_ingredient:
        resources[ingredient] -= menu_ingredient[ingredient]

    return f"Here is your {coffee_type}. Enjoy!  \nNew resources:\n{report()}"

while on:
    print(get_command())








