from typing import List
from app.utils.schemas import Message
from fastapi import APIRouter, UploadFile, File, Form
from app.domains.products.actions import ProductsActions
from app.domains.products.schemas import Product, ProductUpdate

router = APIRouter()
_CRUD_PRODUCTS = ProductsActions()


@router.post('/', response_model=Product)
def new_product(name: str = Form(...),
                description: str = Form(...),
                price: str = Form(...),
                category_id: str = Form(...),
                photos: List[UploadFile] = File(...)):

    product_in = {"name": name,
                  "description": description,
                  "price": price,
                  "category_id": category_id,
                  "photos": photos}
    product = _CRUD_PRODUCTS.add_new_product(product_in)
    return product


@router.get('/', response_model=List[Product])
def get_all_products():
    products = _CRUD_PRODUCTS.get_all_products()
    return products


@router.get('/{poduct_id}', response_model=Product)
def get_product_by_id(poduct_id: str):
    product = _CRUD_PRODUCTS.get_product_by_id(poduct_id)
    return product


@router.delete('/{poduct_id}', response_model=Message)
def delete_product(poduct_id: str):
    _CRUD_PRODUCTS.delete_by_id(poduct_id)
    return {"message": "Product deleted!"}


@router.put('/{poduct_id}', response_model=Product)
def update_product(poduct_id: str, product_in: ProductUpdate):
    product_in = product_in.dict()
    product_in['id'] = poduct_id
    product = _CRUD_PRODUCTS.update_product(product_in)
    return product
