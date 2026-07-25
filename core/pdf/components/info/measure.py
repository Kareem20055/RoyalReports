from design.fonts import BODY_SIZE

from design.info import (
    INFO_ROW_HEIGHT,
    LABEL_PADDING,
    VALUE_PADDING,
)

from design.text import (
    wrap_text,
    text_height,
)


def measure_rows(
    rows,
    layout,
):
    """
    Measure info rows.

    Returns:
        [
            {
                "height": ...,
                "label": [...],
                "value": [...],
            }
        ]
    """

    measured_rows = []

    for label, value in rows:

        label_width = layout.label_width - (LABEL_PADDING * 2)
        value_width = layout.value_width - (VALUE_PADDING * 2)

        wrapped_label = wrap_text(
            text=str(label),
            max_width=label_width,
            bold=True,
            size=BODY_SIZE,
        )

        wrapped_value = wrap_text(
            text=str(value),
            max_width=value_width,
            bold=False,
            size=BODY_SIZE,
        )

        label_height = text_height(
            text=str(label),
            max_width=label_width,
            bold=True,
            size=BODY_SIZE,
        )

        value_height = text_height(
            text=str(value),
            max_width=value_width,
            bold=False,
            size=BODY_SIZE,
        )

        row_height = max(
            INFO_ROW_HEIGHT,
            label_height + 8,
            value_height + 8,
        )

        measured_rows.append(
            {
                "height": row_height,
                "label": wrapped_label,
                "value": wrapped_value,
            }
        )

    return measured_rows