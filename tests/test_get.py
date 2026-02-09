import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException, status
from datetime import date

from app.services.employserv import get_employee_by_id

from app.models.empmodels import Employee




def test_get_employee_by_id_success():

    db = MagicMock()

    mock_emp = Employee(
        EmployeeID=3,
        FirstName="Sai",
        LastName="pawan",
        Email="sai@example.com"
    )

   
    db.query().filter().first.return_value = mock_emp

   
    result = get_employee_by_id(db, 3)

  
    assert result.EmployeeID == 3
    

   
 
