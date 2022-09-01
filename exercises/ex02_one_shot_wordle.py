"""One shot wordle, get one guess to guess secret word python."""
__author__ = 730561311

wordle_secret: str = "python"
number_of_letters: int = len(wordle_secret)
wordle_guess: str = input(f"What is your { number_of_letters }-letter guess? ")
while len(wordle_guess) < len(wordle_secret) or len(wordle_guess) > len(wordle_secret): 
    wordle_guess: str = input ("That is not 6 letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
def l(a: str, b: int) -> str:
    if a[b] == wordle_secret[b]:
        return GREEN_BOX
    else:
        return WHITE_BOX 

print(l(wordle_guess, 0) + l(wordle_guess, 1) + l(wordle_guess, 2) + l(wordle_guess, 3) + l(wordle_guess, 4) + l(wordle_guess, 5))

while len(wordle_guess) == len(wordle_secret):
    if wordle_guess == wordle_secret:
        print("Woo! You got it!")
        exit()
    else:
        print("Not quite. Play again soon!")
        exit()