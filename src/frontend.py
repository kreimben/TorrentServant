from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


def ready_for_frontend() -> FastAPI:
    app = FastAPI()

    templates = Jinja2Templates(directory="../templates")

    @app.get("/", response_class=HTMLResponse)
    async def root(request: Request):
        context = {
            'request': request,
            'title': 'TorrentServant',
            'content': 'Hello! This is TorrentServant.'
        }
        return templates.TemplateResponse('index.html', context)

    return app
