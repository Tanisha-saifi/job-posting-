from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..database import SessionLocal
from ..dependencies import get_db 

router = APIRouter(prefix="/employers", tags=["Employers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.EmployerResponse)
def register_employer(employer: schemas.EmployerCreate, db: Session = Depends(get_db)):
    hashed_password = auth.get_password_hash(employer.password)
    new_employer = models.Employer(name=employer.name, email=employer.email, password=hashed_password)
    db.add(new_employer)
    db.commit()
    db.refresh(new_employer)
    return new_employer
