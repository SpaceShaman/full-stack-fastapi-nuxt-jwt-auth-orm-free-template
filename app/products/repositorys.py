from database import db_connect

from app.products.models import Product


class ProductRepository:
    def get(self) -> list[Product]:
        with db_connect() as connection:
            cursor = connection.execute("SELECT * FROM products")
            columns = [column[0] for column in cursor.description]
            return [
                Product(**dict(zip(columns, product))) for product in cursor.fetchall()
            ]
