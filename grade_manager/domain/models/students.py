from pydantic import BaseModel

class Student(BaseModel):
    
    id:                 int
    matricola_num:      str
    dipartimento:       str
    campo_del_studio:   str       
    
    