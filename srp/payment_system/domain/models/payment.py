from dataclasses import dataclass
from datetime import datetime

@dataclass
class Payment:
    id:     str
    amount: float
    status: str
    created_at: str = ""
    
    def __post_init__(self):
        self.created_at = datetime.now().isoformat()