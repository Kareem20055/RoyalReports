import re

from design.colors import BLACK
from design.fonts import BODY_SIZE
from design.layout import TABLE_CELL_PADDING
from design.text import (
    draw_multiline_text,
    text_height,
)
from core.pdf.layout_engine import LayoutEngine


TIME_PATTERN = re.compile(
    r"^(AM|PM)\s+\d{1,2}:\d{2}$",
    re.IGNORECASE,
)


def draw_cell(
    canvas,
    text,
    x,
    y,
    width,
    height,
    background=None,
    text_color=BLACK,
    border_color=BLACK,
    bold=False,
):
    """
    Draw a single table cell.
    """

    canvas.setStrokeColor(border_color)

    if background is not None:
        canvas.setFillColor(background)
        canvas.rect(
            x,
            y - height,
            width,
            height,
            fill=1,
            stroke=1,
        )
    else:
        canvas.rect(
            x,
            y - height,
            width,
            height,
            fill=0,
            stroke=1,
        )

    canvas.setFillColor(text_color)

    available_width = width - (TABLE_CELL_PADDING * 2)

    content_height = text_height(
        text=str(text),
        max_width=available_width,
        bold=bold,
        size=BODY_SIZE,
    )

    # Center of the text block inside the cell
    text_y = y - (height / 2)

    if isinstance(text, str) and TIME_PATTERN.match(text.strip()):
        align = "center"
        text_x = x + TABLE_CELL_PADDING + (available_width / 2)
    else:
        align = LayoutEngine.text_align()
        text_x = LayoutEngine.text_x(
            cell_x=x,
            cell_width=width,
            padding=TABLE_CELL_PADDING,
        )

    draw_multiline_text(
        canvas=canvas,
        text=text,
        x=text_x,
        y=text_y,
        max_width=available_width,
        align=align,
        bold=bold,
        size=BODY_SIZE,
    )