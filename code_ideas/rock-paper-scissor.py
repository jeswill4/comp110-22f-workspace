"""Rock-paper-scissor game."""

print("ROCK-PAPER-SCISSORS\nTHE GAME")
username: str = input("Player name: ")
print(f"{username} vs MACHINE.\n{username}, type what you're thinking of - ROCK/PAPER/SCISSORS\nThen your pick will shoot against the MACHINE")
picks: list[str] = ["ROCK", "PAPER", "SCISSORS"]


def picked(user: str) -> int:
    if user == picks[0]:
        return 0
    if user == picks[1]:
        return 1
    if user == picks[2]:
        return 2

def numtostr(machine: int) -> str:
    if machine == 0:
        return picks[0]
    if machine == 1:
        return picks[1]
    if machine == 2:
        return picks[2]

def winner(urnum: int, compnumb: int) -> str:
    print(f"MACHINE SHOOTS {numtostr(compnumb)}! <--> {username} SHOOTS {numtostr(urnum)}!")
    computernumber: int = compnumb
    while picked == computernumber:
        print("AGAIN")
        picked(input("Thinking of ROCK or PAPER or SCISSORS: "))
        computernumber: int = randint(0,2)
        print(f"MACHINE SHOOTS {numtostr(computernumber)}! <--> {username} SHOOTS {numtostr(picked)}!")

    if (picked == 0 and computernumber == 2) or (picked == 1 and computernumber == 0) or (picked == 2 and computernumber == 1):
        print(f"{username} WON!!!! ")
    else:
        print(f"MACHINE WON!!!!")
    

picked(input("What are you thinking? ROCK, PAPER, or SCISSORS? Type exactly the same way, all capatilized letters: "))
from random import randint
computernumber: int = randint(0, 2)
winner(picked, computernumber)

    