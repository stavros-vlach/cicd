from cicd.function_app import http_hello
import azure.functions as func
import pytest

def test_http_hello():
    req = func.HttpRequest(
        method='GET',
        url='/api/http_hello',
        params={'name': 'Pytest'},
        body=None
    )

    resp = http_hello(req)

    assert resp.status_code == 200
    assert "Hello, Pytest" in resp.get_body().decode()