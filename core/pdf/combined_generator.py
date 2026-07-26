from reportlab.pdfgen import canvas

from design.layout import (
    PAGE_WIDTH,
    PAGE_HEIGHT,
)

from core.pdf.report_generator import ReportGenerator
from core.pdf.weekly_summary_generator import WeeklySummaryGenerator


class CombinedGenerator:

    def __init__(
        self,
        summary_report,
        employee_reports,
        settings,
    ):
        self.summary_report = summary_report
        self.employee_reports = employee_reports
        self.settings = settings

    def generate(
        self,
        output_path,
    ):

        pdf = canvas.Canvas(
            output_path,
            pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        )

        # ==========================
        # Weekly Summary
        # ==========================

        WeeklySummaryGenerator(
            report=self.summary_report,
            settings=self.settings,
        ).render(pdf)

        # Bookmark مخفي للرابط فقط
        pdf.bookmarkPage("weekly_summary")


        # ==========================
        # Employee Reports
        # ==========================

        for index, report in enumerate(self.employee_reports, start=1):

            pdf.showPage()

            # Bookmark مخفي للرابط فقط
            pdf.bookmarkPage(f"employee_{index}")

            ReportGenerator(
                report=report,
                settings=self.settings,
            ).render(pdf)

        pdf.save()