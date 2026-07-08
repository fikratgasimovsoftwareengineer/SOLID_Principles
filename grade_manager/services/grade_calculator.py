from domain.interfaces.i_grade_calculator import IGradeCalculator
from domain.models.assignment import Assignment
from typing import List
from domain.models.logger import Logger

logger = Logger("GradeCalculator")

class GradeCalculator(IGradeCalculator):
    
    def __init__(self):
        self._assigment_storage:dict = {}
    
        
         
    def insert_student_assignments(self, assignment:Assignment)->List[Assignment]:
        if assignment.student_id not in self._assigment_storage:
            self._assigment_storage[assignment.student_id] = []
        
        self._assigment_storage[assignment.student_id].append(assignment)
        
        logger.info(f"Aggiunto materia {assignment.materia} "
                    f"per studente {assignment.student_id}")
        
        return self._assigment_storage[assignment.student_id]
    
    
    def get_average(self, student_id:int):
        if student_id not in self._assigment_storage:
            logger.warning(f"Lo studente {student_id} cercato non esiste ")        
            return 0.0
        
        all_voti = []
        for assignment in self._assigment_storage[student_id]:
            all_voti.extend(assignment.voti)   # ✓ prendi i voti dall'assignment
            
        if not all_voti:
            return 0.0
            
        return sum(all_voti) / len(all_voti)
    
    
    def assign_score(self, score: int) -> str:
        if score >= 90:   return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else:             return "E"