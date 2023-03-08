from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Jijo",
        "age": 25,
        "specialization": "Computer Science and Engineering",
    }
}

class Student(BaseModel):
    name: str
    age: int
    specialization: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    specialization: Optional[str] = None

@app.get("/")
def index():
    return {"name": "Jijo"}


@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(None, description="ID of the student", gt=0, lt=10)
):
    return students[student_id]


@app.get("/get-by-name")
def get_student(*, student_id: int, name: Optional[str] = None, test:int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"data": "Not Found"}


@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {'error': 'Student Exists'}
    
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {'error': 'Student Doesn\'t Exist'}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.specialization != None:
        students[student_id].specialization = student.specialization

    return students[student_id]


@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {'error': 'Student Doesn\'t Exist'}
    
    del students[student_id]
    return {'message': 'Student Deleted Successfully'}

