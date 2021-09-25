from fastapi import APIRouter

from app.libraries.storage import remove


router = APIRouter()


@router.post("/flush")
async def flush():
    remove()
    return {"result": "storage file was removed"}
