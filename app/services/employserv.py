from sqlalchemy.orm import Session
from app.models.empmodels import Employee
from app.schema.empschema import EmployeeCreate,EmployeeUpdate
    

from fastapi import HTTPException, status



def create_employee(db: Session, emp: EmployeeCreate):
    existing_emp = db.query(Employee).filter(
        Employee.Email == emp.Email
    ).first()

    if existing_emp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_emp = Employee(
        FirstName=emp.FirstName,
        LastName=emp.LastName,
        Email=emp.Email,
        HireDate=emp.HireDate,
        JobTitle=emp.JobTitle,
        Salary=emp.Salary
    )

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp



def get_employee_by_id(db: Session, emp_id: int):
    emp = db.query(Employee).filter(
        Employee.EmployeeID == emp_id
    ).first()

    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return emp



def get_all_employees(db: Session):
    return db.query(Employee).all()



def update_employee(
    db: Session,
    emp_id: int,
    emp_data: EmployeeUpdate
):
    emp = db.query(Employee).filter(
        Employee.EmployeeID == emp_id
    ).first()

    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    for key, value in emp_data.dict(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp



def delete_employee(db: Session, emp_id: int):
    emp = db.query(Employee).filter(
        Employee.EmployeeID == emp_id
    ).first()

    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted successfully"}
