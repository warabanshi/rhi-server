import pytest
from httpx import AsyncClient
from typing import Any, Dict, List

from unittest.mock import patch
from unittest.mock import ANY

from unittest.mock import AsyncMock, MagicMock
from app.routers.delete import delete
from app.main import app


@pytest.mark.asyncio
@patch('app.routers.delete.update')
@patch('app.routers.delete.retrieve_all')
async def test_delete(mock_retrieve_all, mock_update):
    mock_retrieve_all.return_value = [
        {"command": "test command 1", "message": ""},
        {"command": "test command 2", "message": ""},
        {"command": "test command 3", "message": ""},
        {"command": "test command 4", "message": ""},
        {"command": "test command 5", "message": ""},
        {"command": "test command 6", "message": ""},
    ]
    mock_update.return_value = None

    expected_update_args = [
        {"command": "test command 1", "message": ""},
        {"command": "test command 4", "message": ""},
        {"command": "test command 6", "message": ""},
    ]

    expected_result = {"result": f"command 2,3,5 were deleted"}

    async with AsyncClient(app=app, base_url='http://localhost') as ac:
        r = await ac.delete('/delete/2,3,5/')

        mock_update.assert_called_once_with(ANY, expected_update_args)
        assert r.json() == expected_result
