""" 
Code for https://adventofcode.com/2021/day/3
"""

import os
from typing import Sequence

import numpy as np


class Report:
    """
    Class to manage Data for AOC Day 3.
    """

    def __init__(self, data: np.ndarray):
        self.data = data

    def calculate_part_1(self) -> int:
        """Calculates the gamma and epsilon rate for Part 1, returns the product."""
        gamma_rate = [
            "1" if Report._mode_is_one(self.data[:, idx]) else "0"
            for idx in range(len(self.data[0]))
        ]
        gamma_rate_val = Report._convert_bin_list_to_int(gamma_rate)

        epsilon_rate = [
            "0" if Report._mode_is_one(self.data[:, idx]) else "1"
            for idx in range(len(self.data[0]))
        ]
        epsilon_rate_val = Report._convert_bin_list_to_int(epsilon_rate)

        return gamma_rate_val * epsilon_rate_val

    def calculate_part_2(self) -> int:
        """Looks at the mode for each column and picks the corresponding rows which either have mode 1 or 0 (depending on oxy or co2)."""
        oxy_rating = self.data.copy()
        co2_rating = self.data.copy()

        # TODO: How to DRY this?
        idx = 0
        while len(oxy_rating) > 1 and idx < len(self.data[0]):
            oxy_desired_bit = int(Report._mode_is_one(oxy_rating[:, idx]))
            oxy_rating = np.array(
                [row for row in oxy_rating if row[idx] == oxy_desired_bit]
            )
            idx += 1

        idx = 0
        while len(co2_rating) > 1 and idx < len(self.data[0]):
            co2_desired_bit = int(not Report._mode_is_one(co2_rating[:, idx]))
            co2_rating = np.array(
                [row for row in co2_rating if row[idx] == co2_desired_bit]
            )
            idx += 1

        oxy_sol_value = Report._convert_bin_list_to_int(oxy_rating[0])
        co2_sol_value = Report._convert_bin_list_to_int(co2_rating[0])

        return oxy_sol_value * co2_sol_value

    @staticmethod
    def _mode_is_one(seq: Sequence) -> bool:
        """Returns True if the mode of a binary sequence `seq` is 1."""
        return sum(seq) >= len(seq) / 2

    @staticmethod
    def _convert_bin_list_to_int(s: list[str]) -> int:
        """Converts a list of binary values to a decimal.  Eg, '0010' -> 2."""
        return int("".join(map(str, s)), base=2)

    @classmethod
    def parse_input(cls, raw_input: str) -> "Report":
        """Takes raw input data from aoc3.csv (lines of binary) and returns an ndarray where each col/row is the corresponding binary digit from the input."""

        data = np.array([list(map(int, list(row))) for row in raw_input.splitlines()])
        return cls(data)


if __name__ == "__main__":
    with open(os.path.abspath("aoc/data/a03.csv"), "r") as f:
        data = f.read()

    report = Report.parse_input(data)

    solution_a = report.calculate_part_1()
    solution_b = report.calculate_part_2()

    print(f"AOC3a: {solution_a}\nAOC3b: {solution_b}")
