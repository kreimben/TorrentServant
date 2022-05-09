import fastapi.applications
from fastapi import FastAPI
import event
import environments


def get_application() -> fastapi.applications.FastAPI:
    app = FastAPI(name=environments.APP_NAME, version=environments.APP_VERSION, debug=True)
    event.ready_for_event(app)

    return app
