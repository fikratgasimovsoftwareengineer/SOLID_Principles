from domain.interfaces.i_grade_calculator import IGradeCalculator
from domain.interfaces.i_student_repository import IStudentRepository
from domain.models.students import Student
from domain.models.assignment import Assignment
from domain.models.logger import Logger
from typing import List, Optional

logger = Logger("Manager-Orchestrator")

class GradeManager:
    """
        orchestratore
    """
    def __init__(self, 
                 repository:IStudentRepository,
                 grade_calculator:IGradeCalculator):
        
        self._repo = repository
        self._calc = grade_calculator
        
    def add_student(self, student_id, mat_num, dipartment, campo_del_studio):
        
        ### INIT ###
        student = Student(id=student_id,
                          matricola_num=mat_num,
                          dipartimento=dipartment,
                          campo_del_studio=campo_del_studio)
        
        
        ## chiama create student ##
        self._repo._create_student(student)
        logger.info(f"Studente aggiunto")
        
        return student
    
    def remove_student(self, student_id:int):
        student = self._repo._find_by_id(student_id=student_id)
        if not student:
            logger.error(f"Studente {student_id} non trovato")
            
        self._repo._delete_student(student_id)
        logger.info(f"Il studente {student_id} cancellato")
        
    def get_all_students(self):
        
        all_students = self._repo._find_all()
        return all_students
    
    
    #============================================================================
    # ASSIGNMENT HANDLING #
    #=============================================================================
    def create_assigment(self,student_id, materia, voti):
        assignment = Assignment(student_id=student_id, 
                                materia=materia,
                                voti=voti)
        return self._calc.insert_student_assignments(assignment=assignment)
    
    
    def calculate_avverage_score(self,student_id:int):
        get_student_byId = self._repo._find_by_id(student_id)
        if not get_student_byId:
            logger.error(f"Studente By Id {get_student_byId} not esiste")
            
        get_average_per_studente = self._calc.get_average(get_student_byId)
        
        assert(get_average_per_studente) == type(float)
        
        return get_average_per_studente
    
    def insert_grade_per_studente(self, score:int):
        return self._calc.assign_score(score=score)
        
        