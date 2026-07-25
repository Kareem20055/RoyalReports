from core.attendance.parser import parse_schedule
from core.pdf.formatter import format_shift

from core.pdf.components import (
    section,
    info,
)

from design.layout import (
    PAGE_MARGIN,
    SECTION_SPACING,
)



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
        title="بيانات الموظف",
        current_y=current_y,
        width=width,
    )

    if employee.rows:
        start, end = parse_schedule(employee.rows[0].schedule)
        shift = format_shift(start, end)
    else:
        shift = "--"

    rows = [
        ("اسم الموظف", employee.name),
        ("رقم الموظف", employee.person_id),
        ("الشيفت", shift),
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