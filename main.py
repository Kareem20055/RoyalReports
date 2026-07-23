import customtkinter as ctk
from tkinter import filedialog, messagebox

from core.splitter import ReportSplitter
from core.pdf_generator import PDFGenerator
from core.settings_manager import SettingsManager


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

settings = SettingsManager.load()

splitter = ReportSplitter()
pdf = PDFGenerator(settings)

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
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if file:
        entry.delete(0, "end")
        entry.insert(0, file)


# ==============================
# Generate
# ==============================

def generate():

    file = entry.get().strip()

    if file == "":

        messagebox.showerror(
            "Error",
            "Please choose an Excel report first."
        )

        return

    try:

        # إنشاء ملف Excel
        output, employees = splitter.split(file)

        report_data = {
            "title": "Attendance Report",
            "date_range": ""
        }

        # إنشاء أول PDF تجريبي
        pdf.generate(report_data)

        messagebox.showinfo(
            "Finished",
            f"""Done Successfully

Employees : {employees}

Excel Saved To :

{output}

PDF Saved To :

output/Royal_Report.pdf
"""
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# ==============================
# UI
# ==============================

title = ctk.CTkLabel(
    app,
    text="Royal Reports",
    font=("Arial", 26, "bold")
)

title.pack(pady=20)

entry = ctk.CTkEntry(
    app,
    width=520
)

entry.pack()

browse_btn = ctk.CTkButton(
    app,
    text="Browse",
    width=150,
    command=browse
)

browse_btn.pack(pady=10)

generate_btn = ctk.CTkButton(
    app,
    text="Generate",
    width=150,
    command=generate
)

generate_btn.pack()

app.mainloop()