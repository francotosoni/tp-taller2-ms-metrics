from main import app
from fastapi.testclient import TestClient

import pytest


@pytest.fixture()
def client():
    return TestClient(app)


def test_home(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}
