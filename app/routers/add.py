from fastapi import APIRouter
from pydantic import BaseModel

from app.libraries.storage import store_command

router = APIRouter()


class AddBody(BaseModel):
    command: str


@router.post('/add')
async def add(add: AddBody):
    msg = store_command(add.command)

    return {'result': msg}
