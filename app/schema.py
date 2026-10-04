from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Annotated


class CreateStudent(BaseModel):

    model_config = ConfigDict(
        str_strip_whitespace= True
    )

    enrollment_no : Annotated[
        str, Field(
            min_length= 8,
            max_length=10,
            pattern= r"^[A-Za-z0-9]+$"
        )
    ]

    name : Annotated[
        str, Field(
            max_length = 100,
            pattern = r"^[A-Za-z\s]+$"
        )
    ]

    email : EmailStr

    phone : Annotated[
        str | None, Field(
            min_length=10,
            max_length=12,
            default = None,
            pattern = r"^\+?[0-9]{10,14}$"
        )
    ]

    department : Annotated[
        str, Field(
            max_length=20,
            min_length=2
        )
    ]

    semester : Annotated[
        int, Field(
            ge=1,
            le=8
        )
    ]

class UpdateStudent(BaseModel):

    model_config = ConfigDict(
        str_strip_whitespace= True
    )

    enrollment_no : Annotated[
        str | None, Field(
            min_length= 8,
            max_length=10,
            pattern= r"^[A-Za-z0-9]+$",
            default= None
        )
    ]

    name : Annotated[
        str | None, Field(
            max_length = 100,
            pattern = r"^[A-Za-z\s]+$",
            default= None
        )
    ]

    email : EmailStr | None = None

    phone : Annotated[
        str | None, Field(
            min_length=10,
            max_length=12,
            default = None,
            pattern = r"^\+?[0-9]{10,14}$"
        )
    ]

    department : Annotated[
        str | None, Field(
            max_length=20,
            min_length=2,
            default= None
        )
    ]

    semester : Annotated[
        int | None, Field(
            ge=1,
            le=8,
            default= None
        )
    ]
