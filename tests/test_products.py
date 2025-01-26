from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def _create_product(connection, name: str, price: int, stock: int):
    connection.execute(
        f"INSERT INTO products (name, price, stock) VALUES ('{name}', {price}, {stock})"
    )
    connection.commit()


def test_get_empty_products_list():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []


def test_get_products_list(connection):
    _create_product(connection, "Product 1", 10, 15)
    _create_product(connection, "Product 2", 20, 25)

    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == [
        {"name": "Product 1", "price": 10.0, "stock": 15},
        {"name": "Product 2", "price": 20.0, "stock": 25},
    ]
