"""Examples of importing in Python."""


from lessons import helpers

# Alias a module / imported name as another name
# simplifies helpers. to hp. when calling function, hp.powerful
from lessons import helpers as hp

# Import names defined globally in a module
# no longer need file name. before fn
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2,4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)
if __name__ == "__main__":
    main()
