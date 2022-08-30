"""One shot wordle, get one guess to guess secret word python."""
__author__ = 730561311

wordle_secret: str = "python"
wordle_guess: str = input("What is your 6-letter guess? ")
 
while len(wordle_guess) < 6 or len(wordle_guess) > 6: 
    wordle_guess: str = input ("That is not 6 letters! Try again: ")

if len(wordle_guess) == len(wordle_secret):
    if wordle_guess == wordle_secret:
        print("Woo! You got it!") 
    else:
        print("Not quite. Play again soon!")



