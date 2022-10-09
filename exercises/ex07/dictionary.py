"""Dictionary exercise 07."""

__author__ = "730561311"


def invert(inversion: dict[str, str]) -> dict[str, str]:
    """Invert should swap key with values."""
    for key in inversion: 
        og_value = inversion[key]
        inversion[key] = key
        key = og_value


def favorite_color(colors: dict[str, str]) -> str:
    """Names, favorite color. Returns most popular color. If tie return 1st to appear color of the tie."""
    color_dict: dict[str, int]
    color_dict = {}
    set_highest: str = ""
    color_numbers: list[int] = list()
    i: int = 0
    n: int = 0
    m: int = 0
    for key in colors:
        color_dict = {colors[key]: 1}
        color_numbers.append(1) 
        while n < 1:
            set_highest = colors[key]
            n += 1
        if color_dict == colors[key]:
            color_dict[key] += 1
        i += 1
    for key in color_dict:
        if color_dict[key] > color_numbers[m]:
            set_highest = colors[key]
        m += 1
    return set_highest 
    

def count(count_dracula: list[str]) -> dict[str, int]:
    """Count produces dictionary of a list with [list str, count of # times that str appeared in list]."""
    empty_dict: dict[str, int]
    empty_dict = {}
    for index in count_dracula:
        if count_dracula[index] in empty_dict:
            empty_dict[count_dracula[index]] += 1
        else:
            empty_dict += {count_dracula[index]: 1}
    return empty_dict
