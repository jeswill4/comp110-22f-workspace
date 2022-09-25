"""Rock-paper-scissor game."""

print("ROCK-PAPER-SCISSORS\nTHE GAME")
username: str = input("Player name: ")
print(f"{username} vs MACHINE.\n{username}, type what you're thinking of - ROCK/PAPER/SCISSORS\nThen your pick will shoot against the MACHINE")
picks: list[str] = ["ROCK", "PAPER", "SCISSORS"]

def picked(user: str) -> str:
    if picks[0] == user:
        return 0
    if picks[1] == user:
        return 1
    if picks[2] == user:
        return 2


def winner(urnum: int, compnumb: int) -> str:
    if urnum == 0:
        thought: str = picks[0]
    if urnum == 1:
        thought: str = picks[1]
    if urnum == 2:
        thought: str = picks[2]
    if compnumb == 0:
        comppick: str = picks[0]
    if compnumb == 1:
        comppick: str = picks[1]
    if compnumb == 2:
        comppick: str = picks[2]
    print(f"MACHINE SHOOTS {comppick}! <--> {username} SHOOTS {thought}!")
    while urnum == compnum:
        print("AGAIN")
        picked(input("Thinking of ROCK or PAPER or SCISSORS: "))
        compnum: int = randint(0,2)
        if urnum == 0:
            thought: str = picks[0]
        if urnum == 1:
            thought: str = picks[1]
        if urnum == 2:
            thought: str = picks[2]
        if compnumb == 0:
            comppick: str = picks[0]
        if compnumb == 1:
            comppick: str = picks[1]
        if compnumb == 2:
            comppick: str = picks[2]
        print(f"MACHINE SHOOTS {comppick}! <--> {username} SHOOTS {thought}!")

    if (urnum == 0 and compnum == 2) or (urnum == 1 and compnum == 0) or (urnum == 2 and compnum == 1):
        print(f"{username} WON!!!! ")
    else:
        print(f"MACHINE WON!!!!")
    

picked(input("What are you thinking? ROCK, PAPER, or SCISSORS? Type exactly the same way, all capatilized letters: "))
from random import randint
compnum: int = randint(0,2)    
winner(picked, compnum)
if input("To replay, press 0 and enter: ") == 0:
    replay: int = 0 
while replay == 0:
    picked(input("What are you thinking? ROCK, PAPER, or SCISSORS: "))
    from random import randint
    compnum: int = randint(0,2)    
    winner(picked, compnum)
    if input("To replay, press 0 and enter: ") == 0:
        replay: int = 0 
    elif input("So you don't want to play again :( or did you type 0 wrong and not press enter correctly? Try again if so: ") == 0:
        replay: int = 0
    else: 
        replay: int = 1