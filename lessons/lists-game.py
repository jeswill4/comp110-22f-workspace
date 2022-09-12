"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item
# print(rolls[0])
# print(rolls[1])
# print(rolls[3])
# # Access the length of a list (number of items)
# print(len(rolls))

#  # Acces the last item of a list
# print(rolls[len(rolls) - 1])
# # or make a variable
# last_index: int = len(rolls) - 1
# print(rolls[last_index])