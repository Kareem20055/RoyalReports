from core.attendance.parser import parse_attendance

from core.attendance.calculators.status import calculate_status
from core.attendance.calculators.worked import calculate_worked_minutes
from core.attendance.calculators.late import calculate_late_minutes
from core.attendance.calculators.early_leave import (
    calculate_early_leave_minutes,
)
from core.attendance.calculators.overtime import (
    calculate_overtime_minutes,
)

from models.employee import Employee
from models.parsed_attendance import ParsedAttendance
from models.calculated_attendance import CalculatedAttendance
from models.settings import Settings


class AttendanceCalculator:

    def __init__(self, settings: Settings):
        self.settings = settings

    def calculate(
        self,
        attendance: ParsedAttendance,
    ) -> CalculatedAttendance:

        status = calculate_status(
            attendance,
            self.settings,
        )

        return CalculatedAttendance(
            date=attendance.date,
            weekday=attendance.weekday,
            shift_start=attendance.shift_start,
            shift_end=attendance.shift_end,
            check_in=attendance.check_in,
            check_out=attendance.check_out,
            worked_minutes=calculate_worked_minutes(
                attendance,
                status,
                self.settings,
            ),
            late_minutes=calculate_late_minutes(
                attendance,
                status,
                self.settings,
            ),
            early_leave_minutes=calculate_early_leave_minutes(
                attendance,
                status,
            ),
            overtime_minutes=calculate_overtime_minutes(
                attendance,
                status,
            ),
            status=status,
        )

    def calculate_employee(
        self,
        employee: Employee,
    ) -> list[CalculatedAttendance]:

        results = []

        for row in employee.rows:

            parsed = parse_attendance(row)

            results.append(
                self.calculate(parsed)
            )

        return results