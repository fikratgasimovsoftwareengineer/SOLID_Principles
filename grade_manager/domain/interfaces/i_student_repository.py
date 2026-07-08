from domain.models.students import Student
from abc import ABC, abstractmethod
from typing import List,Optional

class IStudentRepository(ABC):
    

    """
    BluePrint per DataBase Operations Management
    """
    @abstractmethod
    def create_student(self, student:Student):
        pass
        
        
    @abstractmethod
    def delete_student(self, student_id:int)->str:
        pass
    
    @abstractmethod
    def find_by_id(self, student_id:int)->Optional[Student]:
        pass
    
    @abstractmethod
    def find_all(self)->List[Student]:
        pass
        

    