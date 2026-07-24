from design.colors import BLACK

from i18n import t

from .data_table import draw_data_table


def draw_key_value_table(
    canvas,
    rows,
    y,
    page_width,
    row_height=None,
):
    """
    Draw a two-column key/value table.
    """

    headers = [
        t("field"),
        t("value"),
    ]

    table_rows = []

    for key, value in rows:
        table_rows.append(
            [
                key,
                value,
            ]
        )

    return draw_data_table(
        canvas=canvas,
        headers=headers,
        rows=table_rows,
        current_y=y,
        page_width=page_width,
        margin=0,
        weights=[0.65, 0.35],
        max_column_widths=None,
        header_background=None,
        header_text_color=BLACK,
        normalize=False,   # <-- السطر الجديد
    )