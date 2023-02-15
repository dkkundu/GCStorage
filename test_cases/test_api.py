import requests
import pathlib

working_dir = pathlib.Path.cwd()
sample = working_dir.joinpath('sample')


url = "http://127.0.0.1:5000/config"


def test_upload_file():
    with open(f"{sample}/right/configuration-file.json", 'rb') as file:
        response = requests.post(url, files={'file': file})
    assert response.status_code == 200, f"status code Should be 200, but got {response.status_code}" # noqa

    with open(f"{sample}/wrong/configuration-filess.json", 'rb') as file:
        response = requests.post(url, files={'file': file})
    assert response.status_code == 400, f"status code Should be 200, but got {response.status_code}" # noqa


def test_download_file():
    response = requests.get(url)
    assert response.status_code == 200, f"status code Should be 200, but got {response.status_code}" # noqa
