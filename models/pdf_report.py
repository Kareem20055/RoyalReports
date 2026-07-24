from dataclasses import dataclass

from models.employee import Employee
from models.calculated_attendance import CalculatedAttendance
from models.summary import Summary


@dataclass
class PdfReport:

    company: str

    title: str

    date_range: str

    employee: Employee

    attendance: list[CalculatedAttendance]

    summary: Summary