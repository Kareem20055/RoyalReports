from dataclasses import dataclass, field


@dataclass
class Employee:

    name: str

    rows: list = field(default_factory=list)