""" 
Code for https://adventofcode.com/2021/day/21
"""

import os
from itertools import cycle
from typing import Sequence, Tuple, Any, Union
from dataclasses import dataclass

import numpy as np


class Board:
    """Board object for players to play on.  Circular track with 10 squares."""

    def __init__(self, p1_start: int, p2_start: int):
        self.p1 = Player(p1_start)
        self.p2 = Player(p2_start)
        self.turn = 0

        self._die_list = cycle(range(1, 101))

    def _die_roll(self) -> int:
        """Returns die roll for current turn."""
        return sum(next(self._die_list) for _ in range(3))

    def take_turn(self) -> None:
        self.turn += 1
        player = self.p1 if self.turn % 2 == 1 else self.p2

        die_roll = self._die_roll()
        player.loc = 1 + (player.loc + die_roll - 1) % 10
        player.score += player.loc


@dataclass
class Player:
    """Player object, contains score and location on board."""

    loc: int
    score: int = 0


# -- TESTS --


def test_misc_game() -> None:
    """Tests a misc game."""
    tests = [((4, 8), 739_785)]

    for test in tests:
        b = Board(test[0][0], test[0][1])
        while True:
            b.take_turn()
            if b.p1.score >= 1000:
                val = b.p2.score * b.turn * 3
                break
            if b.p2.score >= 1000:
                val = b.p1.score * b.turn * 3
                break

        print(val, b.p1, b.p2, b.turn)
        assert val == test[1]


# test_misc_game()


if __name__ == "__main__":

    # Initialize Data.
    p1_start = 9
    p2_start = 10

    def play_part_1(p1_start: int, p2_start: int) -> int:
        b = Board(p1_start, p2_start)
        while True:
            b.take_turn()
            if b.p1.score >= 1000:
                val = b.p2.score * b.turn * 3
                break
            if b.p2.score >= 1000:
                val = b.p1.score * b.turn * 3
                break
        return val

    solution_a = play_part_1(p1_start, p2_start)
    solution_b = 0

    print(f"AOC21a: {solution_a}\nAOC21b: {solution_b}")
