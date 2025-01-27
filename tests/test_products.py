def _create_product(connection, name: str, price: int, stock: int):
    connection.execute(
        f"INSERT INTO products (name, price, stock) VALUES ('{name}', {price}, {stock})"
    )
    connection.commit()


def test_get_empty_products_list(client, connection):
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []


def test_get_products_list(client, connection):
    _create_product(connection, "Product 1", 10, 15)
    _create_product(connection, "Product 2", 20, 25)

    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Product 1", "price": 10.0, "stock": 15},
        {"id": 2, "name": "Product 2", "price": 20.0, "stock": 25},
    ]
