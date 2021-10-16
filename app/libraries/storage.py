import json
import os

from typing import Any, Dict, List

from app.config import STORAGE_DIR, STORAGE_FILE_SUFFIX


USER = "warabanshi"  # temporary dummy user

"""
<< stored data format >>

/STORAGE_DIR/(username).store

[
    {"command": "xxxxxxx", "message": "this is sample message 1", tags:['aaa', 'bbb']},
    {"command": "yyyyyyy", "message": "this is sample message 2", tags:[]},
    ...
]
"""


def make_storage_path(username: str) -> str:
    return "/".join([STORAGE_DIR, username]) + STORAGE_FILE_SUFFIX


def retrieve_all(username: str) -> List[Dict[str, Any]]:
    try:
        with open(make_storage_path(username), "r") as f:
            return json.load(f)

        return []
    except Exception:
        return []


def store_command(
    username: str, command: str, message: str = "", tags: List[str] = []
) -> str:
    userdata: List[Dict[str, Any]] = retrieve_all(username)

    if command in [row["command"] for row in userdata]:
        return f'command "{command}" is already registered'

    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

    with open(make_storage_path(username), "w") as f:
        userdata.append(
            {
                "command": command,
                "message": message,
                "tags": tags,
            }
        )

        json.dump(userdata, f)

    return f'command "{command}" is registered'


def remove(username: str) -> None:
    if os.path.exists(make_storage_path(username)):
        os.remove(make_storage_path(username))


def update(username: str, update_target: List[Dict[str, Any]]) -> None:
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

    with open(make_storage_path(username), "w") as f:
        json.dump(update_target, f)
