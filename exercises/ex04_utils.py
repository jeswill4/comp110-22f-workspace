"""Putting utils to use in exercise."""
__author__ = "730561311"


def all(listy: list[int], searchy: int) -> bool:
    """Function all used to search number and check to see if list contains only that number. True/False."""
    i: int = 0 
    if len(listy) == 0:
        return False
    while i < len(listy):
        if listy[i] != searchy:
            return False
        i += 1
    return True 


def max(input: list[int]) -> int:
    """Function max returns largest integar in list. If empty return Value Error."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum_num: int = input[0]
    i: int = 0
    while i < len(input):
        if input[i] > maximum_num:
            maximum_num: int = input[i]
        i += 1
    return maximum_num


def is_equal(listy: list[int], input: list[int]) -> bool:
    """Finding if two lists are equal in each index."""
    if len(listy) != len(input):
        return False
    i: int = 0
    if len(listy) == len(input):
        while i < len(listy):
            if listy[i] != input[i]:
                return False
            i += 1
    return True