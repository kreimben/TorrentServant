import fastapi.applications
from fastapi import FastAPI
import event

def get_application() -> fastapi.applications.FastAPI:
    app = FastAPI()
    event.ready_for_event(app)

    return app
