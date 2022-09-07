"""One shot wordle, get one guess to guess secret word python."""
__author__ = 730561311

"""Most of my variable are in this section. Also input for wordle guess, and a check to make sure its the same amount of letters."""
wordle_secret: str = "python"
number_of_letters: int = len(wordle_secret)
wordle_guess: str = input(f"What is your { number_of_letters }-letter guess? ")
while len(wordle_guess) < len(wordle_secret) or len(wordle_guess) > len(wordle_secret): 
    wordle_guess: str = input (f"That is not { number_of_letters } letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""While loop for saving correct emojis to corresponding guessed letters into string."""
i: int = 0 
holder_emoji: str = ""
while i < number_of_letters:
    if wordle_guess[i] == wordle_secret[i]:
        holder_emoji = holder_emoji + GREEN_BOX
    if wordle_guess[i] != wordle_secret[i]:
        holder_emoji = holder_emoji + WHITE_BOX
    i = i + 1

"""Big magic of printing out the emojis we stored for each letter."""
if i == number_of_letters:
    print(holder_emoji)
"""Finishing touch to tell the player they either guessed the word correctly or not."""
while len(wordle_guess) == len(wordle_secret):
    if wordle_guess == wordle_secret:
        print("Woo! You got it!")
        exit()
    else:
        print("Not quite. Play again soon!")
        exit()