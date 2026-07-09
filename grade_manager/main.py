from app.grade_manager import GradeManager
from services.grade_calculator import GradeCalculator
from services.student_repository import InMemoryStudentRepository

def main():
    
    manager = GradeManager(
        repository=InMemoryStudentRepository(),
        grade_calculator = GradeCalculator()
    )
    
    print("=" * 45)
    print("  Grade Manager — SRP + ISP")
    print("=" * 45)
    
    
    manager.add_student(
        student_id=1,
        mat_num="MAT001",
        dipartment="Informatica",
        campo_del_studio="Intelligenza Artificiale"
    )
    
    manager.add_student(
        student_id=2,
        mat_num="MAT002",
        dipartment="Matematica",
        campo_del_studio="Algebra"
    )
    manager.add_student(
        student_id=3,
        mat_num="MAT003",
        dipartment="Economia",
        campo_del_studio="Finanza"
    )
    
    
        
    # ─── aggiunge voti ─────────────────────────────────────────
    manager.create_assigment(1, "Matematica",    [85, 90, 78])
    manager.create_assigment(1, "Algoritmi",     [92, 88, 95])
    manager.create_assigment(2, "Algebra",       [70, 65, 72])
    manager.create_assigment(2, "Analisi",       [80, 75, 68])
    manager.create_assigment(3, "Economia",      [55, 60, 58])
    manager.create_assigment(3, "Statistica",    [45, 50, 52])
    
      
    # ─── lista tutti ───────────────────────────────────────────
    manager.get_all_students()
    
    # ─── elimina studente ──────────────────────────────────────
    manager.remove_student(2)
    
    print("\nDopo eliminazione:")
    manager.get_all_students()
    
if __name__ == "__main__":
    main()