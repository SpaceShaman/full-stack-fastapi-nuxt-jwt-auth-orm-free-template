from fastapi import APIRouter

from products.models import ProductOut

from .services import ProductService

products_router = APIRouter(prefix="/products", tags=["products"])


@products_router.get("/")
async def get_products() -> list[ProductOut]:
    return ProductService().get()
