from design.colors import (
    BLACK,
    TABLE_HEADER_BG,
)

from design.layout import PAGE_MARGIN

from core.pdf.components.table.data_table import draw_data_table
from core.pdf.formatter import format_minutes


def draw(
    canvas,
    rows,
    current_y,
    width,
):
    headers = [
        "الموظف",
        "الحضور",
        "الغياب",
        "التأخير",
        "ساعات العمل",
        "الإضافي",
    ]

    table_rows = []

    for row in rows:

        table_rows.append(
            [
                row.employee_name,
                row.attendance_days,
                row.absence_days,
                format_minutes(row.late_duration),
                format_minutes(row.worked_duration),
                format_minutes(row.overtime_duration),
            ]
        )

    return draw_data_table(
        canvas=canvas,
        headers=headers,
        rows=table_rows,
        current_y=current_y,
        page_width=width,
        margin=PAGE_MARGIN,
        weights=[
            3.5,
            1.0,
            1.0,
            1.6,
            1.8,
            1.6,
        ],
        header_background=TABLE_HEADER_BG,
        header_text_color=BLACK,
    )