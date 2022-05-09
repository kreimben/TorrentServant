import uvicorn as uvicorn
import ready
import frontend
from router import storage

app = ready.get_application()

app.add_route('/', frontend.router)
# TODO: mount backend logics.
# app.mount('/router/storage', storage.storage)
app.add_route('/api/storage', storage.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port='8000')
