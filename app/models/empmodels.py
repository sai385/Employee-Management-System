from sqlalchemy import Column, Integer, String, Date, Numeric

from app.database.db import Base

class Employee(Base):
    __tablename__ = "employees"

    EmployeeID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Email = Column(String(100), unique=True)
    HireDate = Column(Date)
    JobTitle = Column(String(50))
    Salary = Column(Numeric(10, 2))
