from core.attendance.status import AttendanceStatus
from core.attendance.time_utils import (
    add_minutes,
    minutes_between,
)

from models.parsed_attendance import ParsedAttendance
from models.settings import Settings


def calculate_worked_minutes(
    attendance: ParsedAttendance,
    status: AttendanceStatus,
    settings: Settings,
) -> int:

    if status == AttendanceStatus.ABSENT:

        if (
            attendance.check_out is None
            or attendance.shift_start is None
        ):
            return 0

        if not settings.calculate_from_absence_time_if_checkout_only:
            return 0

        absence_time = add_minutes(
            attendance.shift_start,
            settings.absence_after_minutes,
        )

        return max(
            minutes_between(
                absence_time,
                attendance.check_out,
            ),
            0,
        )

    if attendance.check_in is None:
        return 0

    if attendance.check_out is None:

        if attendance.shift_end is None:
            return 0

        return max(
            minutes_between(
                attendance.check_in,
                attendance.shift_end,
            ),
            0,
        )

    # حساب ساعات العمل داخل حدود الشيفت فقط

    work_start = attendance.check_in
    work_end = attendance.check_out

    if attendance.shift_start is not None and work_start < attendance.shift_start:
        work_start = attendance.shift_start

    if attendance.shift_end is not None and work_end > attendance.shift_end:
        work_end = attendance.shift_end

    return max(
        minutes_between(
            work_start,
            work_end,
        ),
        0,
    )