import pytest

from unittest.mock import patch

from httpx import AsyncClient

from app.main import app

@pytest.mark.asyncio
@patch('app.routers.get.retrieve_all')
async def test_get(mock_retrieve_all):
    mock_retrieve_all.return_value = [
        {"command": "test command 1", "message": ""},
        {"command": "test command 2", "message": ""},
    ]

    expected = {'result': [
        {"command": "test command 1", "message": ""},
        {"command": "test command 2", "message": ""},
    ]}

    async with AsyncClient(app=app, base_url='http://localhost') as ac:
        r = await ac.get('/get/')

    assert r.status_code == 200
    assert r.json() == expected
