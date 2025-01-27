from database.connection import db_connect

from products.models import ProductOut


class ProductRepository:
    def get(self) -> list[ProductOut]:
        with db_connect() as connection:
            cursor = connection.execute("SELECT id, name, price, stock FROM products")
            products = cursor.fetchall()
            return [
                ProductOut(id=id, name=name, price=price, stock=stock)
                for id, name, price, stock in products
            ]
