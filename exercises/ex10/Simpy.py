"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730561311"


class Simpy:
    values: list[float]
    

    def __init__(self, items: list[float]):
        """Constructor that takes a list[float] and initializes it to values attribute."""
        self.values = items
    
    def __repr__(self) -> str:
        """Returns str, used when Simpy is converted to str."""
        return f"Simpy({self.values})"
    
    def fill(self, filling: float, num: int) -> None:
        """Fill a simpy's values with a float (filling) num times."""
        while len(self.values) < num:
            self.values.append(filling)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values attribute with a range of float values."""
        assert step != 0.0
        if step > 0: 
            current: float = start
            while current < stop: 
                self.values.append(current)
                current += step
        else: 
            current: float = start
            while current > stop:
                self.values.append(current)
                current += step

