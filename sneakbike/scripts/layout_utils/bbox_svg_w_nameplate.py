import os
import math

from wand.api import library
import wand.color
import wand.image


def create_inner_bbox(
    box_height=200,
    box_width=200,
    box_x=1,
    box_y=1,
    box_stroke_width=2,
    bbox_stroke_width=2,
    bbox_color="#232666",
    bbox_r=2,
    xml_id="",
):

    stroke_total_width = bbox_stroke_width + box_stroke_width
    h = box_height - stroke_total_width
    w = box_width - stroke_total_width
    x = box_x + (stroke_total_width / 2)
    y = box_y + (stroke_total_width / 2)

    tmpl = (
        h,
        w,
        x,
        y,
        f"""<rect id="{xml_id}" style="fill:none; stroke:{bbox_color}; stroke-width:{bbox_stroke_width}px;" fill-opacity="0" width="{w}px" height="{h}px" x="{x}px" y="{y}px" rx="{bbox_r}px" ry="{bbox_r}px"/>""",
    )

    return tmpl


def create_bbox(
    height=200,
    width=200,
    outer_border_color="#726a95",
    inner_border_color="#709fb0",
    border_color="#000000",
    save_path=os.path.expanduser("~"),
    save_prefix="",
    nameplate=False,
):
    # We have to init an empty box with stroke width 2 to start at 1, 1.
    boundaries = [
        {"stroke_width": 1},
        {"stroke_width": 2, "color": border_color, "r": 5, "id": "outer_border"},
        {
            "stroke_width": 4,
            "color": outer_border_color,
            "r": 3,
            "id": "outer_outer_border",
        },
        {"stroke_width": 8, "color": inner_border_color, "r": 0, "id": "inner"},
        {
            "stroke_width": 4,
            "color": outer_border_color,
            "r": 0,
            "id": "inner_outer_border",
        },
        {"stroke_width": 2, "color": border_color, "r": 0, "id": "inner_border"},
    ]

    stroke_width_sum = (
        sum([b["stroke_width"] for b in boundaries]) - 2
    )  # minus the init

    additional_sizing = 0
    if nameplate:
        additional_sizing = 50

    bounding_boxes_total_size = 2 * stroke_width_sum
    svg_height = height + bounding_boxes_total_size
    svg_width = width + bounding_boxes_total_size

    _xml = f"""<svg xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink= "http://www.w3.org/1999/xlink" width="{svg_width}px" height="{svg_height + additional_sizing}px">"""

    h, w, x, y = svg_height, svg_width, 0, 0
    rect_list = []
    for idx in range(1, len(boundaries)):
        h, w, x, y, txt = create_inner_bbox(
            box_height=h,
            box_width=w,
            box_x=x,
            box_y=y,
            box_stroke_width=boundaries[idx - 1]["stroke_width"],
            bbox_stroke_width=boundaries[idx]["stroke_width"],
            bbox_color=boundaries[idx]["color"],
            bbox_r=boundaries[idx]["r"],
            xml_id=boundaries[idx]["id"],
        )
        rect_list.append(txt)

    # HARDCODED FOR NOW
    nameplate_str = ""
    if nameplate:
        nameplate_str = f"""<rect id="namebox" style="fill:{inner_border_color}; stroke:#000000; stroke-width:2px;" fill-opacity="1" width="{svg_width - 33}px" height="50px" x="16.5px" y="504px" rx="2px" ry="2px"/>"""

    # Inner has to be first to get overlapped.
    # This may not work for any more than N=5 borders.
    # TODO: Maybe make this cleaner.
    inner_bd = rect_list.pop(int(math.ceil(len(rect_list) / 2)))

    _xml += (inner_bd + "\n" + nameplate_str + "\n" + "\n".join(rect_list)) + "</svg>"

    file_name = (
        f"{height}h_{width}w_{outer_border_color[1:]}out_{inner_border_color[1:]}in.svg"
    )

    if save_prefix:
        file_name = save_prefix + "_" + file_name

    file_loc = os.path.join(save_path, file_name)
    new_file_loc = os.path.splitext(file_loc)[0] + ".png"
    with open(file_loc, "w+") as f:
        f.write(_xml)

    # Render pngs.
    with open(file_loc, "r") as svg_file:
        with wand.image.Image() as image:
            with wand.color.Color("transparent") as background_color:
                library.MagickSetBackgroundColor(image.wand, background_color.resource)
            svg_blob = svg_file.read().encode("utf-8")
            image.read(blob=svg_blob)
            png_image = image.make_blob("png32")

        with open(new_file_loc, "wb") as out:
            out.write(png_image)


def generate_sneakbike_sizes(
    outer_border_color, inner_border_color, border_color="#000000"
):

    save_path = os.path.join(
        os.path.expanduser("~"),
        f"sneakbike_bboxes_{outer_border_color[1:]}out_{inner_border_color[1:]}in_{border_color[1:]}bdd",
    )

    os.makedirs(save_path, exist_ok=True)
    # name, width, height
    box_list = [
        ["NES", 480, 512, False],
        ["SNES", 476, 544, True],
        ["GENESIS", 448, 640, False],
        ["NAMEPLATE", 533, 375, False],
    ]

    for item in box_list:
        create_bbox(
            height=item[1],
            width=item[2],
            outer_border_color=outer_border_color,
            inner_border_color=inner_border_color,
            border_color=border_color,
            save_path=save_path,
            save_prefix=item[0],
            nameplate=True,
        )


if __name__ == "__main__":
    outer_border_color = "#726a95"
    inner_border_color = "#709fb0"
    border_color = "#000000"
    generate_sneakbike_sizes(
        outer_border_color=outer_border_color,
        inner_border_color=inner_border_color,
        border_color=border_color,
    )

