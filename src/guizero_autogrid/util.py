from dataclasses import dataclass
from typing import Tuple


class NextRow:
    pass


class Auto:
    pass


@dataclass
class AutogridState:
    current_col: int
    current_row: int
    spacing: int | Tuple[int] = 0
