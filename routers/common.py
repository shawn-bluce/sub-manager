from fastapi import APIRouter

router = APIRouter(
    prefix="/common",
    tags=["common"]
)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
