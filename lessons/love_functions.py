"""Some tender loving functions!"""
def love(subject: str) -> str:
    """Give a subject as a parameter, returns a loving string."""
    return f"I love you {subject}"

from lessons.love_functions import love
def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note = love(to) + "\n"
    i += 1
    return love_note
    