""" 
Code for https://adventofcode.com/2021/day/05
"""

from typing import Optional

import numpy as np


class LineSegment:
    """Object representing line segments with integer coordinates."""

    def __init__(
        self,
        coord1: tuple[int, int],
        coord2: tuple[int, int],
        include_diagonal: bool,
    ):
        self.include_diagonal = include_diagonal
        self.x1, self.y1 = coord1
        self.x2, self.y2 = coord2
        self.integer_coords: list[tuple[int, int]] = []

        self.slope: Optional[int] = None
        self.y_intercept: Optional[int] = None

        self._compute_slope_and_y_intercept()
        self._compute_coords_on_segment()

    def __repr__(self) -> str:
        return f"LineSegment(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"

    def _compute_slope_and_y_intercept(self) -> None:
        """Calculates the slope and y-intercept of the line segment (always an integer), returns None if infinite/undefined."""
        if self.x1 == self.x2:
            # If the line is vertical...
            self.slope = None
            self.y_intercept = None

        else:
            self.slope = int((self.y1 - self.y2) / (self.x1 - self.x2))
            self.y_intercept = self.y1 - self.slope * self.x1

    def _compute_coords_on_segment(self) -> None:
        """Computes coords with integer values on the line segments."""
        min_y = min(self.y1, self.y2)
        max_y = max(self.y1, self.y2)
        min_x = min(self.x1, self.x2)
        max_x = max(self.x1, self.x2)

        # Line is vertical...
        if self.y_intercept is None or self.slope is None:
            for _y in range(min_y, max_y + 1):
                self.integer_coords.append((self.x1, _y))

        # Line is horizontal...
        elif self.slope == 0:
            for _x in range(min_x, max_x + 1):
                self.integer_coords.append((_x, self.y1))

        # line is diagonal...
        else:
            if self.include_diagonal:
                for _x in range(min_x, max_x + 1):
                    val = self.slope * _x + self.y_intercept
                    try:
                        self.integer_coords.append((_x, int(val)))
                    except:
                        print(f"{val} isn't an integer!")


class Chart:
    """Chart object containing LineSegment objects."""

    def __init__(
        self,
        line_segments: list[LineSegment],
        chart_size: tuple[int, int] = (1_000, 1_000),
    ):
        self.line_segments = line_segments
        self.chart_size = chart_size
        self.chart = np.zeros(shape=self.chart_size)
        self._plot_integer_coords_on_chart()

    def _plot_integer_coords_on_chart(self) -> None:
        """Adds 1 to each integer point a line hits on the chart."""
        for line_segment in self.line_segments:
            for coord in line_segment.integer_coords:
                self.chart[coord[1], coord[0]] += 1

    @classmethod
    def input_parser(cls, data: str, include_diagonals: bool = False) -> "Chart":
        """Parses input data."""
        linesegments = []
        for row in data.split("\n"):
            row_split = row.split(" -> ")
            str_coords = row_split[0].split(",") + row_split[1].split(",")
            coords = list(map(int, str_coords))
            linesegments.append(
                LineSegment(
                    (coords[0], coords[1]),
                    (coords[2], coords[3]),
                    include_diagonal=include_diagonals,
                )
            )
        return cls(linesegments)


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a05.txt", "r") as f:
        data = f.read()

    solution_a = (Chart.input_parser(data, False).chart >= 2).sum()  # No diagonals.
    solution_b = (Chart.input_parser(data, True).chart >= 2).sum()  # Include diagonals.

    print(f"AOC05a: {solution_a}\nAOC05b: {solution_b}")
