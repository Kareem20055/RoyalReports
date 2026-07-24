from design.fonts import BODY_SIZE

from design.layout import TABLE_CELL_PADDING

from design.text import (
    wrap_text,
    text_height,
)


def measure_header(
    headers,
    columns,
):
    """
    Measure the table header.
    """

    wrapped_headers = []
    max_height = 0

    for header, (_, width) in zip(headers, columns):

        available_width = width - (TABLE_CELL_PADDING * 2)

        lines = wrap_text(
            text=str(header),
            max_width=available_width,
            bold=True,
            size=BODY_SIZE,
        )

        height = text_height(
            text=str(header),
            max_width=available_width,
            bold=True,
            size=BODY_SIZE,
        )

        wrapped_headers.append(lines)

        if height > max_height:
            max_height = height

    return {
        "height": max_height + 8,
        "headers": wrapped_headers,
    }


def measure_rows(
    rows,
    columns,
):
    """
    Measure all table rows.
    """

    measured_rows = []

    for row in rows:

        max_height = 0
        values = []

        for value, (_, width) in zip(row, columns):

            available_width = width - (TABLE_CELL_PADDING * 2)

            lines = wrap_text(
                text=str(value),
                max_width=available_width,
                bold=False,
                size=BODY_SIZE,
            )

            height = text_height(
                text=str(value),
                max_width=available_width,
                bold=False,
                size=BODY_SIZE,
            )

            values.append(lines)

            if height > max_height:
                max_height = height

        measured_rows.append(
            {
                "height": max_height + 8,
                "values": values,
            }
        )

    return measured_rows