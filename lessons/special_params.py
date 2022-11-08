"""Examples of optional parameters and union types."""
from typing import Union
def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "Alien life from sector " + str(name)
    return greeting

# Single-argument:
print(hello("Gummy"))

# No arguments:
print(hello())

# int and float argument works too:
print(hello(110))
print(hello(4.77))

from typing import Union

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result

print(add(1.0, 2.0))
