# do <pip install "fastapi[all]"> to install all the required dependencies
from fastapi import FastAPI
from utils import NewEmployee, UpdateEmployee

app = FastAPI(
    title="CRUD Operations",
    description="CRUS operations demonstration using fastapi"
)

employees = {
    1:{
        "name": "John",
        "age": 32,
        "designation": "SDE"
    }
}

@app.get("/")
def home():
    return "Welcome to the FastAPI demonstration :-)"

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):
    if emp_id not in employees:
        return f"No employee exist with ID: {emp_id}"
    return employees[emp_id]

@app.post("/add-employee")
def add_employee(emp: NewEmployee):
    if not employees:
        new_id = 1
    else:
        new_id = max(employees.keys()) + 1
    employees[new_id] = emp.model_dump() # To convert the dtype from datamodel to dict
    return employees[new_id]

@app.put("/update-employee/{emp_id}")
def update_employee(emp_id: int, emp: UpdateEmployee):
    if emp_id not in employees:
        return f"No employee exist with ID: {emp_id}"
    if emp.name is not None:
        employees[emp_id]["name"] = emp.name
    
    if emp.age is not None:
        employees[emp_id]["age"] = emp.age

    if emp.designation is not None:
        employees[emp_id]["designation"] = emp.designation

    return employees[emp_id]


@app.delete("/delete-employee/{emp_id}")
def delete_employee(emp_id: int):
    if emp_id not in employees:
        return f"No employee exist with ID: {emp_id}"
    del employees[emp_id]
    return employees


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)