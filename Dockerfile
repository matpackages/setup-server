FROM python:3.11
WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN poetry install
COPY server.py .
CMD ["poetry", "run", "uvicorn", "server:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
