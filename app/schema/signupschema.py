from pydantic import BaseModel, EmailStr

class SignupCreate(BaseModel):
    email: EmailStr
    password: str 


class SignupResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True  
