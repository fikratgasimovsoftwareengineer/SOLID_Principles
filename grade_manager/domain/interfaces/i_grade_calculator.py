from abc import ABC,abstractmethod
from typing import List 
from domain.models.assignment import Assignment
from domain.models.logger import Logger

class IGradeCalculator(ABC):
    
    @abstractmethod
    def insert_student_assignments(self, assignment:Assignment)->List[Assignment]:
        pass
    
    @abstractmethod
    def get_average(self, student_id:int)->float:
        pass
    
    @abstractmethod
    def assign_score(self,id, score)->str:
        pass
    