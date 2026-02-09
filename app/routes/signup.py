from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.signupmodel import Signup
from app.schema.signupschema import SignupCreate, SignupResponse
from app.schema.loginschema import LoginResponse,LoginCreate

from passlib.context import CryptContext
from app.core.security import hash_password
from app.services.logger import signup,authenticate_user
from app.core.config import create_access_token



router = APIRouter(prefix="/auth", tags=["Auth"])
@router.post("/signup", response_model=SignupResponse)
def sin(
    sin1:SignupCreate,
    db: Session = Depends(get_db),
):
     return signup(sin1,db)






@router.post("/login", response_model=LoginResponse)
def login(user: LoginCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    
    access_token = create_access_token(data={"user_id": db_user.id, "email": db_user.email})
    
    
    return {
        "id": db_user.id,
        "email": db_user.email,
        "access_token": access_token,
        "token_type": "bearer"
    }
