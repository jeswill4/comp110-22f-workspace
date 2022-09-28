"""Utils testing file 2 of 2 files in exercise 05."""
__author__ = "730561311"

from utils import only_evens, sub, concat


def test_list_output_even() -> None:
    """Testing (only_evens) to see if the function when given a list only outputs numbers that are even from that list."""
    mylistex: list[int] = [33, 8, -2, 92, 7, 4, 10]
    assert only_evens(mylistex)


def test_if_startnumber_is_one() -> None:
    """Testin sub to see if it creates a new list from given, that starts and ends with given numbers."""
    assert sub([8, 42, 4, 10], 1, 3)


def test_concat_emptylist() -> None:
    """Testing to combine two lists together."""
    unolist: list[int] = []
    doslist: list[int] = []
    assert concat(unolist, doslist)