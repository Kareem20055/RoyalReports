from dataclasses import dataclass
from datetime import datetime


@dataclass
class ParsedAttendance:
    date: datetime
    weekday: str
    shift_start: datetime
    shift_end: datetime
    check_in: datetime | None
    check_out: datetime | None