import json
import os

from typing import Any, Dict, List
from werkzeug.wrappers import Request, Response


STORAGE_PATH = '/tmp/rfind-server.store'


def store_command(command: str) -> None:
    with open(STORAGE_PATH, 'a+') as f:
        f.write(command)
        f.write("\n")


def retrieve_all() -> List:
    try:
        with open(STORAGE_PATH, 'r') as f:
            lines = [s.strip() for s in f.readlines()]

        return lines
    except Exception:
        return []


def flush() -> None:
    os.remove(STORAGE_PATH)


def get(num: int) -> None:
    lines = retrieve_all()
    return lines[num-1]


@Request.application
def application(request):
    req = request.get_json()
    res = ''

    if req['instruction'] == 'register':
        store_command(req['body'])
        res = 'A command was registered'
    
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
