from fastapi import APIRouter

from app.api.endpoints import products
from app.api.endpoints import categories

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(categories.router, prefix="/categories", tags=["Categories"])
