import datetime

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
    context = {
        'request': request,
        'title': 'TorrentServant',
        'content': 'Hello! This is TorrentServant.',
        'currentTime': datetime.datetime.now()
    }
    return templates.TemplateResponse('index.html', context)
