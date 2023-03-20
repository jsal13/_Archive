""" 
Code for https://adventofcode.com/2021/day/13
"""

from typing import Tuple

import numpy as np


class Sheet:
    """Class representing the Sheet of paper which will contain dots at certain coordinates."""

    def __init__(self, dots: np.ndarray):
        self.dots = dots
        self.plot()  # Initialize variables.

    def __repr__(self) -> str:
        return "\n".join(
            "".join("#" if col else " " for col in row) for row in self.paper
        )

    def plot(self) -> None:
        """Plots the dots onto the paper."""
        # Make the paper big enough for the plots.
        ncols, nrows = self.dots.max(axis=0) + 1
        self.paper = np.zeros(shape=(nrows, ncols))
        for d in self.dots:
            self.paper[d[1], d[0]] = 1

    def fold(self, axis: str = "y", fold_value: int = 0) -> None:
        """Folds the array along a particular axis (always in half for the problem).  Adds a dot to the new coordinate if one is folded onto it."""
        fold_fn = lambda x: 2 * fold_value - x if x >= fold_value else x

        if axis == "x":
            x_vals = np.array(list(map(fold_fn, self.dots[:, 0])))
            y_vals = self.dots[:, 1]
        else:
            x_vals = self.dots[:, 0]
            y_vals = np.array(list(map(fold_fn, self.dots[:, 1])))

        self.dots = np.transpose(np.vstack([x_vals, y_vals]))
        self.plot()

    @classmethod
    def parse_data(cls, dots_data_raw: str) -> "Sheet":
        data_dots = np.array(
            [list(map(int, d.split(","))) for d in dots_data_raw.split("\n")]
        )
        return cls(data_dots)


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a13.csv", "r") as f:
        dots_data_raw, folds_data_raw = f.read().split("\n\n")

    def parse_folds_data(folds_data_raw: str) -> list[Tuple[str, int]]:
        fold_eqs0 = [s.replace("fold along ", "") for s in folds_data_raw.split("\n")]
        fold_eqs1 = [s.split("=") for s in fold_eqs0]
        fold_eqs = [(s[0], int(s[1])) for s in fold_eqs1]
        return fold_eqs

    def fold_sheet(
        sheet: Sheet, folds: list[Tuple[str, int]], n_times: int = None
    ) -> Sheet:
        """Folds `sheet` according to `folds`.  Returns the resultant `sheet` as an ndarray.  If `n_times` is specified, fold the sheet `n_times`, otherwise fold for all the folds in folds."""

        if n_times is not None:
            folds = folds[:n_times]

        for fold in folds:
            sheet.fold(*fold)

        return sheet

    sheet = Sheet.parse_data(dots_data_raw)
    folds = parse_folds_data(folds_data_raw)

    solution_a = int(fold_sheet(sheet, folds, n_times=1).paper.sum())
    solution_b = fold_sheet(sheet, folds)

    print(f"AOC13a: {solution_a}\nAOC13b:\n\n{solution_b}")
