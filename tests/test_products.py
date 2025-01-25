from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_empty_products_list():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []
