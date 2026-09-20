import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#load contents of .env file
load_dotenv()

DB_URL = os.getenv("DataBase_URL")

if not DB_URL:
    raise ValueError("DATABASE_URL is not set in .env")

#DataBase connection creation
engine = create_engine(DB_URL)

sesson_local = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind= engine
)

#create templete of database tables
Base = declarative_base()



