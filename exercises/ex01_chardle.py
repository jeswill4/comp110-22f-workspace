"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730561311"


"""First two variables."""
chardle_word: str = input("Enter a 5-character word: ")

chardle_abc: str = input("Enter a single character: ")

print("Searching for " + chardle_abc + " in " + chardle_word)

"""Using if else statements to figure out if the letter guessed is in the word given, and where if so."""
if chardle_abc == chardle_word[0]:
    print(chardle_abc + " found at index 0") 
else:
    chardle_abc != chardle_word[0]

if chardle_abc == chardle_word[1]:
    print(chardle_abc + " found at index 1")
else:
    chardle_abc != chardle_word[1]

if chardle_abc == chardle_word[2]:
    print(chardle_abc + " found at index 2")
else:
    chardle_abc != chardle_word[2]

if chardle_abc == chardle_word[3]:
    print(chardle_abc + " found at index 3")
else:
    chardle_abc != chardle_word[3]

if chardle_abc == chardle_word[4]:
    print(chardle_abc + " found at index 4")
else:
    chardle_abc != chardle_word[4]

"""Using int and addition to figure out total amount of letters that where guessed in the letters of the word."""
correct_amount_abc = int(chardle_abc == chardle_word[0]) + int(chardle_abc == chardle_word[1]) + int(chardle_abc == chardle_word[2]) + int(chardle_abc == chardle_word[3]) + int(chardle_abc == chardle_word [4])

"""Using the above variable made to give back the information of how many instances the guessed letter appears in the word."""

if correct_amount_abc == 0:
    print("No instances of " + chardle_abc + " found in " + chardle_word)
else:
    correct_amount_abc != 0

if correct_amount_abc == 1:
    print("1 instance of " + chardle_abc + " found in " + chardle_word)
else:
    correct_amount_abc != 1

if correct_amount_abc == 2:
    print("2 instances of " + chardle_abc + " found in " + chardle_word)
else: 
    correct_amount_abc != 2

if correct_amount_abc == 3:
    print("3 instances of " + chardle_abc + " found in " + chardle_word)
else: 
    correct_amount_abc != 3

if correct_amount_abc == 4:
    print("4 instances of " + chardle_abc + " found in " + chardle_word)
else: 
    correct_amount_abc !=4

if correct_amount_abc == 5:
    print("5 instances of " + chardle_abc + " found in " + chardle_word)

