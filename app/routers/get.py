from fastapi import APIRouter

from app.libraries.storage import retrieve_all


router = APIRouter(
    prefix='/get',
    tags=['get'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/')
async def get_all():
    return {'result': retrieve_all()}


@router.get('/{row_num}')
async def get(row_num: int):
    lines = retrieve_all()
    return {'result': f'{lines[row_num-1]}'}
