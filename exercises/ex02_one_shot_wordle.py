"""One shot wordle, get one guess to guess secret word python."""
__author__ = 730561311

wordle_secret: str = "python"
wordle_guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letters: int = 0
letter_block: str = wordle_guess[letters]
while letters < 6:
    if letter_block == wordle_secret[letters]:
        letter_block == GREEN_BOX
    else:
        letter_block != wordle_secret[letters]
        letter_block == WHITE_BOX
        if letters == 5:
            print(letter_block(0) + letter_block(1) + letter_block(2) + letter_block(3) + letter_block(4) + letter_block(5))
    letters = letters + 1

while len(wordle_guess) < 6 or len(wordle_guess) > 6: 
    wordle_guess: str = input ("That is not 6 letters! Try again: ")

while len(wordle_guess) == len(wordle_secret):
    if wordle_guess == wordle_secret:
        print("Woo! You got it!")
        exit()
    else:
        print("Not quite. Play again soon!")
        exit()