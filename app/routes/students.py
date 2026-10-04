from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.database import sesson_local
from app.model import Student
from app.schema import CreateStudent, UpdateStudent

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

@router.get("/")
def getStudent():

    db = sesson_local()

    student = db.query(Student).all()

    db.close()

    return student

@router.get("/{s_id}")
def getSpecificStudent(s_id : int):

    db = sesson_local()

    student = db.query(Student).filter(
        Student.id == s_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=400,
            detail="Student not Found !"
        )

    db.close()

    return student

@router.patch("/{s_id}")
def updateStudent(s_id : int, student_data : UpdateStudent):

    db = sesson_local()

    student = db.query(Student).filter(
        Student.id == s_id
    ).first()

    if not student:
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Student Not Found !"
        )

    update_data = student_data.model_dump(
        exclude_unset=True
    )

    for key,value in update_data.items():
        setattr(student, key, value)

    try:
        db.commit()
        db.refresh(student)

    except IntegrityError:
        db.rollback()
        db.close()

        raise HTTPException(
            status_code=400,
            detail="Something is Wrong while Updating Data !"
        )
    db.close()

    return student


@router.delete("/{s_id}")
def deleteStudent(s_id : int):

    db = sesson_local()

    student = db.query(Student).filter(
        Student.id == s_id
    ).first()

    try:

        db.delete(student)
        db.commit()

    except IntegrityError:

        db.rollback()
        db.close()

    db.close()

    return {
        "Message" : "Student record deleted from Databse"
    }