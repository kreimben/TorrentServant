import uvicorn as uvicorn
import ready
import frontend
from router import storage

app = ready.get_application()

app.include_router(frontend.router)
app.include_router(storage.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
