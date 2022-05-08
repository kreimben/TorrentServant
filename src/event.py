from fastapi import FastAPI
import environments

def ready_for_event(app: FastAPI) -> FastAPI:
    @app.on_event('startup')
    async def event_start():
        # TODO: Insert logger.
        print("Application started!")
        print("{} ({})".format(environments.APP_NAME, environments.APP_VERSION))

    @app.on_event('shutdown')
    async def event_shutdown():
        # TODO: Insert logger.
        print("Application is going shutdown!")

