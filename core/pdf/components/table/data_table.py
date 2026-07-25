from design.colors import BLACK
from design.layout import PAGE_MARGIN

from core.pdf.layout_engine import LayoutEngine

from .cell import draw_cell
from .measure import (
    measure_header,
    measure_rows,
)


def build_columns(
    headers,
    rows,
    page_width,
    margin,
    weights,
    max_column_widths,
):
    return LayoutEngine.data_table_layout(
        headers=headers,
        rows=rows,
        page_width=page_width,
        margin=margin,
        weights=weights,
        max_column_widths=max_column_widths,
    )


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
    if len(columns) != len(values):
        raise ValueError(
            "columns and values must have the same length."
        )

    table_width = sum(width for _, width in columns)

    x = margin + table_width

    for value, (_, column_width) in zip(values, columns):

        x -= column_width

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

def draw_header(
    canvas,
    headers,
    columns,
    y,
    background,
    text_color,
    margin,
):
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


def draw_rows(
    canvas,
    rows,
    columns,
    y,
    margin,
):
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
            margin=margin,
        )

        y -= row["height"]

    return y

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
    show_header=True,
):
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