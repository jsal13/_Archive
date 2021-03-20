# pylint: disable=missing-module-docstring, too-many-arguments, bad-continuation
# pylint: disable=too-many-instance-attributes, invalid-name, missing-function-docstring
# pylint: disable=too-many-function-args, line-too-long

import typing  # pylint: disable=unused-import
import os

import numpy as np
from PIL import Image, ImageDraw


def hex_to_rgba(c):
    c = c.replace("#", "")
    if len(c) == 6:  # If alpha not specified...
        c += "ff"

    return np.array([int(f"{c[idx]}{c[idx + 1]}", 16) for idx in [0, 2, 4, 6]]).astype(
        np.uint8
    )


class BoundingBox:
    """ ok """

    def __init__(
        self,
        interior_width: int,
        interior_height: int,
        outer_color: str = "#0044ffff",
        inner_color: str = "#22aa00ff",
        fill_color: str = "#ffffff00",
        border_color: str = "#000000ff",
        save_folder: str = os.path.expanduser("~"),
        file_prefix: str = "",
    ):

        file_name = (
            f"{file_prefix}{'_' if file_prefix else ''}"
            + f"{interior_width}w_{interior_height}h"
            + f"_{outer_color[1:]}_outer_{inner_color[1:]}_inner.png"
        )
        self.save_path = os.path.join(save_folder, file_name)

        self.interior_width = interior_width
        self.interior_height = interior_height
        self.outer_color = hex_to_rgba(outer_color)
        self.inner_color = hex_to_rgba(inner_color)
        self.fill_color = hex_to_rgba(fill_color)  # default transparent.
        self.border_color = hex_to_rgba(border_color)  # default #000000ff

        self.outer_color_raw = outer_color
        self.inner_color_raw = inner_color
        self.fill_color_raw = fill_color  # default transparent.
        self.border_color_raw = border_color  # default #000000ff

        self.border_width = 2
        self.outer_width = 2
        self.inner_width = 4
        self.total_border_width = (
            (2 * self.border_width) + (2 * self.outer_width) + self.inner_width
        )

        if (
            (self.inner_width % 2 != 0)
            or (self.outer_width % 2 != 0)
            or (self.border_width % 2 != 0)
        ):
            raise Exception("Please make widths an even number.")

        im = self._join_pieces()
        im.save(self.save_path)

    def _make_strip(self, width: int, direction: bool = "vertical"):
        """ Makes a strip of bounding box of length `length`.
        To make it horizontal instead of vertical, use `direction='horizontal'`."""
        # Slice of blackx2, outer_color, inner_colorx2, blackx2.
        single_slice = np.array(
            [self.border_color] * self.border_width
            + [self.outer_color] * self.outer_width
            + [self.inner_color] * self.inner_width
            + [self.outer_color] * self.outer_width
            + [self.border_color] * self.border_width
        ).astype(np.uint8)

        strip = np.array([single_slice for _ in range(width)])
        if direction == "horizontal":
            strip = strip.swapaxes(0, 1)

        return Image.fromarray(strip)

    def _make_center_fill(self):
        """ Creates the center fill for the bounding box. """
        im = np.array(
            [self.fill_color for _ in range(self.interior_width * self.interior_height)]
        ).astype(np.uint8)

        return Image.fromarray(im.reshape(self.interior_height, self.interior_width, 4))

    def _make_corner(self):
        """ Creates a corner for the bounding box. """
        canvas = Image.new("RGBA", (self.total_border_width, self.total_border_width))
        draw = ImageDraw.Draw(canvas)

        half_len = int(self.total_border_width / 2) - 1  # it must be even from above.

        # Background: sets to transparent white for replacement later.
        draw.rectangle(
            [(0, 0), (self.total_border_width, self.total_border_width)],
            fill=self.inner_color_raw,
        )

        # Outer boundary
        draw.line(
            [(0, 0), (0, half_len)], width=self.border_width, fill=self.border_color_raw
        )
        draw.line(
            [
                (half_len, self.total_border_width - self.border_width),
                (self.total_border_width, self.total_border_width - self.border_width),
            ],
            width=self.border_width,
            fill=self.border_color_raw,
        )
        draw.line(
            [(0, half_len), (half_len, self.total_border_width - self.border_width)],
            width=self.border_width,
            fill=self.border_color_raw,
        )

        # Outer color
        draw.line(
            [
                (self.border_width + (self.outer_width / 2) - 1, 0),
                (self.border_width + (self.outer_width / 2) - 1, half_len),
            ],
            width=self.outer_width,
            fill=self.outer_color_raw,
        )
        draw.line(
            [
                (
                    half_len + (self.border_width / 2),
                    self.total_border_width
                    - self.border_width
                    - (self.outer_width / 2)
                    - 1,
                ),
                (
                    self.total_border_width,
                    self.total_border_width
                    - self.border_width
                    - (self.outer_width / 2)
                    - 1,
                ),
            ],
            width=self.outer_width,
            fill=self.outer_color_raw,
        )
        #!! TODO: This breaks EVERYTHING if we change the size of the items above.
        #!! TODO: Need to fix this boi.
        draw.line(
            [
                (
                    self.border_width + (self.outer_width / 2) - 1,
                    half_len - (self.border_width / 2),
                ),
                (
                    half_len + (self.border_width / 2),
                    self.total_border_width - self.border_width - self.outer_width,
                ),
            ],
            width=self.outer_width,
            fill=self.outer_color_raw,
        )

        # Outer color on top-right part.
        draw.polygon(
            [
                (self.total_border_width - self.border_width - self.outer_width, 0),
                (self.total_border_width, 0),
                (self.total_border_width, self.border_width + self.outer_width),
            ],
            fill=self.outer_color_raw,
        )

        # Border color on top-right part.
        draw.polygon(
            [
                (self.total_border_width - self.border_width, 0),
                (self.total_border_width, 0),
                (self.total_border_width, self.border_width),
            ],
            fill=self.border_color_raw,
        )

        draw.polygon(
            [
                (0, half_len + self.border_width),
                (0, self.total_border_width),
                (half_len, self.total_border_width),
            ],
            fill="#00000000",
        )

        return canvas

    def _join_pieces(self):
        """ Joins edges, corners, and center fill. """

        canvas = Image.new(
            "RGBA",
            (
                (self.interior_width + 2 * self.total_border_width),
                (self.interior_height + 2 * self.total_border_width),
            ),
        )

        horiz_strip = self._make_strip(
            width=self.interior_width, direction="horizontal"
        )
        vert_strip = self._make_strip(width=self.interior_height, direction="vertical")
        corner = self._make_corner()
        center_fill = self._make_center_fill()

        # Top + Bottom
        for _y in [0, self.total_border_width + self.interior_height]:
            canvas.paste(horiz_strip, (self.total_border_width, _y))

        # Corners
        canvas.paste(corner.rotate(270), (0, 0))  # UL
        canvas.paste(
            corner.rotate(180), (self.total_border_width + self.interior_width, 0)
        )  # UR
        canvas.paste(corner, (0, self.total_border_width + self.interior_height))  # LL
        canvas.paste(
            corner.rotate(90),
            (
                self.total_border_width + self.interior_width,
                self.total_border_width + self.interior_height,
            ),
        )  # LR

        # Left + Right
        for _x in [0, self.total_border_width + self.interior_width]:
            canvas.paste(vert_strip, (_x, self.total_border_width))

        # Center fill
        canvas.paste(center_fill, (self.total_border_width, self.total_border_width))

        return canvas


def make_snes_scene_boxes(inner_bounding_color_hex, outer_color_hex="#000000"):
    """ Makes an SNES Scene set of bounding boxes.  Name labels have spaces for pronouns.

    Note the SNES emu bounding boxes are 540w x 480h.
    """

    # emu bounding box
    BoundingBox(
        interior_width=540,
        interior_height=480,
        outer_color=outer_color_hex,
        inner_color=inner_bounding_color_hex,
    )

    # nameplate bounding
    BoundingBox(
        interior_width=375,
        interior_height=90,
        outer_color=outer_color_hex,
        inner_color=inner_bounding_color_hex,
    )


if __name__ == "__main__":
    # Make a GUI For this.
    console = "SNES"

    if console == "SNES":
        make_snes_scene_boxes(
            inner_bounding_color_hex="#2a3d66", outer_color_hex="#d789d7"
        )
