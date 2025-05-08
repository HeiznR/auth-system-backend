from fastapi import APIRouter
from src.db.database import engine
from src.utils.models import Base

router = APIRouter()


@router.post("/setup_database", tags=["database"], summary="createDB")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}
