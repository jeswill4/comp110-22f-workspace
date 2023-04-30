"""FIRE STORM"""
__author__ = "Gummybear"
game: int = 10

"""Stats"""
hp: int = 100
fire: int = 10
wind: int = 1
exp: int = 0

"""Duck stats"""
duckhp: int = 25
duckfire: int = 4
duckwind: int = 2

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
    print(f"               Hp: {hp}   \t Fire: {fire} \t Wind: {wind}")
    print(" ")
    print(f"A {attakers_name} appears")
    print(" ")
    if attakers_name == "duck":
        print(f"               Duck Hp: {duckhp} \t Duck Fire: {duckfire} \t Duck Wind: {duckwind}")
    attack: str = input("Attack with \"x\"    ")
    while attack != "x":
        print("You typed \"x\" wrong")
        attack: str = input("Attack with \"x\"")
    if attack == "x":
        while duckhp > 0:
            if duckwind > wind:
                print(f"{attakers_name} attacks first")
                hp = fight(hp, duckfire)
                print(f"hp: {hp}")
                if hp < 1:
                    print("Hp = 0 \tGame Over")
                    exit()
                duckhp = fight(duckhp, fire)
                print(f"duck hp: {duckhp}")
                if duckhp < 0:
                    print(attakers_name, " defeated")
                    exp += 1
                    return exp
            else:
                print("You attack first")
                duckhp = fight(duckhp, fire)
                print(f"duck hp: {duckhp}")
                if duckhp < 0:
                    print(attakers_name, " defeated")
                    exp += 1
                    return exp
                hp = fight(hp, duckfire)
                print(f"hp: {hp}")
                if hp < 1:
                    print("Hp = 0 \tGame Over")
                    exit()

def lvl(exp: int, hp: int, fire: int, wind: int) -> int:
    if exp > 0:
        print(" ")
        print(" ")
        print("                    Level Up!")
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
if levelup == (fire + 2):
    fire += 2
    exp = 0
if levelup == (wind + 1):
    wind += 1
    exp = 0
print("V    You're good at beating up afflack! Embrace the inferno and go deeper    V")
print(f"Exp: {exp} Hp: {hp} Fire: {fire} Wind: {wind}")
for round in range(game):
    answered: str = input("Do you want to continue? \"y\" for yes and anything else for no:    ")
    while answered != "y":
        print("You typed your answer wrong. Try again.")
        answered = input("Do you want to continue? \"y\" for yes and anythign else for no:    ")
    if answered == "y":
        exp = attacks("duck", hp, fire, wind, duckhp, duckfire, duckwind, exp)
        levelup = lvl(exp, hp, fire, wind)
        if levelup == (hp + 10):
            hp += 10
            exp = 0
        if levelup == (fire + 2):
            fire += 2
            exp = 0
        if levelup == (wind + 1):
            wind += 1
            exp = 0
        print(f"Exp: {exp} Hp: {hp} Fire: {fire} Wind: {wind}")
    if answered != "y":
        exit()