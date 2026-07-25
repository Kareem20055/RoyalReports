from i18n import t

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
        title=t("summary"),
        current_y=current_y,
        width=width,
    )

    rows = [
        (t("present_days"), summary.present),
        (t("late_days"), summary.late),
        (t("absent_days"), summary.absent),

        (t("worked_time"), format_minutes(summary.worked_minutes)),
        (t("late_time"), format_minutes(summary.late_minutes)),
        (t("early_leave_time"), format_minutes(summary.early_leave_minutes)),
        (t("overtime_time"), format_minutes(summary.overtime_minutes)),

        (t("average_check_in"), format_time(summary.average_check_in)),
        (t("average_check_out"), format_time(summary.average_check_out)),
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