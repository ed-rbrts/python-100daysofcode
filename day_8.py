import math
#
# height = int(input("What is the height of your wall? \n"))
# width = int(input("What is the width of your wall? \n"))
# coverage = 5
#
# def paint_calc(h, w,cov):
#     paint_cans = math.ceil((h*w)/cov)
#     print(f"You will need to buy {paint_cans} cans of paint.")
#
# paint_calc(height, width, coverage)

# running = True

# def prime_checker(number):
#     no_of_factors = 0
#     for i in range(2, math.ceil(number/2)+1):
#         if number % i == 0:
#             no_of_factors += 1
#     if no_of_factors == 0:
#         print(f"\n{number} is a prime number.\n")
#     else:
#         print(f"\n{number} is not prime. It has {no_of_factors} factors that aren't 1 and itself.\n")
#
# while(running):
#     n = int(input("\nEnter a number to see if it's a prime number:\n\n "))
#     prime_checker(n)

def encode(text_to_encrypt, shift_amount):
    encrypted_text_list = []
    plain_text_list = list(text_to_encrypt)
    for letter in plain_text_list:
        if letter in alphabet:
            element_number = alphabet.index(letter)
            alph_index = (element_number + shift_amount) % len(alphabet)
            new_letter = alphabet[alph_index]
            encrypted_text_list.append(new_letter)
        else:
            encrypted_text_list.append(letter)
    encrypted_text_string = ''.join(encrypted_text_list)
    if shift_amount < 0:
        message = "DECODED"
    else:
        message = "ENCODED"
    print(f"{message} MESSAGE: \n {encrypted_text_string}")
def decode(encrypted_text, reverse_shift_amount):
    encode(encrypted_text, - (reverse_shift_amount))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running  = True
while running:
    legal_direction = False
    while not legal_direction:
        direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
        if direction == "encode" or direction == "decode":
            legal_direction = True
        else:
            legal_direction = False
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encode(text, shift)
    else:
        decode(text, shift)
    keep_running = input("Would you like to keep the program running. Y or N: \n").lower()
    if keep_running == "y":
        running = True
    elif keep_running == "n":
        running = False








