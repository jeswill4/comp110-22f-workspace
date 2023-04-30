"""FIRE STORM"""
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

def duck(stat: str) -> int:
    """Gives stat desired"""
    if stat == "hp":
        return duckhp
    if stat == "fire":
        return duckfire
    if stat == "wind":
        return duckwind

def fight(hp: int, damage: int) -> int:
    """When someone takes damage, gives new HP."""
    new_hp = (hp - damage)
    return new_hp

def introduction(hp: int, fire: int, wind:int) -> None:
    print("Fire Storm")
    print("Hp represents health, fire is your attack damage, wind is your speed. If your wind is slower than your enemy's wind, the enemy attacks first. If your health gets below 1 you die. You will be able to add to your stats after leveling up!")
    print(f"Hp: {hp} \t Fire: {fire} \t Wind: {wind} ")
    attacks("duck", hp, fire, wind)

def attacks(attakers_name: str, hp: int, fire: int, wind: int) -> int:

    print(f"{attakers_name} appears")
    if attakers_name == "duck":
        print("Hp:", duck("hp"), "Fire: ", duck("fire"), "Wind:", duck("wind"))
        attack: str = input("Attack with \"x\"")
        while attack != "x":
            print("You typed \"x\" wrong")
            attack: str = input("Attack with \"x\"")
        if attack == "x":
            while duck("hp") > 0:
                if duck("wind") > wind:
                    print(f"{attakers_name} attacks first")
                    hp = fight(hp, duck("fire"))
                    print(hp)
                    if hp < 1:
                        print("Hp = 0 \tGame Over")
                        exit()
                    duckhp = fight(duck("hp"), fire)
                    print(duckhp)
                    if duckhp == 0:
                        print(attakers_name, " defeated")
                        return hp 
                else:
                    print("You attack first")
                    duckhp = fight(duck("hp"), fire)
                    print(duckhp)
                    if duckhp == 0:
                        print(attakers_name, " defeated")
                        return hp
                    hp = fight(hp, duck("fire"))
                    print(hp)
                    if hp < 1:
                        print("Hp = 0 \tGame Over")
                        exit()

for round in range(game):
    introduction(hp, fire, wind)
    hp = attacks("duck", hp, fire, wind)
    continues: str = input("Would you like to continue or save? Type \"c\" or \"s\"")
    if continues == "c":
        hp = attacks("duck", hp, fire, wind)
    if continues == "s":
        print("Saved")