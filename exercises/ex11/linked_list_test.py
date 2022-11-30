"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730561311"


def test_last_empty() -> None:
    """Last of an empty linked list should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)



def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3



def test_value_at_none() -> None:
    """Value_at of an empty index number should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(Node(10, Node(20, Node(30, None))), 3)



def test_value_at_index() -> None:
    """Value_at of a given node and index should return the data of the node at that index."""
    assert value_at(Node(10, Node(20, Node(30, None))), 0) == 10
    assert value_at(Node(10, Node(20, Node(30, None))), 1) == 20
    assert value_at(Node(10, Node(20, Node(30, None))), 2) == 30



def test_max_nothing() -> None:
    """Max with None for Node should raise ValueError."""
    with pytest.raises(ValueError):
        max(None)



def test_max_something() -> None:
    """Max with given list of should return biggest data within."""
    assert max(Node(10, Node(20, Node(30, None)))) == 30
    assert max(Node(10, Node(30, Node(20, None)))) == 30
    assert max(Node(30, Node(20, Node(10, None)))) == 30



def test_linkify_no_first_number() -> None:
    """No first number in colon."""
    items: list[int] = [10, 20, 30, 40]
    assert linkify(items[:3]) == [10, 20, 30]


def test_linkify_both() -> None:
    """Should return correlated indexes forming a new Node list."""
    items: list[int] = [10, 20, 30, 40]
    assert linkify(items[1:4]) == [20, 30, 40]