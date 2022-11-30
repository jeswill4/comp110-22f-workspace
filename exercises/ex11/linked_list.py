"""Utility functions fro working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730561311"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Contruct a singly linked list. Use None for 2nd argument if fail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualizaiton of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a linked list, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None.")
    elif head.next is None:
        return head.data 
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of a Node at the given index of the head parameter."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data 
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Returns the maximum data value in the liked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    if head.next is None:
        return head.data
    maximum: int = max(head.next)
    if head.data > maximum:
        return head.data
    else:
        return maximum


def linkify(items: list[int]) -> Optional[Node]:
    """Given items make and return optional node."""
    head: Optional[Node] = []
    if len(items) == 0:
        return head
    else:
        head.append(items)
        linkify(items - head[0])


def scale():
    return None

