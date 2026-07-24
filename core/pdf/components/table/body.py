from .measure import measure_rows
from .row import draw_row


def draw_rows(
    canvas,
    rows,
    columns,
    y,
):
    """
    Draw all table rows.
    """

    measured_rows = measure_rows(
        rows=rows,
        columns=columns,
    )

    for row in measured_rows:

        draw_row(
            canvas=canvas,
            columns=columns,
            values=row["values"],
            y=y,
            height=row["height"],
        )

        y -= row["height"]

    return y