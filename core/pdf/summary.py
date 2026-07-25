from core.pdf.components import (
    section,
    info,
)

from design.layout import (
    PAGE_MARGIN,
    SECTION_SPACING,
)

from models.summary import Summary

from core.pdf.formatter import (
    format_minutes,
    format_time,
)


def draw(
    canvas,
    summary: Summary,
    current_y: float,
    width: float,
) -> float:

    current_y = section.draw(
        canvas=canvas,
        title="الملخص",
        current_y=current_y,
        width=width,
    )

    rows = [
        ("أيام الحضور", summary.present),
        ("أيام التأخير", summary.late),
        ("أيام الغياب", summary.absent),

        ("إجمالي ساعات العمل", format_minutes(summary.worked_minutes)),
        ("إجمالي التأخير", format_minutes(summary.late_minutes)),
        ("إجمالي الانصراف المبكر", format_minutes(summary.early_leave_minutes)),
        ("إجمالي العمل الإضافي", format_minutes(summary.overtime_minutes)),

        ("متوسط وقت الحضور", format_time(summary.average_check_in)),
        ("متوسط وقت الانصراف", format_time(summary.average_check_out)),
    ]

    current_y = info.draw_info_list(
        canvas=canvas,
        rows=rows,
        current_y=current_y,
        page_width=width,
        margin=PAGE_MARGIN,
    )

    current_y -= SECTION_SPACING

    return current_y