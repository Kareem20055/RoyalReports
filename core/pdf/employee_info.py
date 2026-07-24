from core.attendance.parser import parse_schedule
from core.pdf.formatter import format_shift

from core.pdf.components import (
    section,
    table,
)

from design.layout import (
    SECTION_SPACING,
    TABLE_ROW_HEIGHT,
)

from i18n import t


def draw(
    canvas,
    employee,
    current_y,
    width,
):
    """
    Draw employee information section.
    """

    current_y = section.draw(
        canvas=canvas,
        title=t("employee_information"),
        current_y=current_y,
        width=width,
    )

    if employee.rows:
        start, end = parse_schedule(employee.rows[0].schedule)
        shift = format_shift(start, end)
    else:
        shift = "--"

    rows = [
        (t("employee_name"), employee.name),
        (t("employee_id"), employee.person_id),
        (t("shift"), shift),
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