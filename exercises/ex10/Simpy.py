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
    
    def sum(self) -> float:
        """Return sum of floats in attribute values."""
        final_sum: float = 0.0
        for item in self.values:
            final_sum += item
        return final_sum
    
    def __add__(self, u: Union[Simpy, float]) -> Simpy:
        """Lets you use + in conjuction with Simpy objects and floats."""
        new_simpy: Simpy = Simpy([])
        if isinstance(u, float):
            for item in self.values:
                new_simpy.values.append(item + u)
        else:
            assert len(self.values) == len(u.values)
            for i in range(len(self.values)):
                new_simpy.values.append(self.values[i] + u.values[i])
        return new_simpy

    def __pow__(self, u: Union[Simpy, float]) -> Simpy:
        """Lets you use ** in conjuction with Simpy objects and floats."""
        power: Simpy = Simpy([])
        if isinstance(u, float):
            for item in self.values:
                power.values.append(item ** u)
        else:
            assert len(self.values) == len(u.values)
            for i in range(len(self.values)):
                power.values.append(self.values[i] ** u.values[i])
        return power
    
    def __eq__(self, u: Union[Simpy, float] ) -> list[bool]:
        """Produce mask/ list[bool] based on equality of each item in values attribute of another Simpy/float."""
        mask: list[bool] = []
        if isinstance(u, float):
            for item in self.values:
                if item == u:
                    mask.append(True)
                else:
                    mask.append(False)
        else: 
            assert len(self.values) == len(u.values)
            for i in range(len(self.values)):
                if self.values[i] == u.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __gt__(self, u: Union[Simpy, float]) -> list[bool]:
        """Produce list[bool] based on greater than of each item in values attribute of another Simpy/float."""
        greater: list[bool] = []
        if isinstance(u, float):
            for item in self.values:
                if item >= u:
                    greater.append(True)
                else:
                    greater.append(False)
        else:
            assert len(self.values) == len(u.values)
            for i in range(len(self.values)):
                if self.values[i] >= u.values[i]:
                    greater.append(True)
                else:
                    greater.append(False)
        return greater
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription of Simpy objects, can call specific floats in values."""
        if isinstance(rhs, int):
            number = self.values[rhs]
        elif isinstance(__gt__): 
            number: Simpy = Simpy([])
            if rhs == self:
                number.values.append()
        else:
            number: Simpy = Simpy([])
            if self > rhs:
                number.values.append()


        return number
        