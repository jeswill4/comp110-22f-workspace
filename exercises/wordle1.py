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

i: int = 0 
holder_emoji: str = ""
while i < number_of_letters:
    if wordle_guess[i] == wordle_secret[i]:
        holder_emoji = holder_emoji + GREEN_BOX
    if wordle_guess[i] != wordle_secret[i]:
        never_in: bool = False
        alternatives: int = 0 
        while never_in == False and alternatives < number_of_letters:
            if wordle_guess[i] == wordle_secret[alternatives]:
                never_in: bool = True
            else:
                alternatives = alternatives + 1
        if never_in == False:
            holder_emoji = holder_emoji + WHITE_BOX
        else:
            holder_emoji = holder_emoji + YELLOW_BOX
    i = i + 1

if i == number_of_letters:
    print(holder_emoji)

while len(wordle_guess) == len(wordle_secret):
    if wordle_guess == wordle_secret:
        print("Woo! You got it!")
        exit()
    else:
        print("Not quite. Play again soon!")
        exit()
