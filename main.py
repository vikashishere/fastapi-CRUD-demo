# do <pip install "fastapi[all]"> to install all the required dependencies
from fastapi import FastAPI
from utils import NewEmployee

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
    NewEmployee[new_id] = emp
    return employees[new_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)