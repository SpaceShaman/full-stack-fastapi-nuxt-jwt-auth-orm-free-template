from fastapi import APIRouter

from products.models import Product

from .services import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
async def get_products() -> list[Product]:
    return ProductService().get()
