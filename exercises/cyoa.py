"""Rock-paper-scissor game."""
__author__ = "730561311"

from random import randint

points: str = ""
player: str = input("Player name: ")
total_wins: int = 0
total_games: int = 0


def greet() -> None:
    print("ROCK-PAPER-SCISSOR\nTHE GAME")
    global player
    print(f"{player} vs MACHINE.\n{player}, type what you're thinking of - ROCK/PAPER/SCISSOR\nThen your pick will shoot against the MACHINE!")
   

def picked(user: str) -> int:
    "Converts answer of users thought (rock, paper, or scissor) into 3 numbers accordingly."
    picks: list[str] = ["ROCK", "PAPER", "SCISSOR"]
    if user == picks[0]:
        return 0
    elif user == picks[1]:
        return 1
    elif user == picks[2]:
        return 2
    else: 
        return 3


def numtostr(machine: int) -> str:
    """Converts 3 numbers into correspoding rock, paper, scissor emojies."""
    ROCK =  str = "\U0000270A"
    PAPER = str = "\U0000270B"
    SCISSOR = str = "\U0000270C"
    if machine == 0:
        return ROCK
    if machine == 1:
        return PAPER
    if machine == 2:
        return SCISSOR
    if machine == 3:
        return "nothing"


def winner(urnum: int, compnumb: int) -> int:
    """Uses users thoughts converted into corresponding number and machines random number. Produces Winner or Loser text and 0 or 1. Also, adds yellow to points if a tie happens."""
    global points, tie_master_achievement
    YELLOW_BOX: str = "\U0001F7E8"
    print(f"MACHINE SHOOTS {numtostr(compnumb)}! <--> {player} SHOOTS {numtostr(urnum)}!") 
    while urnum == compnumb:
        points += YELLOW_BOX
        print("AGAIN")
        urnum: int = picked(input("Thinking of ROCK or PAPER or SCISSOR: ")) 
        compnumb: int = randint(0,2)
        print(f"MACHINE SHOOTS {numtostr(compnumb)}! <--> {player} SHOOTS {numtostr(urnum)}!")

    if (urnum == 0 and compnumb == 2) or (urnum == 1 and compnumb == 0) or (urnum == 2 and compnumb == 1):
        print(f"{player} WON!!!!\n")
        return 0
    else:
        print(f"MACHINE WON!!!!\n")
        return 1


def upto(neededtowin: int) -> int:
    """Uses winner function and a quantity of wins needed to produce multiple rock paper scissor games."""
    global points, total_games, total_wins
    machine_wins: int = 0
    player_wins: int = 0
    GREEN_BOX: str = "\U0001F7E9" 
    RED_BOX: str = "\U0001F7E5"
    while neededtowin > player_wins and neededtowin > machine_wins:
        rpspick: int = picked(input("Thinking of ROCK or PAPER or SCISSOR: "))
        computernumber: int = randint(0, 2)
        if winner(rpspick, computernumber) == 0:
            player_wins += 1
            total_wins += 1
            total_games += 1
            points += GREEN_BOX
        else: 
            machine_wins += 1
            total_games += 1
            points += RED_BOX
    if machine_wins == neededtowin:
        print(f"Nice try {player}, but you lost to MACHINE.")
        return total_games and total_wins
    if player_wins == neededtowin:
        print(f"{player} you're to good!")
        return total_games and total_wins


def best_of_one() -> None:
    """Second path. One game of rock paper scissor. Counts player_wins/games."""
    upto(1)
    print(f"Your points: {points}\nWins/total games - {total_wins}/{total_games}")
    

def best_of_three() -> None:
    """Third path. Best out of 3 games of rock paper scissor. Counts player_wins/games."""
    upto(2)
    print(f"Your points: {points}\nWins/total games - {total_wins}/{total_games}")


def best_of_seven() -> None:
    """Fourth path. Best out of 7 games of rock paper scissor. Counts player_wins/games."""
    upto(4)
    print(f"Your points: {points}\nWins/total games - {total_wins}/{total_games}")


def tie_award() -> bool:
    """Tracks MIND READER achievement. Have to have a total of 5 ties and 3 in a row followed by a win."""
    global points
    i: int = 0
    in_a_row: int = 0
    while i < len(points):
        if points[i] == "\U0001F7E8":
            in_a_row += 1
        if points[i] == "\U0001F7E5":
            in_a_row == 0
        if in_a_row >= 3 and points[i + 1] == "\U0001F7E9":
            return True
        i += 1
    return False

def tie_award_two() -> bool:
    """Tracks MIND READER achievement. Have to have a total of 5 ties and 3 in a row followed by a win."""
    global points
    i: int = 0
    in_a_row: int = 0
    while i < len(points):
        if points[i] == "\U0001F7E8":
            in_a_row += 1
        if points[i] == "\U0001F7E5":
            in_a_row == 0
        if in_a_row >= 7 and points[i + 1] == "\U0001F7E9":
            return True
        i += 1
    return False


def loser_award() -> bool:
    """Tracks MACHINE DOMINATION achievement. Machine wins total of 5 times in a row."""
    global points
    i: int = 0
    in_a_row: int = 0
    while i < len(points):
        if points[i] == "\U0001F7E5":
            in_a_row += 1
        if points[i] == "\U0001F7E9":
            in_a_row == 0
        if in_a_row >= 5:
            return True
        i += 1
    return False


def winner_award() -> bool:
    """Tracks PLAYER DOMINATION achievement. Player wins a total of 5 times or more in a row."""
    global points
    i: int = 0
    in_a_row: int = 0
    while i < len(points):
        if points[i] == "\U0001F7E5":
            in_a_row == 0
        if points[i] == "\U0001F7E9":
            in_a_row += 1
        if in_a_row >= 5:
            return True
        i += 1
    return False


def achievement_tracked() -> None:
    global player
    if tie_award() is True:
        print("\nACHIEVEMENT - MIND READER\n----Tie +3 times or more in row and win----")
    if tie_award_two() is True:
        print("\nACHIEVEMENT - MACHINE INTERPRETER\n----Tie +7 times or more in row and win----")
    if loser_award() is True:
        print("\nACHIEVEMENT - MACHINE DOMINATION\n----Lose +5 times or more in a row----")
    if winner_award() is True:
        print(f"\nACHIEVEMENT - {player} DOMINATION\n----Win +5 times or more in a row----")


def main() -> None:
    """Where it all starts!"""
    greet()
    pathways: str = input("Enter \"0\" for STOP, \"1\" for one game, \"3\" for best of 3, or \"7\" for best of 7: ")
    while pathways != "0": 
        if pathways == "1":
            best_of_one()
        if pathways == "3":
            best_of_three()
        if pathways == "7":
            best_of_seven()
        pathways: int = input("Enter \"0\" for STOP, \"1\" for one game, \"3\" for best of 3, or \"7\" for best of 7: ")
    achievement_tracked()
    print(f"Your total points: {points}\nWins/total games - {total_wins}/{total_games}\nThanks for playing!")


if __name__ == "__main__":
  main()