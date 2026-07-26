from reportlab.pdfgen import canvas

from design.layout import (
    PAGE_WIDTH,
    PAGE_HEIGHT,
)

from core.pdf import (
    header,
    employee_info,
    summary,
    attendance_table,
    footer,
)


class ReportGenerator:
    """
    Generate attendance PDF reports.
    """

    def __init__(
        self,
        report,
        settings,
    ):
        self.report = report
        self.settings = settings

    def generate(
        self,
        output_path,
    ):

        pdf = canvas.Canvas(
            output_path,
            pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
        )

        self.render(pdf)

        pdf.save()

    def render(
        self,
        pdf,
    ):
        current_y = header.draw(
            canvas=pdf,
            report=self.report,
            settings=self.settings,
            width=PAGE_WIDTH,
            height=PAGE_HEIGHT,
        )

        current_y = employee_info.draw(
            canvas=pdf,
            employee=self.report.employee,
            current_y=current_y,
            width=PAGE_WIDTH,
        )

        current_y = attendance_table.draw(
            canvas=pdf,
            attendance=self.report.attendance,
            current_y=current_y,
            width=PAGE_WIDTH,
        )

        current_y = summary.draw(
            canvas=pdf,
            summary=self.report.summary,
            current_y=current_y,
            width=PAGE_WIDTH,
        )

        footer.draw(
            canvas=pdf,
            width=PAGE_WIDTH,
        )