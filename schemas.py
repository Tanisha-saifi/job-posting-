from pydantic import BaseModel, EmailStr
from typing import List, Optional

class EmployerBase(BaseModel):
    name: str
    email: EmailStr

class EmployerCreate(EmployerBase):
    password: str

class EmployerResponse(EmployerBase):
    id: int

    class Config:
        from_attributes = True

class PoCBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class PoCCreate(PoCBase):
    pass

class PoCResponse(PoCBase):
    id: int
    employers: List[EmployerResponse] = []

    class Config:
        from_attributes = True

class JobBase(BaseModel):
    title: str
    description: str

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int
    employer_id: int

    class Config:
        from_attributes = True
