from database import db_connect

from app.products.models import Product


class ProductRepository:
    def get(self) -> list[Product]:
        with db_connect() as connection:
            cursor = connection.execute("SELECT name, price, stock FROM products")
            products = cursor.fetchall()
            return [
                Product(name=name, price=price, stock=stock)
                for name, price, stock in products
            ]
