from core.pdf.layout_engine import LayoutEngine

from design.fonts import (
    ARABIC_FONT,
    BODY_SIZE,
)

from .measure import measure_rows
from .row import draw_row


def draw_info_list(
    canvas,
    rows,
    current_y,
    page_width,
    margin,
    divider=True,
):
    """
    Draw an information list.

    rows:
        [
            ("اسم الموظف", "كريم سيد"),
            ("رقم الموظف", "11"),
            ...
        ]
    """

    labels = [
        label
        for label, _ in rows
    ]

    layout = LayoutEngine.key_value_layout(
        labels=labels,
        page_width=page_width,
        margin=margin,
        font_name=ARABIC_FONT,
        font_size=BODY_SIZE,
    )

    measured_rows = measure_rows(
        rows=rows,
        layout=layout,
    )

    x = layout.margin

    for row in measured_rows:

        current_y = draw_row(
            canvas=canvas,
            layout=layout,
            row=row,
            x=x,
            y=current_y,
            divider=divider,
        )

    return current_y