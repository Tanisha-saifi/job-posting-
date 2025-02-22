from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Association table for PoCs and Employers (Many-to-Many)
poc_employer_association = Table(
    "poc_employer",
    Base.metadata,
    Column("poc_id", Integer, ForeignKey("pocs.id")),
    Column("employer_id", Integer, ForeignKey("employers.id"))
)

class Employer(Base):
    __tablename__ = "employers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    pocs = relationship("PoC", secondary=poc_employer_association, back_populates="employers")
    jobs = relationship("Job", back_populates="employer")

class PoC(Base):
    __tablename__ = "pocs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)

    employers = relationship("Employer", secondary=poc_employer_association, back_populates="pocs")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    employer_id = Column(Integer, ForeignKey("employers.id"))

    employer = relationship("Employer", back_populates="jobs")
