from pydantic import BaseModel
from typing import List

class Assignment(BaseModel):
    student_id: int
    materia:    str
    voti:       List[int]