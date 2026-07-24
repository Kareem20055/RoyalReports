from dataclasses import dataclass

@dataclass
class AttendanceRow:

    date: str = ""

    weekday: str = ""

    schedule: str = ""

    check_in: str = ""

    check_out: str = ""