from typing import Protocol

from .models import ProductOut
from .repositorys import ProductRepository


class ProductRepositoryInterface(Protocol):
    def get(self) -> list[ProductOut]: ...


class ProductService:
    def __init__(self, repository: ProductRepositoryInterface = ProductRepository()):
        self.repository = repository

    def get(self) -> list[ProductOut]:
        return self.repository.get()
