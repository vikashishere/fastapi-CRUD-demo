# do <pip install "fastapi[all]"> to install all the required dependencies
from fastapi import FastAPI

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