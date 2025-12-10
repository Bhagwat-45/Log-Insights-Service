from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/summary")
def get_summary():
    pass

@router.get("/traffic")
def get_traffic():
    pass
