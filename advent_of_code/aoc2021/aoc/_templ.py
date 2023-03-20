""" 
Code for https://adventofcode.com/2021/day/14
"""

import os
from typing import Sequence, Tuple, Any, Union
from pydantic.dataclasses import dataclass

import numpy as np


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a14.csv", "r") as f:
        data = f.read()

    solution_a = 0
    solution_b = 0

    print(f"AOC14a: {solution_a}\nAOC14b: {solution_b}")
