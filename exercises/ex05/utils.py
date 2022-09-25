"""Utils 1 of 2 files in exercise 05."""
__author__ = "730561311"

def only_evens(wholelist: list[int]) -> list[int]:
    """Takes a list of numbers and outputs a newlist of any even numbers from that list."""
    i: int = 0
    while i < len(wholelist):
        if wholelist[i] == 2:
            newlist: list[int] = list()
            newlist.append(wholelist[i])
        i += 1
    return newlist

def concat(firstlist: list[int], secondlist: list[int]) -> list[int]:
    """Given two list this concat function combines them."""
    completelist: list[int] = list()
    completelist.append(firstlist, secondlist)
    return completelist

def sub(finallist: list[int], startnum: int, endnum: int) -> list[int]:
    """Generates new list that doesn't have numbers before start and numbers after end."""
    finallylist: list[int] = list()
    if len(finallist) == 0 or startnum > len(finallist) or endnum <= 0:
        return finallylist
    finallylist.append(finallist)
    if startnum > -1:
        finallylist.pop(startnum - 1)
    if endnum <= len(finallist):
        finallylist.pop(endnum - 1)

    return finallylist
