#/bin/bash
source .env

pipenv run uvicorn server:app --reload --port 5001
