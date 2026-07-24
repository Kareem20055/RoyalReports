from i18n import t

from core.pdf.components import (
    section,
    table,
)

from design.layout import (
    SECTION_SPACING,
    TABLE_ROW_HEIGHT,
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

    current_y = table.draw_key_value_table(
        canvas=canvas,
        rows=rows,
        y=current_y,
        page_width=width,
        row_height=TABLE_ROW_HEIGHT,
    )

    current_y -= SECTION_SPACING

    return current_y