import requests


def test_get_auth_error_405():
    response = requests.get('http://127.0.0.1:8000/api/token/')
    assert response.status_code == 405


def test_get_response_content_type():
    response = requests.get('http://127.0.0.1:8000/api/token/')
    assert response.headers['Content-Type'] == 'application/json'
