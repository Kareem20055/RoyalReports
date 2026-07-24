from design.colors import BLACK
from design.layout import PAGE_MARGIN

from .cell import draw_cell


def draw_row(
    canvas,
    columns,
    values,
    y,
    height,
    margin=PAGE_MARGIN,
    header=False,
    background=None,
    text_color=BLACK,
):
    """
    Draw one complete row.
    """

    if len(columns) != len(values):
        raise ValueError(
            "columns and values must have the same length."
        )

    x = margin

    for value, (_, column_width) in zip(values, columns):

        draw_cell(
            canvas=canvas,
            text=value,
            x=x,
            y=y,
            width=column_width,
            height=height,
            background=background,
            text_color=text_color,
            bold=header,
        )

        x += column_width