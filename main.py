from fastapi import FastAPI
from app.database import engine, Base
from app.routes import employers, poc, jobs 

# Create database tables
Base.metadata.create_all(bind=engine)

#Initialize FastAPI app (this must exist)
app = FastAPI()

#  Include routers
app.include_router(employers.router)
app.include_router(poc.router)
app.include_router(jobs.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Job Portal API"}

