"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730561311"

chardle_word: str = input("Enter a 5-character word: ")

chardle_abc: str = input("Enter a single character: ")

print("Searching for " + chardle_abc + " in " + chardle_word)

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


