"""Dictionary related utility functions."""

__author__ = "730561311"

# Define your functions below

from io import TextIOWrapper


def read_csv_rows(entirety: str) -> list[dict[str,str]]:
    """Reads entirety of CSV data and puts in into a list of rows."""
    data_rows: list[dict[str, str]] = []
    file_handle: TextIOWrapper = open(entirety, "r")
    for data_row in file_handle:
        data_row = data_row.lower()
        data_row = data_row.strip()
        data_rows.append(data_row)
    return data_rows


def column_values(list_rows: list[dict[str, str]], column_name: str) -> list[str]:
    """Makes column names."""
    column_values: list[str] = []
    for row in list_rows:
        if column_name in list_rows:
            column_values.append(row)
    return column_values


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Make a table represented as a list of rows into a dictionary of columns."""
    the_dict: dict[str, list[str]] = []
    the_list: list[str] = []
    for column in table:
        the_list.append(column_values(table, table[column]))


def select(not_m: dict[str, list[str]], copy_c: list[str]) -> dict[str, list[str]]:
    """Produce new column-based table wiht only a specific subset of the original columns."""
    new_copy: dict[str, list[str]] = []
    for key in copy_c:
        new_copy.append(copy_c[key])
    return new_copy


def count(value_l: list[str]) -> dict[str, int]:
    """Counter of each key with a unique value."""
    counter: dict[str, int] = []
    if value_l in counter:
        counter[value_l] += 1
    else:
        counter[value_l] = 1
    return counter 




