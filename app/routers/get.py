from typing import Dict

from fastapi import APIRouter, Depends

from app.dependencies import headers
from app.libraries.storage import retrieve_all


router = APIRouter(
    prefix="/get",
    tags=["get"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all(headers: Dict = Depends(headers)):
    r = retrieve_all(headers["x_rhi_username"])
    return {"result": r}


@router.get("/{row_num}")
async def get(row_num: int, headers: Dict = Depends(headers)):
    lines = retrieve_all(headers["x_rhi_username"])
    r = lines[row_num - 1]
    return {"result": r}
