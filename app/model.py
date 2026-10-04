from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id : Mapped[int] = mapped_column(
        index= True,
        primary_key= True
    )

    enrollment_nO : Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    name : Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    phone : Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    email : Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )

    department : Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    semester : Mapped[int] = mapped_column(
        nullable=False
    )

