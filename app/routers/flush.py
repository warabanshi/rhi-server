from typing import Dict

from fastapi import APIRouter, Depends

from app.dependencies import headers
from app.libraries.storage import remove


router = APIRouter()


@router.post("/flush")
async def flush(headers: Dict = Depends(headers)):
    remove(headers["x_rhi_username"])
    return {"result": "storage file was removed"}
