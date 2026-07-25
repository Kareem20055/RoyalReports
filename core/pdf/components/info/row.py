from design.fonts import BODY_SIZE

from design.info import (
    LABEL_PADDING,
    VALUE_PADDING,
    INFO_LABEL_BOLD,
    INFO_VALUE_BOLD,
    INFO_DIVIDER_COLOR,
    INFO_DIVIDER_WIDTH,
)

from design.text import draw_multiline_text

from core.pdf.layout_engine import LayoutEngine


def draw_row(
    canvas,
    layout,
    row,
    x,
    y,
    divider=True,
):
    """
    Draw one information row.

    row:
    {
        "height": ...,
        "label": [...],
        "value": [...],
    }
    """

    height = row["height"]

    label_width = layout.label_width
    value_width = layout.value_width

    if LayoutEngine.rtl():

        value_x = x
        label_x = x + value_width

    else:

        label_x = x
        value_x = x + label_width

    draw_multiline_text(
        canvas=canvas,
        text=row["label"],
        x=LayoutEngine.text_x(
            label_x,
            label_width,
            LABEL_PADDING,
        ),
        y=y - (height / 2),
        max_width=label_width - (LABEL_PADDING * 2),
        align=LayoutEngine.text_align(),
        bold=INFO_LABEL_BOLD,
        size=BODY_SIZE,
    )

    draw_multiline_text(
        canvas=canvas,
        text=row["value"],
        x=LayoutEngine.text_x(
            value_x,
            value_width,
            VALUE_PADDING,
        ),
        y=y - (height / 2),
        max_width=value_width - (VALUE_PADDING * 2),
        align=LayoutEngine.text_align(),
        bold=INFO_VALUE_BOLD,
        size=BODY_SIZE,
    )

    if divider:

        canvas.setStrokeColor(INFO_DIVIDER_COLOR)
        canvas.setLineWidth(INFO_DIVIDER_WIDTH)

        canvas.line(
            x,
            y - height,
            x + layout.table_width,
            y - height,
        )

    return y - height