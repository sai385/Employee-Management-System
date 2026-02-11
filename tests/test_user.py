import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException, status
from datetime import date

from app.services.employserv import create_employee 

from app.models.empmodels import Employee
from app.schema.empschema import EmployeeCreate

def test_create_employee_success():
   
    db = MagicMock()

   
    db.query().filter().first.return_value = None

   
    emp = EmployeeCreate(
        FirstName="Sai",
        LastName="Vinay",
        Email="sai@example.com",
        HireDate=date(2024, 1, 1),
        JobTitle="Developer",
        Salary=50000
    )

   
    result = create_employee(db, emp)

  
    assert result.Email == "sai@example.com"
    assert result.FirstName == "Sai"

  
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()



def test_create_employee_email_exists():
    db = MagicMock()

   
    db.query().filter().first.return_value = Employee(
        Email="sai@example.com"
    )

    emp = EmployeeCreate(
        FirstName="Sai",
        LastName="Vinay",
        Email="sai@example.com",
        HireDate=date(2024, 1, 1),
        JobTitle="Developer",
        Salary=50000
    )

 
    with pytest.raises(HTTPException) as exc:
        create_employee(db, emp)

    assert exc.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc.value.detail == "Email already exists"


