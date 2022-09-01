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

def l(b: int) -> str:
    """To insert colors for wordle letters, green is correct letter correct place, yellow is correct letter wrong place, and white is incorrect letter."""
    if b < number_of_letters:
        if wordle_guess[b] == wordle_secret[b]:
            return GREEN_BOX
        if wordle_guess[b] != wordle_secret[b]:
            return WHITE_BOX 
    else: 
        return ""
        
"""Place holder for wordle color boxes"""
holder: str = l(0) + l(1) + l(2) + l(3) + l(4) + l(5) + l(6) + l(7) + l(8) + l(9) + l(10) + l(11) + l(12) + l(13) + l(14) + l(15)
print(holder)

while len(wordle_guess) == len(wordle_secret):
    if wordle_guess == wordle_secret:
        print("Woo! You got it!")
        exit()
    else:
        print("Not quite. Play again soon!")
        exit()