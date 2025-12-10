from fastapi import APIRouter

router = APIRouter(
    prefix="/alerts",
    tags= ["Alerts"]
)

@router.post("/rules")
def get_rules():
    pass

@router.get("/history")
def get_history():
    pass