from pydantic import BaseModel, EmailStr


class LoginCreate(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    id: int
    email: EmailStr
    access_token: str
    token_type: str
