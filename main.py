from pathlib import Path
import traceback
import customtkinter as ctk
from tkinter import filedialog, messagebox
from core.report.splitter import ReportSplitter
from core.report.report_builder import ReportBuilder
from core.pdf.report_generator import ReportGenerator
from core.settings.loader import load_settings, save_settings
from design.fonts import register_fonts
from core.report.weekly_summary_builder import WeeklySummaryBuilder
from core.pdf.weekly_summary_generator import WeeklySummaryGenerator
from core.report.date_range import build_folder_name
from core.pdf.combined_generator import CombinedGenerator


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

register_fonts()

settings = load_settings()
save_settings(settings)

splitter = ReportSplitter()
builder = ReportBuilder(settings)
weekly_builder = WeeklySummaryBuilder(settings)


app = ctk.CTk()

app.title("Royal Reports")
app.geometry("700x260")
app.resizable(False, False)


# ==============================
# Browse
# ==============================

def browse():

    file = filedialog.askopenfilename(
        title="Select iVMS Report",
        filetypes=[("Excel Files", "*.xlsx")],
    )

    if file:
        entry.delete(0, "end")
        entry.insert(0, file)


# ==============================
# Generate
# ==============================

def generate():

    file = entry.get().strip()

    if not file:

        messagebox.showerror(
            "Error",
            "Please choose an Excel report first.",
        )

        return

    try:

        report = splitter.split(file)

        base_output = Path("output")
        base_output.mkdir(exist_ok=True)

        folder_name = report.date_range

        # إزالة أي حروف غير صالحة في أسماء المجلدات على ويندوز
        for ch in '<>:"/\\|?*':
            folder_name = folder_name.replace(ch, "-")

        if not folder_name:
            folder_name = "Unknown Period"

        output_dir = base_output / folder_name
        output_dir.mkdir(exist_ok=True)

        pdf_count = 0
        employee_reports = []

        # ==========================
        # Generate Employee Reports
        # ==========================

        for employee in report.employees:

            pdf_report = builder.build(
                employee=employee,
                company=report.company,
                title=report.title,
                date_range=report.date_range,
            )

            employee_reports.append(pdf_report)

            pdf_path = output_dir / f"{employee.name}.pdf"

            ReportGenerator(
                pdf_report,
                settings,
            ).generate(
                str(pdf_path),
            )

            pdf_count += 1

        # ==========================
        # Weekly Summary
        # ==========================

        weekly_report = weekly_builder.build(
            employees=report.employees,
            company=report.company,
            title="التقرير الأسبوعي",
            date_range=report.date_range,
        )

        weekly_pdf_path = output_dir / "التقرير الأسبوعي.pdf"

        WeeklySummaryGenerator(
            weekly_report,
            settings,
        ).generate(
            str(weekly_pdf_path),
        )

        # ==========================
        # Combined Report
        # ==========================

        CombinedGenerator(
            summary_report=weekly_report,
            employee_reports=employee_reports,
            settings=settings,
        ).generate(
            str(output_dir / "التقرير الكامل.pdf")
        )

        messagebox.showinfo(
            "Finished",
            f"""Done Successfully

Employees : {pdf_count}

PDFs Saved To :

{output_dir.resolve()}
""",
        )

    except Exception:

        traceback.print_exc()
        raise



# ==============================
# UI
# ==============================

title = ctk.CTkLabel(
    app,
    text="Royal Reports",
    font=("Arial", 26, "bold"),
)

title.pack(pady=20)

entry = ctk.CTkEntry(
    app,
    width=520,
)

entry.pack()

browse_btn = ctk.CTkButton(
    app,
    text="Browse",
    width=150,
    command=browse,
)

browse_btn.pack(pady=10)

generate_btn = ctk.CTkButton(
    app,
    text="Generate",
    width=150,
    command=generate,
)

generate_btn.pack()

app.mainloop()