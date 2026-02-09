from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.config import get_current_user

from app.database.db import get_db
from app.schema.empschema import EmployeeCreate, EmployeeUpdate, EmployeeResponse

  

from app.services.employserv import create_employee,get_employee_by_id,get_all_employees,update_employee,delete_employee
    



router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def add_employee(
    emp: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)

   
):
    return create_employee(db, emp)



@router.get(
    "/{emp_id}",
    response_model=EmployeeResponse
)
def read_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return get_employee_by_id(db, emp_id)



@router.get(
    "/",
    response_model=List[EmployeeResponse]
)
def read_employees(
    db: Session = Depends(get_db)
):
    return get_all_employees(db)



@router.put(
    "/{emp_id}",
    response_model=EmployeeResponse
)
def update_emp(
    emp_id: int,
    emp_data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    return update_employee(db, emp_id, emp_data)



@router.delete(
    "/{emp_id}",
    status_code=status.HTTP_200_OK
)
def delete_emp(
    emp_id: int,
    db: Session = Depends(get_db)
):
    return delete_employee(db, emp_id)
