""" 
Code for https://adventofcode.com/2021/day/06
"""

import numpy as np


def calculate_number_of_lanternfish(data: str, days: int) -> int:
    """Creates a binned array whose index corresponds to the internal timer of the lantern fish
    and whose value is the number of lanternfish with that internal timer.  Shifts as in the problem:

    - Surely, each lanternfish creates a new lanternfish once every 7 days.
    - Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.
    """

    timers = list(map(int, data.split(",")))
    binned_data = np.bincount(timers, minlength=9)

    def iterate(data: np.ndarray) -> np.ndarray:
        new_data = np.roll(data, shift=-1)
        new_data[6] += data[0]
        return new_data

    for _ in range(days):
        binned_data = iterate(binned_data)

    return binned_data.sum()


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a06.csv", "r") as f:
        data = f.read()

    solution_a = calculate_number_of_lanternfish(data, 80)
    solution_b = calculate_number_of_lanternfish(data, 256)

    print(f"AOC06a: {solution_a}\nAOC06b: {solution_b}")
