from design.colors import BLACK

from .normalize_table import normalize_table
from .layout import build_columns
from .header import draw_header
from .body import draw_rows


def draw_data_table(
    canvas,
    headers,
    rows,
    current_y,
    page_width,
    margin,
    header_height=None,
    row_height=None,
    weights=None,
    max_column_widths=None,
    header_background=None,
    header_text_color=BLACK,
    normalize=True,
    show_header=True,
):
    """
    Draw a complete data table.
    """

    if normalize:
        headers, rows, weights, max_column_widths = normalize_table(
            headers=headers,
            rows=rows,
            weights=weights,
            max_column_widths=max_column_widths,
        )

    layout = build_columns(
        headers=headers,
        rows=rows,
        page_width=page_width,
        margin=margin,
        weights=weights,
        max_column_widths=max_column_widths,
    )
    columns = layout.columns
    margin = layout.margin

    if show_header:
        current_y = draw_header(
            canvas=canvas,
            headers=headers,
            columns=columns,
            y=current_y,
            background=header_background,
            text_color=header_text_color,
            margin=margin,
        )

    current_y = draw_rows(
        canvas=canvas,
        rows=rows,
        columns=columns,
        y=current_y,
        margin=margin,
    )

    return current_y