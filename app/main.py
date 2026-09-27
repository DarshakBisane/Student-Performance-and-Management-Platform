from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from app.database import sesson_local
from app.model import User
from app.schema import userCreate, userUpdate


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


@app.put("/users/{userid}")
def update_user(userid : int, user_data : userUpdate):

    db = sesson_local()

    user = db.query(User).filter(User.id  == userid).first()

    if not user:
        db.close()
        raise HTTPException(status_code=404, detail="User Not Found !")

    user.name = user_data.name
    user.email = user_data.email

    db.commit()
    db.refresh(user)
    db.close()

    return user


@app.delete("/users/{userid}")
def delete_user(userid : int):

    db = sesson_local()

    user = db.query(User).filter( User.id == userid).first()

    if not user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found !")

    db.delete(user)
    db.commit()
    db.close()

    return {f"User {user.name} is succssfully deleted !"}