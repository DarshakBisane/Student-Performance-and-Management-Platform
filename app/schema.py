from pydantic import BaseModel, EmailStr


#pydantic model for creating new User
class userCreate(BaseModel):

    name : str
    email : EmailStr

#pydantic model for updating existing user
class userUpdate(BaseModel):
    name : str
    email : EmailStr

