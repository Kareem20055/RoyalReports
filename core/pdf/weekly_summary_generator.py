from reportlab.pdfgen import canvas

from design.layout import (
    PAGE_WIDTH,
    PAGE_HEIGHT,
)

from core.pdf import (
    header,
    footer,
    weekly_summary_table,
)


class WeeklySummaryGenerator:

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

        current_y = header.draw(
            canvas=pdf,
            report=self.report,
            settings=self.settings,
            width=PAGE_WIDTH,
            height=PAGE_HEIGHT,
        )

        current_y = weekly_summary_table.draw(
            canvas=pdf,
            rows=self.report.rows,
            current_y=current_y,
            width=PAGE_WIDTH,
        )

        footer.draw(
            canvas=pdf,
            width=PAGE_WIDTH,
        )

        pdf.save()