"""Utils testing file 2 of 2 files in exercise 05."""
__author__ = "730561311"

from utils import only_evens, sub, concat


def test_list_output_even() -> None:
    """Testing (only_evens) to see if the function when given a list only outputs numbers that are even from that list."""
    mylistex: list[int] = [33, 8, -2, 92, 7, 4, 10]
    assert only_evens(mylistex)


def test_if_startnumber_0() -> None:
    """Testing sub to see if it creates a new list from given, that starts and ends with given numbers."""
    assert sub([1, 2, 5], 0, 0)


def test_if_greater_than_list() -> None:
    """Testing sub for a negative starting number and an end number greater than the list, to see if it give back the correct list."""
    assert sub([4, 6, 7, 8], -1, 6) 


def test_normal_values() -> None:
    """Using values in list parameters "normal" values. """
    assert sub([8, 42, 4, 10], 1, 3)


def test_concat_emptylist_and_more() -> None:
    """Testing to combine two lists together."""
    unolist: list[int] = []
    doslist: list[int] = []
    assert concat(unolist, doslist)


def test_concat_normal_oneint_list() -> None:
    """Concating two list with only one integer."""
    firstlist: list[int] = [1]
    secondlist: list[int] = [2]
    assert concat(firstlist, secondlist)


def test_concat_first_empty() -> None:
    """Concating an empty list with a normal list."""
    onelist: list[int] = []
    twolist: list[int] = [1, 2]
    assert concat(onelist, twolist)


def test_concat_second_empty() -> None:
    """Concating one list to an empty list."""
    listlist: list[int] = [1, 2]
    listylisty: list[int] = []
    assert concat(listlist, listylisty)


def test_concat_unique_lenghts() -> None:
    """Concating unique length lists together."""
    unique: list[int] = [1, 5, 6]
    numberlist: list[int] = [2]
    assert concat(unique, numberlist)