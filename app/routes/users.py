from fastapi import APIRouter
from app.database import sesson_local
from app.model import User

router = APIRouter()

@router.get("/users")
def getData():

    db = sesson_local()

    user = db.query(User).all()


    # .all()     # list of results
    # .first()   # first result/row
    # .scalar()  # actual single value

    db.close()

    return user, {"Users" : [u.name for u in user]}
