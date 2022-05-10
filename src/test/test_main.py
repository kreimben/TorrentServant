from fastapi.testclient import TestClient
from fastapi import FastAPI, Response
from ..main import app

app: FastAPI = app

client = TestClient(app)
print('Test Code Is About Executing!')
print('client info: {}'.format(client))

def test_read_main():
    response: Response = client.get('/')

    assert response.status_code == 200
