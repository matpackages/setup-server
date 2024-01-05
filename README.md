# setup-server

Setup server for bootstrapping matlabpackages (get.matlabpackages.com)

## Prerequisites

Clone this repository:

    git clone https://github.com/matlabpackages/setup-server.git
    cd setup-server

Create a file `.env` and add the following content:

    export GITHUB_TOKEN=<YOUR_GITHUB_ACCESS_TOKEN>

## Start server

Run the following:

    source .env

Start server in development mode (requires `poetry install` to be run first):

    poetry run uvicorn server:app --reload --port 5001

Start server in production mode (using Docker container):

    docker build . -t setup-server
    docker run -e GITHUB_TOKEN -p 8080:80 setup-server

test