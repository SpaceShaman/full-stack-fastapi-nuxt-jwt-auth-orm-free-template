from fastapi import APIRouter

from products.models import ProductOut

from .services import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
async def get_products() -> list[ProductOut]:
    return ProductService().get()
