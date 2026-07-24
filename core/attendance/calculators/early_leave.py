from core.attendance.status import AttendanceStatus
from core.attendance.time_utils import (
    is_before,
    minutes_between,
)

from models.parsed_attendance import ParsedAttendance


def calculate_early_leave_minutes(
    attendance: ParsedAttendance,
    status: AttendanceStatus,
) -> int:

    if status == AttendanceStatus.ABSENT:
        return 0

    if attendance.shift_end is None:
        return 0

    if attendance.check_out is None:
        return 0

    if not is_before(
        attendance.check_out,
        attendance.shift_end,
    ):
        return 0

    return max(
        minutes_between(
            attendance.check_out,
            attendance.shift_end,
        ),
        0,
    )