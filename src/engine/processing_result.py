from typing import Any
from dataclasses import dataclass

@dataclass
class ProcessingResult:
    
    suceeded: bool
    payload: Any