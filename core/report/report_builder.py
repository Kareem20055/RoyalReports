from core.report.summary_calculator import SummaryCalculator

from models.employee import Employee
from models.pdf_report import PdfReport
from models.settings import Settings

from core.attendance.calculator import AttendanceCalculator


class ReportBuilder:
    """
    Build a PDF-ready report for a single employee.
    """

    def __init__(
        self,
        settings: Settings,
    ):
        self.calculator = AttendanceCalculator(settings)
        self.summary_calculator = SummaryCalculator()

    def build(
        self,
        employee: Employee,
        company: str,
        title: str,
        date_range: str,
    ) -> PdfReport:

        attendance = self.calculator.calculate_employee(
            employee,
        )

        summary = self.summary_calculator.calculate(
            attendance,
        )

        return PdfReport(
            company=company,
            title=title,
            date_range=date_range,
            employee=employee,
            attendance=attendance,
            summary=summary,
        )