# data_model.py

from dataclasses import dataclass
from typing import Optional

# data model for one line of lean code: We save the goal before and after the line
@dataclass
class LeanLine:
    lean_line: str
    goal_before: [str]
    goal_after: [str]

    
# data model for one proof step: One latex-comment, and possibly many lines of lean code
@dataclass
class ProofStep:
    latex_comment: str
    lean_code: [LeanLine]

