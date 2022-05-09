from fastapi import FastAPI, APIRouter
from starlette.requests import Request
import shutil
import os

router = APIRouter(
    prefix='/api/storage',
    tags=['storage'],
)


@router.get('/space', description='k, m, g, t, p, e. Default is \'g\' for GigaBytes.')
async def space(request: Request, option: str = 'g'):
    cwd = os.getcwd()
    usage = shutil.disk_usage(cwd + '/../Downloads')

    total_size = _byte_transform(usage.total, option)
    used_size = _byte_transform(usage.used, option)
    free_size = _byte_transform(usage.free, option)

    return {'success': True, 'total': total_size, 'used': used_size, 'free': free_size}


def _byte_transform(bytes: int, to: str, bsize=1024) -> str:
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize

    results = str(round(r,2))

    if to == 'k':
        results += 'KB'

    elif to == 'm':
        results += 'MB'

    elif to == 'g':
        results += 'GB'

    elif to == 't':
        results += 'TB'

    elif to == 'p':
        results += 'PB'

    elif to == 'e':
        results += 'EB'

    return results