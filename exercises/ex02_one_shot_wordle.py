"""One shot wordle, get one guess to guess secret word python."""
__author__ = 730561311

wordle_secret: str = "python"
wordle_guess: str = (input("What is your 6-letter guess? "))
i: int = 0 
while i < len(wordle_guess):
    print("" + wordle_guess[i])
    i = i + 1
