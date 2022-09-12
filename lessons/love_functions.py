"""Some tender loving functions!"""
def love(subject: str) -> str:
    """Give a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note

print(spread_love("Whiskers", 4))
print(spread_love("Moon", 4))
print(spread_love("you", 4))
