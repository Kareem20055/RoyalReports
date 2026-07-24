from dataclasses import dataclass
from datetime import time


@dataclass
class Summary:

    present: int = 0
    late: int = 0
    absent: int = 0

    worked_minutes: int = 0
    late_minutes: int = 0
    early_leave_minutes: int = 0
    overtime_minutes: int = 0

    average_check_in: time | None = None
    average_check_out: time | None = None