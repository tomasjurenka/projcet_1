"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Jurenka
email: jurenka-tomas@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

Users = {

    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username:")
password = input("password:")


if username in Users and Users[username] == password:
    print(40 * "\033[35m-\033[0m")
    print("Welcome to the app\033[35m,\033[0m",username)
    print(
        "We have \033[38;5;214m3\033[0m "
        "texts to be analyzed\033[35m.\033[0m"
        )
    print(40 * "\033[35m-\033[0m")
else:
    print(
        "unregistered user\033[35m,\033[0m "
        "terminating the program\033[35m..\033[0m"
        )
    quit()
choose = int(input(
    "Enter a number btw\033[35m.\033[0m "
    "\033[38;5;214m1\033[0m \033[35mand\033[0m "
    "\033[38;5;214m3\033[0m to select: "
    ))
if choose == 1:
    choose = TEXTS[0] 
elif choose == 2:
    choose = TEXTS[1]
elif choose == 3:
    choose = TEXTS[2]   
else: 
    print("Invalid input")     
    quit()
print(40 * "\033[35m-\033[0m")

words_count = 0
capital_letter = 0
big_letters = 0
small_letters = 0
count_numbers = 0
sum_numbers = 0

words = choose.split()
for word in words:
    clean_word = word.strip(",.")
    words_count += 1

    if clean_word.istitle():
        capital_letter += 1
    elif clean_word.isupper():
        big_letters += 1
    elif clean_word.islower():
        small_letters += 1
    elif clean_word.isdigit():
        count_numbers += 1
        sum_numbers += int(clean_word)            

print(
    f"There are \033[38;5;214m{words_count}\033[0m words"
    f" \033[35min\033[0m the selected text\033[35m.\033[0m"
    )
print(
    f"There are \033[38;5;214m{capital_letter}\033[0m"
    f" \033[34mtitlecase\033[0m words\033[35m.\033[0m"
    )
print(
    f"\033[33mThere\033[0m are \033[38;5;214m{big_letters}\033[0m"
    f" uppercase words\033[35m.\033[0m"
    )
print(
    f"There are \033[38;5;214m{small_letters}\033[0m"
    f" \033[34mlowercase\033[0m words\033[35m.\033[0m"
    )
print(
    f"\033[33mThere\033[0m are \033[38;5;214m{count_numbers} \033[0m"
    f"numeric strings\033[35m.\033[0m"
    )
print(f"The sum of all the numbers \033[38;5;214m{sum_numbers}\033[0m")
print(40 * "\033[35m-\033[0m")
print(
    f"{'LEN':<3}\033[35m|\033[0m  {'OCCURRENCES':^12}" 
    f" \033[35m|\033[0m {'NR\033[35m.\033[0m':<3}"
    )
print(40 * "\033[35m-\033[0m")

word_lengths = {}
for word in words:
    clean_word = word.strip(",.")
    length = len(clean_word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1    
for length in sorted(word_lengths):
    stars = "*" * word_lengths[length]        
    print(
        f"\033[38;5;214m{length:<3}\033[0m\033[35m|"
        f"{stars:<20}     |\033[0m"
        f"\033[38;5;214m{word_lengths[length]:>3}\033[0m"
        )