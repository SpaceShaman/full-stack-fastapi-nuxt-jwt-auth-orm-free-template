from typing import Protocol

from .models import ProductOut
from .repositorys import ProductRepository


class ProductRepositoryInterface(Protocol):
    def get(self) -> list[ProductOut]: ...


class ProductService:
    def __init__(self) -> None:
        self.repository: ProductRepositoryInterface = ProductRepository()

    def get(self) -> list[ProductOut]:
        return self.repository.get()
