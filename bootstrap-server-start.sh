#/bin/bash
source .env

pipenv run uvicorn bootstrap-server:app --reload --port 5001
