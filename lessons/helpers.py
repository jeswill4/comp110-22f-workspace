"""Demonstrate defining a module imported elsewhere."""

def main() -> None:
    print(powerful(2,10))
    print("helpers.py run as a module")

def powerful(x: float, n: float) -> float:
    """"Raise x to the power of n."""
    return x ** n



THE_ANSWER: int = 42

print("helpers.py was evaluated")


# Idiom for making a module able to run as a program
# or have its global definitions imported elsewhere.
if __name__ == "__main__":
    main()
else:
    # It is not idiomatic to have an else branch
    print(f"helper.py was imported: {__name__}")