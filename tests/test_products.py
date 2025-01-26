from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_empty_products_list():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []


def test_get_products_list(connection):
    connection.execute(
        "INSERT INTO products (name, price, stock) VALUES ('Product 1', 10.0, 15)"
    )
    connection.execute(
        "INSERT INTO products (name, price, stock) VALUES ('Product 2', 20.0, 25)"
    )
    connection.commit()

    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Product 1", "price": 10.0, "stock": 15},
        {"name": "Product 2", "price": 20.0, "stock": 25},
    ]
