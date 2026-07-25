from core.attendance.calculator import AttendanceCalculator
from core.report.summary_calculator import SummaryCalculator

from models.employee_summary_row import EmployeeSummaryRow
from models.weekly_summary_report import WeeklySummaryReport
from models.settings import Settings


class WeeklySummaryBuilder:
    """
    Build a weekly summary report for all employees.
    """

    def __init__(
        self,
        settings: Settings,
    ):
        self.calculator = AttendanceCalculator(settings)
        self.summary_calculator = SummaryCalculator()

    def build(
        self,
        employees,
        company: str,
        title: str,
        date_range: str,
    ) -> WeeklySummaryReport:

        rows = []

        for employee in employees:

            attendance = self.calculator.calculate_employee(
                employee,
            )

            summary = self.summary_calculator.calculate(
                attendance,
            )

            rows.append(
                EmployeeSummaryRow(
                    employee_name=employee.name,
                    attendance_days=summary.present,
                    absence_days=summary.absent,
                    late_duration=summary.late_minutes,
                    worked_duration=summary.worked_minutes,
                    overtime_duration=summary.overtime_minutes,
                )
            )

        return WeeklySummaryReport(
            company=company,
            title=title,
            date_range=date_range,
            rows=rows,
        )