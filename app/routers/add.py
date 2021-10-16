from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from app.libraries.storage import store_command

router = APIRouter()


class AddBody(BaseModel):
    command: str
    message: str
    tags: List[str]


@router.post("/add")
async def add(add: AddBody):
    msg = store_command(add.command, add.message, add.tags)

    return {"result": msg}
