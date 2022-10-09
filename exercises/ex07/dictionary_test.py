"""Test of dictionary exercise 07."""

__author__ = "730561311"

from dictionary import invert, count, favorite_color
from exercises.ex07.dictionary import favorite_color

def test_invert_calender() -> None:
    """Inverting month with day. """
    my_dictionary = {"December": "25th", "April": "4th", "October": "31st"}
    invert(my_dictionary)


def test_favorite_color_tie() -> None:
    """Test tie situation of favorite color counts. Should return first color mentioned in the tie."""
    my_dictionary = {"Jesse": "orange", "Albert": "orange", "Miguel": "blue", "DJ" : "blue"}
    favorite_color(my_dictionary)


def test_count_nothing() -> None:
    """Using count defintion but with no inputs."""
    my_dictionary = {}
    count(my_dictionary)