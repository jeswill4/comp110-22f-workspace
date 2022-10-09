"""Dictionary exercise 07."""

__author__ = "730561311"


def invert(inversion: dict[str, str]) -> dict[str,str]:
    """Invert should swap key with values."""
    for key in inversion: 
        og_value = inversion[key]
        inversion[key] = key
        key = og_value


def favorite_color(colors: dict[str, str]) -> str:
    """Names, favorite color. Returns most popular color. If tie return 1st to appear color of the tie."""
    color_list: list[str] = list()
    color_quantity: list[int] = list()
    set_highest: str = ""
    i: int = 0
    while i < len(colors):
        for key in colors:
            color_list[i] = (colors(key))
        i += 1
    i: int = 0
    m: int = 1 
    n: int = 0
    while i < len(color_list):
        color_amount: int = 1
        while m < len(color_list):
            if color_list[i] == color_list[m]:
                color_amount += 1
            m += 1
        color_quantity.append(color_amount)
        i += 1
    while n < len(color_quantity):
        set_num: int = 0
        if color_quantity[n] > set_num:
            set_num = color_quantity[n]
            set_highest = color_list[n]
        n += 1
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
