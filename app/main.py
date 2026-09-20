from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from app.database import sesson_local
from app.model import User
from app.schema import userCreate


app = FastAPI()


@app.post("/users")
def create_user(userdata : userCreate):

    db = sesson_local()

    user = User(
        name=userdata.name,
        email=userdata.email
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

@app.get("/users")
def getData():

    db = sesson_local()

    user = db.query(User).all()

    id1 = db.query(User.name).filter(
        User.id == 1
    ).scalar()

    # .all()     # list of results
    # .first()   # first result/row
    # .scalar()  # actual single value

    db.close()

    return user,id1

@app.get("/users/{userid}")
def getExact(userid : int):

    db = sesson_local()

    user = db.query(User).filter(
        User.id == userid
    ).scalar()

    db.close()

    if not user:
        raise HTTPException(status_code=400,
                            detail="User Does Not Exist !"
        )
    
    return user
