import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('http://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/olgatatarchenkova')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Olga'
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'


@pytest.mark.http
def test_status_code_404_test():
    r = requests.get('https://api.github.com/users/0lgatatarchenkova')

    assert r.status_code == 404
