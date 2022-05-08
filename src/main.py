import uvicorn as uvicorn
import ready
import frontend

app = ready.get_application()

app.mount('/', frontend.ready_for_frontend())
# TODO: mount backend logics.

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port='8000')
