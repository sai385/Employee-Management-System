from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.signupmodel import Signup
from app.schema.signupschema import SignupCreate, SignupResponse
from passlib.context import CryptContext
from app.core.security import hash_password,verify_password
from app.core.config import create_access_token



SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  


def signup(user: SignupCreate, db: Session = Depends(get_db)):
    existing_user = db.query(Signup).filter(Signup.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    new_user = Signup(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def authenticate_user(db: Session, email: str, password: str):
    user = db.query(Signup).filter(Signup.email == email).first()
    print("authenticate")
    print("vgvgvgvgvgvgce")
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
