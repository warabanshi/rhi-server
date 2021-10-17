import pytest

from unittest.mock import patch

from httpx import AsyncClient

from app.main import app

@pytest.mark.asyncio
@patch('app.routers.flush.remove')
async def test_add(mock_remove):
    expected = {"result": "storage file was removed"}

    async with AsyncClient(app=app, base_url='http://localhost') as ac:
        r = await ac.post('/flush')

    assert r.status_code == 200
    assert r.json() == expected
