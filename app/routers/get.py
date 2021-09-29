import json

from fastapi import APIRouter

from app.libraries.storage import retrieve_all

USER = "warabanshi"  # temporary dummy user


router = APIRouter(
    prefix="/get",
    tags=["get"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_all():
    r = retrieve_all(USER)  # fixed user name is given temporary
    return {"result": r}


@router.get("/{row_num}")
async def get(row_num: int):
    lines = retrieve_all(USER)  # fixed user name is given temporary
    r = lines[row_num - 1]
    return {"result": r}
