import json
import os

from typing import Any, Dict, List
from werkzeug.wrappers import Request, Response


STORAGE_PATH = '/tmp/rfind-server.store'


def retrieve_all() -> List[str]:
    try:
        with open(STORAGE_PATH, 'r') as f:
            lines = [s.strip() for s in f.readlines()]

        return lines
    except Exception:
        return []


def store_command(command: str) -> str:
    lines: Line[str] = retrieve_all()
    if command in lines:
        return f'command "{command}" is already registered'

    with open(STORAGE_PATH, 'a+') as f:
        f.write(command + "\n")
        return f'command "{command}" is registered'


def flush() -> None:
    os.remove(STORAGE_PATH)


def get(num: int) -> None:
    lines = retrieve_all()
    return lines[num-1]


@Request.application
def application(request):
    req = request.get_json()
    res = ''

    if req['instruction'] == 'add':
        res = store_command(req['body'])
    
    if req['instruction'] == 'get_all':
        res = json.dumps(retrieve_all())

    if req['instruction'] == 'get':
        res = get(int(req['body']))

    if req['instruction'] == 'flush':
        flush()
        res = 'Commands flushed'

    return Response(res)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, application, use_reloader=True)
