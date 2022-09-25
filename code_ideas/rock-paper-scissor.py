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

def winner(urnum: int, compnumb: int) -> int:
    print(f"MACHINE SHOOTS {numtostr(compnumb)}! <--> {username} SHOOTS {numtostr(urnum)}!")
    while urnum == compnumb:
        print("AGAIN")
        urnum: int = picked(input("Thinking of ROCK or PAPER or SCISSORS: ")) 
        compnumb: int = randint(0,2)
        print(f"MACHINE SHOOTS {numtostr(compnumb)}! <--> {username} SHOOTS {numtostr(urnum)}!")

    if (urnum == 0 and compnumb == 2) or (urnum == 1 and compnumb == 0) or (urnum == 2 and compnumb == 1):
        print(f"{username} WON!!!! ")
        return 0
    else:
        print(f"MACHINE WON!!!!")
        return 1
    
rpspick: int = picked(input("What are you thinking? ROCK, PAPER, or SCISSORS? Type exactly the same way, all capatilized letters: "))
from random import randint
computernumber: int = randint(0, 2)
winner(rpspick, computernumber)

if input(f"{username} do you want to play a best out of 3? YES or NO: ") == "YES":
    machinewins: int = 0
    playerwins: int = 0
    while machinewins < 2 or playerwins < 2:
        rpspick: int = picked(input("Thinking of ROCK or PAPER or SCISSORS: "))
        computernumber: int = randint(0, 2)
        if winner(rpspick, computernumber) == 0:
            playerwins += 1
        else: 
            machinewins += 1
    if machinewins == 2:
        print(f"Nice try {username}, but you lost to MACHINE.")
    if playerwins == 2:
        print(f"{username} you're to good!")



    