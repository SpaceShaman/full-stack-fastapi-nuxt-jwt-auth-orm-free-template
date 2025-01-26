from database import db_connect

from app.products.models import ProductOut


class ProductRepository:
    def get(self) -> list[ProductOut]:
        with db_connect() as connection:
            cursor = connection.execute("SELECT name, price, stock FROM products")
            products = cursor.fetchall()
            return [
                ProductOut(name=name, price=price, stock=stock)
                for name, price, stock in products
            ]
