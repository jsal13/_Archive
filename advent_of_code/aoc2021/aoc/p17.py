""" 
Code for https://adventofcode.com/2021/day/17
"""

import re
from collections import namedtuple

import numpy as np

# Namedtuple to represent xy position for the probelauncher.
Position = namedtuple("Position", ("x", "y"))
TargetZone = namedtuple("TargetZone", ("xmin", "xmax", "ymin", "ymax"))


class ProbeLauncher:

    """
    The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y (upward, or downward if negative) directions. For example, an initial x,y velocity like 0,10 would fire the probe straight up, while an initial velocity like 10,-1 would fire the probe forward at a slight downward angle.

    The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

    - The probe's x position increases by its x velocity.
    - The probe's y position increases by its y velocity.
    - Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    - Due to gravity, the probe's y velocity decreases by 1.
    """

    def __init__(self, x_vel: int, y_vel: int, target_zone: TargetZone) -> None:
        """Class for Probe Launcher.

        Parameters
        ----------
        x_vel : int
            The initial value for velocity in the x-direction.
        y_vel : int
            The initial value for velocity in the y-direction.
        target_zone : tuple[int, int, int, int]
            (x_min, x_max, y_min, y_max) for the desired target zone.
        """

        self.x_vel = x_vel
        self.y_vel = y_vel
        self.target_zone = target_zone

        # Keep track of all launched probe positions per step.
        self.current_pos = Position(0, 0)
        self.positions = [self.current_pos]

    @property
    def highest_y_position(self) -> int:
        """Returns the maximum value of y that the probe has reached thus far.  (For the problem solution.)"""
        return max(pos.y for pos in self.positions)

    def step(self) -> None:
        new_x = self.current_pos.x + self.x_vel
        new_y = self.current_pos.y + self.y_vel
        self.current_pos = Position(new_x, new_y)
        self.positions.append(self.current_pos)

        # Reduce velocities by 1 due to drag/gravity.
        self.x_vel = max(0, self.x_vel - 1)
        self.y_vel -= 1

    def step_until_out_of_range(self) -> None:
        """Steps until the probe is out of range for the target."""

        while True:
            # If we overshot it and it's
            if self.current_pos.x > self.target_zone.xmax:
                break

            # If we're free-falling...
            if self.x_vel == 0:

                # If we're not in the x-range to get there.
                if (
                    self.current_pos.x < self.target_zone.xmin
                    or self.current_pos.x > self.target_zone.xmax
                ):
                    break

                # If we're below it...
                if self.current_pos.y < self.target_zone.ymin:
                    break

            # If we're falling and below the min y value.
            if self.y_vel < 0 and self.current_pos.y < self.target_zone.ymin:
                break

            self.step()

    def _is_in_target_zone(self, pos: Position) -> bool:
        """Returns True if `pos` is inside of the `target_zone`."""
        return (
            (pos.x >= self.target_zone.xmin)
            and (pos.x <= self.target_zone.xmax)
            and (pos.y >= self.target_zone.ymin)
            and (pos.y <= self.target_zone.ymax)
        )

    def has_hit_target(self) -> bool:
        """Checks all positions in `positions` to see if any have hit the `target_zone`."""

        return any(self._is_in_target_zone(pos) for pos in self.positions)

    def __repr__(self) -> str:
        """Graphs a representation of the arc.
        Note: This is kind'a gross, just wanted to make an 'okay' picture."""
        max_x_val = max(max(p.x for p in self.positions), self.target_zone.xmax)
        y_span = max(
            abs(max(p.y for p in self.positions))
            + abs(min(p.x for p in self.positions)),
            abs(self.target_zone.ymax) + abs(self.target_zone.xmax),
        )
        min_y_val = min(p.y for p in self.positions)
        grid = np.zeros(shape=(y_span + 1, max_x_val + 1))
        y_offset = int(y_span / 2) + min_y_val

        # Plot the Target Zone.
        for col in range(self.target_zone.xmin, self.target_zone.xmax + 1):
            for row in range(self.target_zone.ymin, self.target_zone.ymax + 1):
                grid[y_offset - row, col] = 2

        # Plot the positions of the probe.
        for pos in self.positions:
            grid[y_offset - pos.y, pos.x] = 1

        symbol_map = {0: ".", 1: "#", 2: "T"}
        return "\n".join(" ".join(symbol_map[r] for r in row) for row in grid)

    @classmethod
    def parse_input(cls, input_data: str, x_vel: int, y_vel: int) -> "ProbeLauncher":
        """Parses input which looks like into an appropriate target area, returns `ProbeLauncher` obj with associated `x_vel, y_vel`."""

        pattern = re.compile(r"[xy]=(-?\d+)\.\.(-?\d+),?")
        x, y = re.findall(pattern, input_data)
        target_zone = TargetZone(int(x[0]), int(x[1]), int(y[0]), int(y[1]))
        return cls(x_vel, y_vel, target_zone)


# -- Tests --
def test_examples() -> None:
    test_input = "target area: x=20..30, y=-10..-5"

    # [x, y, has_hit_target]
    tests = [
        [7, 2, True],
        [6, 3, True],
        [9, 0, True],
        [17, -4, False],
    ]

    for test in tests:
        probe = ProbeLauncher.parse_input(test_input, test[0], test[1])
        probe.step_until_out_of_range()
        assert (
            probe.has_hit_target() == test[2]
        ), f"Expected {test[2]} for {test[0]}, {test[1]}"


# test_examples()

if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a17.csv", "r") as f:
        data = f.read()

    def grid_vels_for_trajectory(
        input_data: str,
        xvmin: int = 0,
        xvmax: int = 300,
        yvmin: int = -120,
        yvmax: int = 5_000,
    ) -> tuple[tuple[int, int], int, int]:
        """Grid-searches over values for x, y.  Returns x, y such that the max y value is attained and hits the target.

        Parameters
        ----------
        xvmin : int, optional
            Minimum x velocity to begin gridding with, by default 0
        xvmax : int, optional
            Maximum x velocity to begin gridding with, by default 20
        yvmin : int, optional
            Minimum y velocity to begin gridding with], by default -10
        yvmax : int, optional
            Maximum y velocity to begin gridding with, by default 20

        Returns
        -------
        tuple[tuple[int, int], int, int]
            ((xvel, yvel), max_y_attained, number_of_vels_that_hit) which the max y value attained and hits the target.  `number_of_vels_that_hit` is the total number of velocities that hit the target.
        """

        current_best_vels = (-9999, -9999)
        current_max_y = -9999

        number_of_vels_that_hit = 0

        for xv in range(xvmin, xvmax + 1):
            for yv in range(yvmin, yvmax + 1):
                p = ProbeLauncher.parse_input(input_data, xv, yv)
                p.step_until_out_of_range()
                if p.has_hit_target():
                    number_of_vels_that_hit += 1
                    if p.highest_y_position > current_max_y:
                        current_max_y = p.highest_y_position
                        current_best_vels = (xv, yv)

        return (current_best_vels, current_max_y, number_of_vels_that_hit)

    grid_results = grid_vels_for_trajectory(data)

    solution_a = grid_results[1]
    solution_b = grid_results[2]

    print(f"AOC17a: {solution_a}\nAOC17b: {solution_b}")
