import json

from typing import Any, Dict, List
from werkzeug.wrappers import Request, Response


STORAGE_PATH = '/tmp/rfind-server.store'


def store_command(command: str) -> None:
    pass


def retrieve_all() -> List:
    return ['test', 'test2', 'test3']


@Request.application
def application(request):
    req = request.get_json()
    res = ''

    if req['instruction'] == 'register':
        store_command(req['body'])
    
    if req['instruction'] == 'get_all':
        res = json.dumps(retrieve_all())

    return Response(res)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8000, application, use_reloader=True)
