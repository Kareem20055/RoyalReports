from dataclasses import dataclass


@dataclass
class EmployeeSummaryRow:

    employee_name: str

    attendance_days: int
    absence_days: int

    late_duration: int
    worked_duration: int
    overtime_duration: int