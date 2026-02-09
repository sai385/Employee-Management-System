from sqlalchemy import Column, Integer, String
from app.database.db import Base 

class Signup(Base):
    __tablename__ = "signup2"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100))
    password = Column(String(128))  
