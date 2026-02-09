from pydantic import BaseModel, EmailStr
from datetime import date
from decimal import Decimal
from typing import Optional


class EmployeeBase(BaseModel):
    FirstName: str
    LastName: str
    Email: Optional[EmailStr] = None
    HireDate: Optional[date] = None
    JobTitle: Optional[str] = None
    Salary: Optional[Decimal] = None



class EmployeeCreate(EmployeeBase):
    FirstName: str
    LastName: str
    Email: Optional[EmailStr] = None
    HireDate: Optional[date] = None
    JobTitle: Optional[str] = None
    Salary: Optional[Decimal] = None
   



class EmployeeUpdate(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[EmailStr] = None
    HireDate: Optional[date] = None
    JobTitle: Optional[str] = None
    Salary: Optional[Decimal] = None



class EmployeeResponse(EmployeeBase):
    EmployeeID: int

    class Config:
        orm_mode = True
