""" 
Code for https://adventofcode.com/2021/day/1
"""

import os
from typing import Sequence

import numpy as np

# NOTE: In Numpy 1.22.x, we will be able to use numpy.typing.ArrayLike.


def count_increases(data: Sequence[int]) -> int:
    """Takes `data` (list/ndarray of ints) and calculates the number of times the values increase as the list is waked.

    Examples
    --------
    >>> count_increases([1, 2, 3, 2, 4, 1])
    3
    """

    return np.sum(np.diff(data) > 0)


def create_sliding_window(data: Sequence[int], n: int = 3) -> Sequence[int]:
    """Creates an `n`-sliding window of a list of ints.

    Examples
    --------
    >>> create_sliding_window([1, 3, 4, 5, 6, 7])
    [ 8 12 15 18]

    >>> create_sliding_window([0, 1, 2, 3, 4])
    [3 6 9]
    """
    lag_array = np.array(
        [[data[idx + jdx] for jdx in range(n)] for idx in range(len(data) - 2)]
    )
    return np.sum(lag_array, axis=1)


if __name__ == "__main__":

    data = np.genfromtxt(os.path.abspath("aoc/data/a01.csv"), delimiter=",")

    solution_a = count_increases(data)
    solution_b = count_increases(create_sliding_window(data))

    print(f"AOC1a: {solution_a}\nAOC1b: {solution_b}")
