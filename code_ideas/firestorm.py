"""FIRE STORM"""
__author__ = "Gummybear"
import random 
game: int = 100

"""Stats"""
hp: int = 100
fire: int = 10
wind: int = 1
exp: int = 0
level: int = 0

"""Duck stats"""
duckhp: int = 25
duckfire: int = 4
duckwind: int = 2

"""Goose stat"""
goosehp: int = 32
goosefire: int = 35
goosewind: int = 5

"""Albatross"""
albatrosshp: int = 64
albatrossfire: int = 25
albatrosswind: int = 3

def fight(hp: int, damage: int) -> int:
    """When someone takes damage, gives new HP."""
    new_hp = (hp - damage)
    return new_hp

def introduction() -> None:
    """Intro"""
    print(" ")
    print(" ")
    print("                  _______________")
    print("             _________________________")
    print("     __________________________________________")
    print("______________________________________________________")
    print(" ")
    print("                    Fire Storm")
    print(" ")
    print("______________________________________________________")
    print("     __________________________________________")
    print("                  _______________")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Hp represents health, fire is your attack damage, wind is your speed.")
    print("If your wind is slower than your enemy's wind, the enemy attacks first.")
    print("If your health gets below 1 you die. You will be able to add to your stats after leveling up!")

def attacks(attakers_name: str, hp: int, fire: int, wind: int, duckhp: int, duckfire: int, duckwind:int, exp: int) -> int:
    """Getting attacked"""
    print(" ")
    print(" ")
    print(f"                       Hp: {hp}   \t Fire: {fire} \t Wind: {wind}")
    print(" ")
    print(f"A {attakers_name} appears")
    print(" ")
    if attakers_name == "duck":
        print(f"                       {attakers_name} Hp: {duckhp} \t {attakers_name} Fire: {duckfire} \t {attakers_name} Wind: {duckwind}")
        print(" ")
    if attakers_name == "goose":
        print(f"                       {attakers_name} Hp: {duckhp} \t {attakers_name} Fire: {duckfire} \t {attakers_name} Wind: {duckwind}")
        print(" ")
    if attakers_name == "albatross": 
        print(f"                       {attakers_name} Hp: {duckhp} \t {attakers_name} Fire: {duckfire} \t {attakers_name} Wind: {duckwind}")
        print(" ")
    attack: str = input("Attack with \"x\"    ")
    print(" ")
    while attack != "x":
        print("You typed \"x\" wrong")
        attack: str = input("Attack with \"x\"")
        print(" ")
    if attack == "x":
        while duckhp > 0:
            if duckwind > wind:
                print(f"{attakers_name} attacks first")
                hp = fight(hp, duckfire)
                print(f"hp: {hp}")
                if hp <= 0:
                    print("Hp = 0 \tGame Over")
                    exit()
                duckhp = fight(duckhp, fire)
                print(f"{attakers_name} hp: {duckhp}")
                if duckhp <= 0:
                    print(attakers_name, " defeated")
                    exp += 1
                    return exp
            else:
                print("You attack first")
                duckhp = fight(duckhp, fire)
                print(f"{attakers_name}: {duckhp}")
                if duckhp <= 0:
                    print(attakers_name, " defeated")
                    exp += 1
                    return exp
                hp = fight(hp, duckfire)
                print(f"hp: {hp}")
                if hp <= 0:
                    print("Hp = 0 \tGame Over")
                    exit()

def lvl(exp: int, hp: int, fire: int, wind: int) -> int:
    """Leveling up!"""
    if exp > 0:
        print(" ")
        print("                         ____-------____")
        print("                        |   Level Up!   |")
        print("                         ----_______----")
        print(" ")
        up: str = input("Increase \"hp\", \"fire\", or \"wind\":    ")
        while up != "hp" and up != "fire" and up != "wind" :
            print("Your answer was not an option. Try again.")
            up: str = input("Increase \"hp\", \"fire\", or \"wind\":    ")
        if up == "hp":
            hp += 10
            print("Hp +10")
            print(" ")
            print(" ")
            return hp
        if up == "fire":
            fire += 2
            print("Fire +2")
            print(" ")
            print(" ")
            return fire
        if up == "wind":
            wind += 1
            print("Wind +1")
            print(" ")
            print(" ")
            return wind
    return 0

introduction()
exp = attacks("duck", hp, fire, wind, duckhp, duckfire, duckwind, exp)
levelup = lvl(exp, hp, fire, wind)
if levelup == (hp + 10):
    hp += 10
    exp = 0
    level += 1
if levelup == (fire + 2):
    fire += 2
    exp = 0
    level += 1
if levelup == (wind + 1):
    wind += 1
    exp = 0
    level += 1
print("V    You're good at beating up afflack! Embrace the inferno and go deeper    V")
print(f"                Level: {level} Hp: {hp} Fire: {fire} Wind: {wind}")
for round in range(game):
    print(" ")
    answered: str = input("Do you want to continue? \"enter\" for yes and anything else for no:    ")
    if answered == "":
        if level < 3:
            exp = attacks("duck", hp, fire, wind, duckhp + (random.randint(0,5)), duckfire +  (random.randint(0,3)), duckwind + (random.randint(-2, 1)), exp)
            levelup = lvl(exp, hp, fire, wind)
            if levelup == (hp + 10):
                hp += 10
                exp = 0
                level += 1
            if levelup == (fire + 2):
                fire += 2
                exp = 0
                level += 1
            if levelup == (wind + 1):
                wind += 1
                exp = 0
                level += 1
        if level >= 3 and level < 6:
            exp = attacks("goose", hp, fire, wind, (goosehp + (random.randint(0,3))), (goosefire + (random.randint(0,1))), (goosewind + (random.randint(-2, 1))), exp)
            levelup = lvl(exp, hp, fire, wind)
            if levelup == (hp + 10):
                hp += 10
                exp = 0
                level += 1
            if levelup == (fire + 2):
                fire += 2
                exp = 0
                level += 1
            if levelup == (wind + 1):
                wind += 1
                exp = 0
                level += 1
        if level >= 6:
            exp = attacks("albatross", hp, fire, wind, (albatrosshp + (random.randint(0,5))), (albatrossfire + (random.randint(0,4))), (albatrosswind + (random.randint(-2, 1))), exp)
            levelup = lvl(exp, hp, fire, wind)
            if levelup == (hp + 10):
                hp += 10
                exp = 0
                level += 1
            if levelup == (fire + 2):
                fire += 2
                exp = 0
                level += 1
            if levelup == (wind + 1):
                wind += 1
                exp = 0
                level += 1
        print(f"Level: {level} Hp: {hp} Fire: {fire} Wind: {wind}")
    if answered != "":
        exit()