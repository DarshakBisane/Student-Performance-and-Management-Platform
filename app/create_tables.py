from app.database import engine, Base
from app.model import Student

Base.metadata.create_all(bind = engine)

print("Successful")