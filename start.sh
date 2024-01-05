#/bin/bash
source .env

poetry run uvicorn server:app --reload --port 5001
