from core.attendance.status import AttendanceStatus
from core.attendance.time_utils import (
    add_minutes,
    minutes_between,
)

from models.parsed_attendance import ParsedAttendance
from models.settings import Settings


def calculate_late_minutes(
    attendance: ParsedAttendance,
    status: AttendanceStatus,
    settings: Settings,
) -> int:

    if status != AttendanceStatus.LATE:
        return 0

    if attendance.shift_start is None:
        return 0

    if attendance.check_in is None:
        return 0

    grace_time = add_minutes(
        attendance.shift_start,
        settings.late_grace_minutes,
    )

    return max(
        minutes_between(
            grace_time,
            attendance.check_in,
        ),
        0,
    )