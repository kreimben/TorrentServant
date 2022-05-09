from fastapi import FastAPI, APIRouter
from starlette.requests import Request
import shutil
import os

router = APIRouter(
    prefix='/storage',
    tags=['storage'],
)


@router.get('/space')
async def space(request: Request):
    downloads_dir = os.getcwd()
    print('downloads_dir: {}'.format(downloads_dir))
    usage = shutil.disk_usage('../../Downloads')

    return {'success': True, 'total': usage.total, 'used': usage.used, 'free': usage.free}
