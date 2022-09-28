"""Utils testing file 2 of 2 files in exercise 05."""
__author__ = "730561311"

from utils import only_evens, sub, concat


def test_list_output_even() -> None:
    """Testing (only_evens) to see if the function when given a list only outputs numbers that are even from that list."""
    mylistex: list[int] = [33, 8, -2, 92, 7, 4, 10]
    assert only_evens(mylistex)


def test_if_startnumber_1() -> None:
    """Testing sub to see if it creates a new list from given, that starts and ends with given numbers."""
    assert sub([1, 2, 3], 1, 2)


def test_concat_emptylist_and_more() -> None:
    """Testing to combine two lists together."""
    unolist: list[int] = []
    doslist: list[int] = []
    assert concat(unolist, doslist)