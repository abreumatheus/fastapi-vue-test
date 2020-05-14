from typing import List
from fastapi import APIRouter
from app.utils.schemas import Message
from app.domains.categories.actions import CategoryActions
from app.domains.categories.schemas import Category, CategoryUpdate

router = APIRouter()
_CRUD_CATEGORIES = CategoryActions()


@router.post('/', response_model=Category)
def new_category(name: str):
    category_in = {"name": name}
    category = _CRUD_CATEGORIES.add_new_category(category_in)
    return category


@router.get('/', response_model=List[Category])
def get_all_categories():
    categories = _CRUD_CATEGORIES.get_all_categories()
    return categories


@router.get('/{category_id}', response_model=Category)
def get_category_by_id(category_id: int):
    category = _CRUD_CATEGORIES.get_category_by_id(category_id)
    return category


@router.delete('/{category_id}', response_model=Message)
def delete_category(category_id: int):
    _CRUD_CATEGORIES.delete_category_by_id(category_id)
    return {"message": "Product deleted!"}


@router.put('/{category_id}', response_model=Category)
def update_category(category_id: int, category_in: CategoryUpdate):
    category_in = category_in.dict()
    category_in['id'] = category_id
    category = _CRUD_CATEGORIES.update_category(category_in)
    return category
