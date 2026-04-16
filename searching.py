from pathlib import Path
import json
from generators import ordered_sequence

import time
import matplotlib.pyplot as plt

def read_data(file_name, field):

    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
        if field in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
            return data[field]
        else:
            return None




def linear_search(seq, number):
    positions = []
    count = 0
    for i, s in enumerate(seq):
        if s == number:
            positions.append(i)
            count += 1
    return {"positions": positions, "count": count}




def binary_search(seq, number):
    left = 0
    right = len(seq) - 1

    while left <= right:
        middle = (left + right) // 2
        if seq[middle] == number:
            return middle
        elif seq[middle] > number:
            right = middle - 1
        else:
            left = middle + 1
    return None






def main():
    time = []
    data = read_data("sequential.json", "ordered_numbers")
    print(data)
    print(linear_search(data, 63))
    print(binary_search(data, 8))


if __name__ == "__main__":
    main()
