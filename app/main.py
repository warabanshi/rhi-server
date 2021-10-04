from fastapi import FastAPI

from app.routers import add, get, flush, delete


app = FastAPI()

app.include_router(add.router)
app.include_router(get.router)
app.include_router(flush.router)
app.include_router(delete.router)
