#!/bin/bash

uvicorn --host=0.0.0.0 --port=80 rfind_server.wsgi:app --reload
