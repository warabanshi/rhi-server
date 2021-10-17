from typing import Dict, List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import headers
from app.libraries.storage import store_command

router = APIRouter()


class AddBody(BaseModel):
    command: str
    message: str
    tags: List[str]


@router.post("/add")
async def add(add: AddBody, headers: Dict = Depends(headers)):
    msg = store_command(headers["x_rhi_username"], add.command, add.message, add.tags)

    return {"result": msg}
