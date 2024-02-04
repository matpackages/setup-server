"""Setup Server get.matlabpackages.com for bootstraping matlabpackages."""
import os

from fastapi import FastAPI, Response
import requests


REPO_API = 'https://api.github.com/repos/matlabpackages/matlabpackages'
token = os.environ.get('GITHUB_TOKEN')
app = FastAPI()


# Routes
@app.get("/")
def root():
    """Root route."""
    url = f'{REPO_API}/contents/get_matlabpackages.m'
    return _github_request(url, accept='application/vnd.github.raw', media_type='text/plain')


@app.get("/latest.zip")
def download_latest():
    """Download latest version of matlabpackages as zip file."""
    url = f'{REPO_API}/zipball/master'
    return _github_request(url, accept='application/vnd.github+json', media_type='application/zip')


@app.get("/products")
def get_products():
    """Return known Mathworks products."""
    url = f'{REPO_API}/contents/products.csv'
    data = _github_request(url, accept='application/vnd.github.raw', media_type='text/plain')
    if data.status_code != 200:
        return data
    return _convert_json(data.body.decode())


def _github_request(url, accept='', media_type=''):
    try:
        res = requests.get(url, headers=_headers(accept=accept), stream=True, timeout=5.0)
        if res.status_code == 200:
            return Response(content=res.raw.data, media_type=media_type)
        else:
            return Response(status_code=404)
    except Exception:
        return Response(status_code=404)


def _headers(accept):
    return {
        'Accept': accept,
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28',
    }


def _convert_json(string: str):
    products = []
    rows = string.split('\n')
    data_rows = [r for r in rows[1:] if r != ""]
    for row in data_rows:
        name, identifier, description = row.split(',')
        products.append({"name": name, "identifier": identifier, "description": description})
    return products
