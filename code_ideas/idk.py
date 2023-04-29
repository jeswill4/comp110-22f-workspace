"""Make a game."""
__author__ = "Gummybear"

game: int = 1

"""Stats"""
hp: int = 100
fire: int = 10
wind: int = 1

"""Duck stats"""
duckhp: int = 25
duckfire: int = 4
duckwind: int = 2
def duck(what_needed: str) -> int:
    if what_needed == "hp":
        return duckhp
    if what_needed == "fire":
        return duckfire
    if what_needed == "wind":
        return duckwind


"""Intro"""
print("Fire Storm")
print("Hp represents health, fire is your attack damage, wind is your speed. If your wind is slower than your enemy's wind, the enemy attacks first. If your health gets below 1 you die. You will be able to add to your stats after leveling up!")

print(f"Hp: {hp} \t Fire: {fire} \t Wind: {wind} ")
print("Duck appears")




def attacks(attakers_name) -> str:
    attack: str = input("Attack with \"x\"")
    while attack != "x":
        print("You typed \"x\" wrong")
        attack: str = input("Attack with \"x\"")
    if attack == "x":
        if attakers_name("wind") > wind:
            print(f"{attakers_name} attacks first")
            hp -= attakers_name("fire")
            if hp < 1:
                print("Hp = 0 \tGame Over")
                exit()
        else:
            print("You attack first")
            attackers_hp = attakers_name("hp") - fire


for round in range(game):
    print(f"Hp: {hp} \t Fire: {fire} \t Wind: {wind} ")
    continues: str = input("Would you like to continue or save? Type \"yes\" or \"no\"")
    if continues == "yes":
        print("yeah")