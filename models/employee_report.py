from dataclasses import dataclass

from models.employee import Employee
from models.summary import Summary
from models.calculated_attendance import CalculatedAttendance


@dataclass
class EmployeeReport:

    company: str

    title: str

    date_range: str

    employee: Employee

    attendance: list[CalculatedAttendance]

    summary: Summary