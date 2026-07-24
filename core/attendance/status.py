from enum import Enum


class AttendanceStatus(Enum):
    PRESENT = "Present"
    LATE = "Late"
    ABSENT = "Absent"