from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter(prefix="/api")


@router.get("/health", response_model=HealthResponse, tags=["system"])
async def health():
    return {"status": "ok", "version": "0.1.0"}
