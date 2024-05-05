from pydantic import BaseModel
from typing import Optional

class NewEmployee(BaseModel):
    name: str
    age: int
    designation: str


class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    designation: Optional[str] = None