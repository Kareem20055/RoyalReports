from dataclasses import dataclass, field
from .employee import Employee


@dataclass
class Report:

    company: str = ""

    title: str = "تقرير الحضور"

    date_range: str = ""

    employees: list[Employee] = field(default_factory=list)

    excel_path: str = ""