from pydantic import BaseModel


class ProductOut(BaseModel):
    name: str
    price: float
    stock: int
