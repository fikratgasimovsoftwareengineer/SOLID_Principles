from domain.interfaces.i_student_repository import IStudentRepository
from domain.models.students import Student
from domain.models.logger import Logger
from typing import Optional,List

logger = Logger("StudentRepository")

class InMemoryStudentRepository(IStudentRepository):
    
    def __init__(self):    
        self._storage:dict = {}
        self._unique_students:set = set()    
    
    def create_student(self, student:Student)->dict:
        if student.id not in self._unique_students:
            self._unique_students.add(student.id)
            self._storage[student.id] = student
            
            Logger.info(f"Lo studente {student.matricola_num} seguente e` stata aggiunto {student.id}")
          
        else:
            Logger.warning(f"Lo studento {student.id} gia presente nella Database")
            return self._storage
       

    def delete_student(self, student_id:int)->dict[int, bool]:
        if student_id in self._unique_students and student_id in self._storage:
            self._storage.pop(student_id)
            self._unique_students.remove(student_id)
            
            logger.info(f"Studente {student_id} eliminato")
        else:
            logger.error(f"Studente {student_id} non esiste nel database")
    
            
    def find_by_id(self, student_id:int)->Optional[Student]:
        if student_id in self._storage:
            return self._storage[student_id]
        logger.warning(f"Studente {student_id} non trovato")
        return None
        
    def find_all(self)->List[Student]:
        return list(self._storage.values())