"""EX03 - Wordle. It's wordle time!!!!"""
__author__ = "730561311"
"""Use lots of functions: main, input_guess, emojified, and contains_char"""
wordle_secret: str = "codes"


def contains_char(secrets: str, letter_checked: str) -> bool:
    """First str secrets is the word people are trying to guess."""
    """Second string is one letter from wordle guess/ persons guessed word that they typed in."""
    """ Returns True if the wordle guessed letter is in it and if not False."""
    assert len(letter_checked) == 1
    i: int = 0
    while i < len(secrets):
        if letter_checked == secrets[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Colored block output. Green is correct, white incorrect, yellow wrong place."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8" 
    magic_bubbles: str = ""
    i: int = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            magic_bubbles += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            magic_bubbles += YELLOW_BOX
        else:
            magic_bubbles += WHITE_BOX
        i += 1
    return magic_bubbles


def input_guess(expected_length: int) -> str:
    """Expected number of letters in guess made by player."""
    wordle_guess: str = input(f"Enter a {len(wordle_secret)} character word: ")
    while len(wordle_guess) != expected_length:
        wordle_guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
    return wordle_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    while i <= 6: 
        print(f"=== Turn {i}/6 ===")
        wordle_guess: str = input_guess(len(wordle_secret))
        print(emojified(wordle_guess, wordle_secret))
        if wordle_guess == wordle_secret:
            return print(f"You won in {i}/6 turns!")
        i += 1
    return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()