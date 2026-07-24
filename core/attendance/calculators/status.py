from core.attendance.status import AttendanceStatus
from core.attendance.time_utils import (
    add_minutes,
    is_after,
)

from models.parsed_attendance import ParsedAttendance
from models.settings import Settings


def calculate_status(
    attendance: ParsedAttendance,
    settings: Settings,
) -> AttendanceStatus:

    if attendance.shift_start is None:
        return AttendanceStatus.ABSENT

    if attendance.check_in is None:
        return AttendanceStatus.ABSENT

    grace_time = add_minutes(
        attendance.shift_start,
        settings.late_grace_minutes,
    )

    absence_time = add_minutes(
        attendance.shift_start,
        settings.absence_after_minutes,
    )

    if is_after(
        attendance.check_in,
        absence_time,
    ):
        return AttendanceStatus.ABSENT

    if is_after(
        attendance.check_in,
        grace_time,
    ):
        return AttendanceStatus.LATE

    return AttendanceStatus.PRESENT