import os
import requests
from fastapi import FastAPI, Response

repo_api = 'https://api.github.com/repos/matlabpackages/matlabpackages'
token = os.environ.get('GITHUB_TOKEN')
app = FastAPI()


# Routes
@app.get("/")
def root():
    url = f'{repo_api}/contents/get_matlabpackages.m'
    return github_request(url, accept='application/vnd.github.raw', type='text/plain')


@app.get("/latest.zip")
def download_latest():
    url = f'{repo_api}/zipball/master'
    return github_request(url, accept='application/vnd.github+json', type='application/zip')


def github_request(url, accept='', type=''):
    try:
        res = requests.get(url, headers=headers(accept=accept), stream=True)
        if res.status_code == 200:
            return Response(content=res.raw.data, media_type=type)
        else:
            return Response(status_code=404)
    except:
        return Response(status_code=404)


def headers(accept):
    return {
        'Accept': accept,
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28',
    }
