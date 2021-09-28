from fastapi import APIRouter
from pydantic import BaseModel

from app.libraries.storage import store_command

router = APIRouter()


class AddBody(BaseModel):
    command: str
    message: str


@router.post("/add")
async def add(add: AddBody):
    msg = store_command(add.command, add.message)

    return {"result": msg}
