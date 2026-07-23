from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from design.fonts import register_fonts
from design.text import draw_text

register_fonts()

c = canvas.Canvas("test.pdf", pagesize=A4)

# English
draw_text(
    c,
    "English Test - Noto Sans",
    50,
    800,
    size=18,
)

draw_text(
    c,
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    50,
    770,
    size=14,
)

# Arabic
draw_text(
    c,
    "اختبار اللغة العربية",
    550,
    720,
    align="right",
    size=18,
)

draw_text(
    c,
    "أ",
    550,
    690,
    align="right",
    size=18,
)

draw_text(
    c,
    "أحمد",
    550,
    660,
    align="right",
    size=18,
)

draw_text(
    c,
    "إبراهيم",
    550,
    630,
    align="right",
    size=18,
)

draw_text(
    c,
    "آدم",
    550,
    600,
    align="right",
    size=18,
)

draw_text(
    c,
    "مسؤول",
    550,
    570,
    align="right",
    size=18,
)

draw_text(
    c,
    "رئيس",
    550,
    540,
    align="right",
    size=18,
)

draw_text(
    c,
    "فتاة",
    550,
    510,
    align="right",
    size=18,
)

draw_text(
    c,
    "هدى",
    550,
    480,
    align="right",
    size=18,
)

# Bold
draw_text(
    c,
    "أحمد محمد",
    550,
    430,
    align="right",
    bold=True,
    size=20,
)

draw_text(
    c,
    "Royal Reports",
    50,
    430,
    bold=True,
    size=20,
)

c.save()

print("PDF created successfully.")