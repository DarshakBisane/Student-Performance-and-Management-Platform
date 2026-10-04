from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.database import sesson_local
from app.model import Student
from app.schema import CreateStudent

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/")
def createStudent(student_data : CreateStudent):

    db = sesson_local()

    student = Student(
        enrollment_no = student_data.enrollment_no,
        name = student_data.name,
        email = student_data.email,
        phone = student_data.phone,
        department = student_data.department,
        semester = student_data.semester
    )

    try:
        db.add(student)
        db.commit()
        db.refresh(student)
    
    except IntegrityError:
        db.rollback()
        db.close()

        raise HTTPException(
            status_code=400,
            detail="Something is wrong while inserting the Data !"  
        )

    db.close()

    return {
        "Message" : "Student created Successfully",
        "Student" : student.id
    }
