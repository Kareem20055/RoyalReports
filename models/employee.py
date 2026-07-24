from dataclasses import dataclass, field
from models.attendance_row import AttendanceRow


@dataclass
class Employee:

    name: str
    person_id: str = ""
    department: str = ""
    position: str = ""

    rows: list[AttendanceRow] = field(default_factory=list)