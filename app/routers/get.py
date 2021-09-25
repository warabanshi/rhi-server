from fastapi import APIRouter

router = APIRouter(
    prefix='/get',
    tags=['get'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/')
async def get_all():
    return {'result': 'get_all() called'}

@router.get('/{row_num}')
async def get_all(row_num: int):
    return {'result': f'get() called. row_num={row_num}'}
