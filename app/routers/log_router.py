from fastapi import APIRouter

router = APIRouter(
    prefix= "/logs",
    tags = ["Logs"]
)

@router.get("/")
def get_logs():
    pass

@router.post("/upload")
def upload_logs():
    pass