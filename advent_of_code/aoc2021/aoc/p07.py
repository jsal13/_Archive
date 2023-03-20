""" 
Code for https://adventofcode.com/2021/day/07
"""

import numpy as np


def rearrange_crabs(data: np.ndarray) -> int:
    """You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible."""
    return min(sum([abs(d - i) for d in data]) for i in range(1000))


def rearrange_crabs_with_dynamic_fuel(data: np.ndarray) -> int:
    """As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

    (James: Brute force.  Nothing clever to see here, move along.)"""

    def calculate_dynamic_fuel_for_horiz_pos(pos: int, data: np.ndarray) -> int:
        """Tests horizontal position where fuel costs sum(1..n) for n positions moved."""

        vsum_of_digits = np.vectorize(lambda n: n * (n + 1) / 2)
        return vsum_of_digits(np.absolute(data - pos)).sum()

    values = []
    for pos in range(data.min(), data.max() + 1):
        values.append([pos, calculate_dynamic_fuel_for_horiz_pos(pos, data)])

    arr = np.array(values)
    return int(arr[arr[:, 1].argmin()][1])


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a07.csv", "r") as f:
        data = f.read()

    def parse_input(s: str) -> np.ndarray:
        return np.array(list(map(int, s.split(","))))

    parsed_data = parse_input(data)

    solution_a = rearrange_crabs(parsed_data)
    solution_b = rearrange_crabs_with_dynamic_fuel(parsed_data)

    print(f"AOC07a: {solution_a}\nAOC07b: {solution_b}")
