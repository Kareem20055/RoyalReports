from .measure import measure_header
from .row import draw_row


def draw_header(
    canvas,
    headers,
    columns,
    y,
    background,
    text_color,
    margin,
):
    """
    Draw the table header.
    """

    header = measure_header(
        headers=headers,
        columns=columns,
    )

    draw_row(
        canvas=canvas,
        columns=columns,
        values=header["headers"],
        y=y,
        height=header["height"],
        header=True,
        background=background,
        text_color=text_color,
        margin=margin,
    )

    return y - header["height"]