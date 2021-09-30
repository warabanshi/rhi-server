from starlette.testclient import TestClient

from app.main import app
from .conftest import test_app

client = TestClient(app)


def test_get(test_app):
    res = test_app.get('/get/')

    assert res.status_code == 200
    assert res.json() == {'result': []}
