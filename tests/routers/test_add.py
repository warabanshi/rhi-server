import json
import pytest

from unittest.mock import patch

from httpx import AsyncClient

from app.main import app

@pytest.mark.asyncio
@patch('app.routers.add.store_command')
async def test_add(mock_store_command):
    mock_store_command.return_value = 'command test is registered'
    expected = {'result': 'command test is registered'}

    async with AsyncClient(app=app, base_url='http://localhost') as ac:
        data = {'command': 'test', 'message': 'test mesage', 'tags': ['test1', 'test2']}
        r = await ac.post('/add', json=data)

    assert r.status_code == 200
    assert r.json() == expected

@pytest.mark.asyncio
@patch('app.routers.add.store_command')
async def test_add_invalid_data(mock_store_command):
    async with AsyncClient(app=app, base_url='http://localhost') as ac:
        data = {'command': 'test'}
        r = await ac.post('/add', json=data)

    assert r.status_code == 422
