from typing import Protocol

from .models import Product
from .repositorys import ProductRepository


class ProductRepositoryInterface(Protocol):
    def get(self) -> list[Product]: ...


class ProductService:
    def __init__(self, repository: ProductRepositoryInterface = ProductRepository()):
        self.repository = repository

    def get(self) -> list[Product]:
        return self.repository.get()
