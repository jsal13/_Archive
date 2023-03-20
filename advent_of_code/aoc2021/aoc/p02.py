""" 
Code for https://adventofcode.com/2021/day/2
"""

import os
from dataclasses import dataclass


@dataclass
class Coord:
    """
    XY Coordinate with addition and scalar multiplication.
    (_Note: This is overkill for what we need; I wanted to practice using magic methods._)

    Attributes
    ----------
    x : int
    y : int
    """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Coord({self.x}, {self.y})"

    def __add__(self, coord: "Coord") -> "Coord":
        return Coord(self.x + coord.x, self.y + coord.y)

    def __mul__(self, other: int) -> "Coord":
        return Coord(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> "Coord":
        return self.__mul__(other)


class Submarine:
    def __init__(self, directions: list[tuple[Coord, int]]):
        self.directions = directions

    def commands_part_1(self) -> Coord:
        """
        forward X increases the horizontal position by X units.
        down X increases the depth by X units.
        up X decreases the depth by X units.

        This returns a Coord corresponding to the end location of the submarine.
        """
        current_loc = Coord(0, 0)
        for direction, value in self.directions:
            current_loc += value * direction

        return current_loc

    def commands_part_2(self) -> Coord:
        """
        In addition to horizontal position and depth (see `commands_part_1`), you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

        down X increases your aim by X units.
        up X decreases your aim by X units.
        forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
        """
        current_loc = Coord(0, 0)
        current_aim = 0
        for direction, value in self.directions:

            if direction.y in [-1, 1]:  # if going up or down...
                current_aim += direction.y * value

            elif direction.x == 1:  # if going forward...
                current_loc += Coord(value, value * current_aim)

            else:
                raise ValueError(f"Direction {direction} is not a valid direction!")

        return current_loc

    @classmethod
    def parse_directions(cls, raw_input: str) -> "Submarine":
        """Takes raw input data from aoc2.csv and parses it into a usable format for the class."""

        DIR_MAP = {"forward": Coord(1, 0), "down": Coord(0, 1), "up": Coord(0, -1)}

        lines = [line.strip().split(" ") for line in raw_input.splitlines()]
        parsed_dirs = [(DIR_MAP[line[0]], int(line[1])) for line in lines]
        return cls(directions=parsed_dirs)


if __name__ == "__main__":
    with open(os.path.abspath("aoc/data/a02.csv"), "r") as f:
        data = f.read().strip()

    submarine = Submarine.parse_directions(data)

    result_a = submarine.commands_part_1()
    solution_a = result_a.x * result_a.y

    result_b = submarine.commands_part_2()
    solution_b = result_b.x * result_b.y

    print(f"AOC2a: {solution_a}\nAOC2b: {solution_b}")
