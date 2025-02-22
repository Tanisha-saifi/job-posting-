from fastapi import APIRouter

router = APIRouter()

@router.get("/pocs")
def get_pocs():
    return {"message": "List of PoCs"}

@router.post("/pocs")
def create_poc():
    return {"message": "PoC created"}
