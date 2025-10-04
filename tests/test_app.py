from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app


def test_read_root_dev_retorna_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_ola():
    client = TestClient(app)

    response = client.get('/ola')

    text = """
    <html>
    <head><title>FastAPI</title></head>
    <body><h1>Olá Mundo</h1></body>
    </html>
    """
    assert response.text == text
