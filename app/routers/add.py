from fastapi import APIRouter

router = APIRouter()


@router.post('/add')
async def add_command():
    return {'result': 'add_command called'}
