from dataclasses import dataclass
from datetime import datetime

from core.attendance.status import AttendanceStatus


@dataclass
class CalculatedAttendance:

    date: datetime

    weekday: str

    check_in: datetime | None

    check_out: datetime | None

    worked_minutes: int

    late_minutes: int

    early_leave_minutes: int

    overtime_minutes: int

    status: AttendanceStatus

    shift_start: datetime | None
    
    shift_end: datetime | None