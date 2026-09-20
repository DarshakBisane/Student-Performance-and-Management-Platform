from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from app.database import sesson_local
from app.model import User


app = FastAPI()


@app.post("/users")
def create_user(name : str, email : str):

    db = sesson_local()

    user = User(
        name=name,
        email=email
    )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()

        raise HTTPException(status_code=400,
                      detail="User already Exist!"
        )

    finally:    
        db.close()

    return user