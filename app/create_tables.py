from app.database import engine, Base
from app.model import User

Base.metadata.create_all(bind = engine)

print("Successful")