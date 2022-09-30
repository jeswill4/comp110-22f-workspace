"""Rock-paper-scissor game."""
__author__ = "730561311"

from random import randint

points: str = ""
player: str = input("Player name: ")


def greet() -> None:
    print("ROCK-PAPER-SCISSOR\nTHE GAME")
    global player
    print(f"{player} vs MACHINE.\n{player}, type what you're thinking of - ROCK/PAPER/SCISSOR\nThen your pick will shoot against the MACHINE!")
   

def picked(user: str) -> int:
    "Converts answer of users thought (rock, paper, or scissor) into 3 numbers accordingly."
    picks: list[str] = ["ROCK", "PAPER", "SCISSOR"]
    if user == picks[0]:
        return 0
    if user == picks[1]:
        return 1
    if user == picks[2]:
        return 2

def numtostr(machine: int) -> str:
    """Converts machines random 3 numbers into correspoding rock, paper, scissor emojies."""
    ROCK =  str = "\U0000270A"
    PAPER = str = "\U0000270B"
    SCISSOR = str = "\U0000270C"
    if machine == 0:
        return ROCK
    if machine == 1:
        return PAPER
    if machine == 2:
        return SCISSOR

def winner(urnum: int, compnumb: int) -> int:
    """Uses users thoughts converted into corresponding number and machines random number. Produces Winner or Loser text and 0 or 1."""
    print(f"MACHINE SHOOTS {numtostr(compnumb)}! <--> {player} SHOOTS {numtostr(urnum)}!")
    while urnum == compnumb:
        print("AGAIN")
        urnum: int = picked(input("Thinking of ROCK or PAPER or SCISSORS: ")) 
        compnumb: int = randint(0,2)
        print(f"MACHINE SHOOTS {numtostr(compnumb)}! <--> {player} SHOOTS {numtostr(urnum)}!")

    if (urnum == 0 and compnumb == 2) or (urnum == 1 and compnumb == 0) or (urnum == 2 and compnumb == 1):
        print(f"{player} WON!!!! ")
        print("")
        return 0
    else:
        print(f"MACHINE WON!!!!")
        print("")
        return 1

def upto(neededtowin: int) -> int:
    """Uses winner function and a quantity of wins needed to produce multiple rock paper scissor games."""
    global points
    GREEN_BOX: str = "\U0001F7E9" 
    RED_BOX: str = "\U0001F7E5"
    machinewins: int = 0
    playerwins: int = 0
    while neededtowin > playerwins and neededtowin > machinewins:
        rpspick: int = picked(input("Thinking of ROCK or PAPER or SCISSORS: "))
        computernumber: int = randint(0, 2)
        if winner(rpspick, computernumber) == 0:
            playerwins += 1
            points += GREEN_BOX
        else: 
            machinewins += 1
            points += RED_BOX
    if machinewins == neededtowin:
        print(f"Nice try {player}, but you lost to MACHINE.")
        return 1
    if playerwins == neededtowin:
        print(f"{player} you're to good!")
        return 0


def best_of_one() -> None:
    """Second path. One game of rock paper scissor."""
    rpspick: int = picked(input("What are you thinking? ROCK, PAPER, or SCISSOR? "))
    computernumber: int = randint(0, 2)
    winner(rpspick, computernumber)


def best_of_three() -> None:
    """Third path. Best out of 3 games of rock paper scissor."""
    upto(2)


def best_of_seven() -> None:
    """Fourth path. Best out of 7 games of rock paper scissor."""
    upto(4)


def main() -> None:
    """Where it all starts!"""
    global points
    greet()
    pathways: int = input("Enter \"0\" for STOP, \"1\" for one game, \"3\" for best of 3, or \"7\" for best of 7: ")
    if pathways == 0:
        print(f"Your total win/loss points: {points} \nThanks for playing! Bye!!!!")
    while pathways > 0: 
        if pathways == 1:
            best_of_one()
            print(f"Your total win/loss points: {points}")
        if pathways == 3:
            best_of_three()
            print(f"Your total win/loss points: {points}")
        if pathways == 7:
            best_of_seven()
            print(f"Your total win/loss points: {points}")
        pathways: int = input("Enter \"0\" for STOP, \"1\" for one game, \"3\" for best of 3, or \"7\" for best of 7: ")
    print(f"Your total win/loss points: {points} \nThanks for playing! Bye!!!!")
    

if __name__ == "__main__":
  main()