"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale, is_equal

__author__ = "730561311"


def test_last_empty() -> None:
    """Last of an empty linked list should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_lis = Node(1, Node(2, Node(3, None)))
    assert last(linked_lis) == 3


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
    items: list[int] = [10, 20, 30]
    links: Node = (Node(10, Node(20, Node(30, None))))
    assert is_equal(linkify(items), links)


def test_linkify_both() -> None:
    """Should return correlated indexes forming a new Node list."""
    item: list[int] = [10, 20]
    link_list: Node = (Node(10, Node(20, None)))
    assert is_equal(linkify(item), link_list)


def test_scale_factors_with_linkify() -> None:
    """Should multiply every linked data by factor."""
    scale(linkify([1, 2, 3]), 2)


def test_scale_normal() -> None:
    """Should multiply every linked data by factor."""
    first_link: Node = Node(1, Node(2, Node(3, Node(4, None))))
    second_link: Node = Node(4, Node(8, Node(12, Node(16, None))))
    assert is_equal(scale(first_link, 4), second_link)
