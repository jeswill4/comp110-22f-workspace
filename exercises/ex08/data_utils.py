"""Dictionary related utility functions."""

__author__ = "730561311"

# Define your functions below

from io import TextIOWrapper


def read_csv_rows(entirety: str) -> list[dict[str,str]]:
    """Reads entirety of CSV data and puts in into a list of rows."""
    data_rows: list[dict[str, str]] = []
    file_handle: TextIOWrapper = open(entirety, "r")
    for data_rows in file_handle:
        data_rows = data_rows.lower()
        data_rows = data_rows.strip()
        data_rows.append(data_rows)
    return data_rows