from core.pdf.components import section, table

from core.pdf.formatter import (
    format_date,
    format_minutes,
    format_time,
)

from design.colors import TABLE_HEADER_BG

from design.layout import (
    PAGE_WIDTH,
    PAGE_MARGIN,
    TABLE_HEADER_HEIGHT,
    TABLE_ROW_HEIGHT,
)

from models.calculated_attendance import CalculatedAttendance


HEADERS = [
    "التاريخ",
    "اليوم",
    "الحضور",
    "الانصراف",
    "ساعات العمل",
    "التأخير",
    "الانصراف المبكر",
    "الساعات الإضافية",
    "الحالة",
]

WEIGHTS = [
    1.4,
    1.2,
    1.2,
    1.2,
    1.2,
    1.0,
    1.0,
    1.0,
    1.3,
]

MAX_WIDTHS = [
    90,   # التاريخ
    60,   # اليوم
    70,   # الحضور
    70,   # الانصراف
    80,   # ساعات العمل
    60,   # التأخير
    90,   # الانصراف المبكر
    90,   # العمل الإضافي
    60,   # الحالة
]

STATUSS = {
    "present": "حاضر",
    "absent": "غائب",
    "late": "متأخر",
    "holiday": "إجازة",
}


def draw(
    canvas,
    attendance: list[CalculatedAttendance],
    current_y,
    width,
):
    current_y = section.draw(
        canvas=canvas,
        title="الحضور",
        current_y=current_y,
        width=width,
    )

    rows = []

    for item in attendance:

        rows.append([
            format_date(item.date),
            item.weekday,
            format_time(item.check_in),
            format_time(item.check_out),
            format_minutes(item.worked_minutes),
            format_minutes(item.late_minutes),
            format_minutes(item.early_leave_minutes),
            format_minutes(item.overtime_minutes),
            STATUSS.get(
                item.status.value.lower(),
                item.status.value,
            ),
        ])

    return table.draw_data_table(
        canvas=canvas,
        headers=HEADERS,
        rows=rows,
        current_y=current_y,
        page_width=PAGE_WIDTH,
        margin=PAGE_MARGIN,
        header_height=TABLE_HEADER_HEIGHT,
        row_height=TABLE_ROW_HEIGHT,
        weights=WEIGHTS,
        max_column_widths=MAX_WIDTHS,
        header_background=TABLE_HEADER_BG,
    )