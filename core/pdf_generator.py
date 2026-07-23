from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os


class PDFGenerator:

    def __init__(self, settings):
        self.settings = settings

    # ==============================
    # Header
    # ==============================

    def draw_header(self, company_name):

        return {
            "company_name": company_name
        }

    # ==============================
    # Report Information
    # ==============================

    def draw_report_info(self, report):

        return {
            "title": report.title,
            "date_range": report.date_range
        }

    # ==============================
    # Employee Information
    # ==============================

    def draw_employee_info(self, employee):

        return employee

    # ==============================
    # Attendance Table
    # ==============================

    def draw_table(self, employee):

        return employee.rows

    # ==============================
    # Footer
    # ==============================

    def draw_footer(self):

        return {}

    # ==============================
    # Generate PDF
    # ==============================

    def generate(self, report):

        output_folder = self.settings.get(
            "output_folder",
            "output"
        )

        os.makedirs(output_folder, exist_ok=True)

        pdf_path = os.path.join(
            output_folder,
            "Royal_Report.pdf"
        )

        c = canvas.Canvas(
            pdf_path,
            pagesize=A4
        )

        width, height = A4

        # ---------------- Header ----------------

        header = self.draw_header(
            self.settings.get(
                "company",
                "Royal Glass"
            )
        )

        c.setFont(
            "Helvetica-Bold",
            18
        )

        c.drawCentredString(
            width / 2,
            height - 50,
            header["company_name"]
        )

        # ---------------- Report Info ----------------

        info = self.draw_report_info(report)

        c.setFont(
            "Helvetica",
            12
        )

        c.drawCentredString(
            width / 2,
            height - 75,
            info["title"]
        )

        c.drawCentredString(
            width / 2,
            height - 95,
            info["date_range"]
        )

        # ---------------- Temporary Message ----------------

        c.setFont(
            "Helvetica",
            10
        )

        c.drawString(
            50,
            height - 140,
            "Royal Reports PDF Engine Ready..."
        )

        # عدد الموظفين (للتأكد أن البيانات وصلت)
        c.drawString(
            50,
            height - 160,
            f"Employees: {len(report.employees)}"
        )

        c.save()

        return pdf_path