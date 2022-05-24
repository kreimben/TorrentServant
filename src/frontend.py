import datetime

import requests
from fastapi import FastAPI, APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(
    tags=['storage'],
)

templates = Jinja2Templates(directory="../templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):

    result = await requests.get('http://localhost:8000/api/storage/space?option=g')
    json = await result.json()
    print('storage space: {}'.format(json))

    context = {
        'request': request,
        'title': 'TorrentServant',
        'content': 'Hello! This is TorrentServant.',
        'result': json
    }
    return templates.TemplateResponse('index.html', context)
