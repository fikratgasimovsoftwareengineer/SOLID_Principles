from domain.models.students import Student
from abc import ABC, abstractmethod
from typing import List,Optional

class IStudentRepository(ABC):
    

    """
    BluePrint per DataBase Operations Management
    """
    @abstractmethod
    def _create_student(self, student:Student):
        pass
        
        
    @abstractmethod
    def _delete_student(self, student_id:int):
        pass
    
    @abstractmethod
    def _find_by_id(self, student_id:int)->Optional[Student]:
        pass
    
    @abstractmethod
    def _find_all(self)->List[Student]:
        pass
        

    