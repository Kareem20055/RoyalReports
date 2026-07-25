from dataclasses import dataclass

from models.employee_summary_row import EmployeeSummaryRow


@dataclass
class WeeklySummaryReport:

    company: str

    title: str

    date_range: str

    rows: list[EmployeeSummaryRow]