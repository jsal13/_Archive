""" 
Code for https://adventofcode.com/2021/day/11
"""

import numpy as np


class OctoMap:
    def __init__(self, data: np.ndarray):
        self.data = data.copy()
        self.n_rows, self.n_cols = self.data.shape
        self.total_flashes = 0

    def step_n_times(self, n: int) -> None:
        """Step `n` times through an octopus iteration."""
        for _ in range(n):
            self._step()

    def _step(self) -> None:
        """Adds one to each element, checks for flashing until the octopus
        flashing is static, then zeros-out the flashed octos.
        """
        # Reset flash data.
        self.flashed_once = np.zeros_like(self.data)
        self.num_flashes_in_loop = 9999

        self.data += 1

        # We continue looping over the array until we check and re-check
        # each octo for flashing.  If none flashed this loop, the loop is
        # over since no other octos could increase in value after that.
        while self.num_flashes_in_loop > 0:
            self.num_flashes_in_loop = 0  # Reset.

            for idx in range(self.n_cols):
                for jdx in range(self.n_cols):
                    if self.data[idx, jdx] > 9 and not self.flashed_once[idx, jdx]:
                        self.flashed_once[idx, jdx] += 1
                        self.num_flashes_in_loop += 1
                        self._increment_neighbors(idx, jdx)

            self.total_flashes += self.num_flashes_in_loop
        self.data[self.data > 9] = 0

    def _increment_neighbors(self, idx: int, jdx: int) -> None:
        """Increments neighboring values in a grid by 1, including diagonals."""
        neighbors = [
            [idx + i, jdx + j]
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
            if (
                (idx + i) >= 0
                and (idx + i) < self.n_cols
                and (jdx + j) >= 0
                and (jdx + j) < self.n_rows
            )
            and (not (i == 0 and j == 0))
        ]

        for neighbor in neighbors:
            self.data[neighbor[0], neighbor[1]] += 1

    @classmethod
    def parse_input(cls, data: str) -> "OctoMap":
        parsed_data = np.array([[int(i) for i in j] for j in data.split("\n")])
        return cls(parsed_data)


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a11.csv", "r") as f:
        data = f.read()

    def step_100_times(data: str) -> int:
        """Steps 100 times and returns the total value of the octos."""
        om = OctoMap.parse_input(data)
        om.step_n_times(100)

        return om.total_flashes

    def wait_until_all_zeros(data: str) -> int:
        """Finds the number of steps necessary to put all octos at value 0."""
        om = OctoMap.parse_input(data)
        idx = 0
        while True:
            idx += 1
            om.step_n_times(1)
            if om.data.sum() == 0:
                break
        return idx

    solution_a = step_100_times(data)
    solution_b = wait_until_all_zeros(data)

    print(f"AOC11a: {solution_a}\nAOC11b: {solution_b}")
