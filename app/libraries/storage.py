import os

from typing import List

from app.config import STORAGE_PATH


def retrieve_all() -> List[str]:
    try:
        with open(STORAGE_PATH, 'r') as f:
            lines = [s.strip() for s in f.readlines()]

        return lines
    except Exception:
        return []


def store_command(command: str) -> str:
    lines: List[str] = retrieve_all()
    if command in lines:
        return f'command "{command}" is already registered'

    with open(STORAGE_PATH, 'a+') as f:
        f.write(command + "\n")
        return f'command "{command}" is registered'


def remove():
    os.remove(STORAGE_PATH)
