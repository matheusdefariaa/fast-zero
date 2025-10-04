from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/ola', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def resposta_ola():
    return """
    <html>
    <head><title>FastAPI</title></head>
    <body><h1>Olá Mundo</h1></body>
    </html>
    """
