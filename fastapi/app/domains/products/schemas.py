from pydantic import BaseModel
from typing import List


class ProductBase(BaseModel):
	name: str
	description: str
	price: float
	promotional_price: float = None


class ProductInDB(ProductBase):
	id: str
	category_id: int
	photos: List[str]

	class Config:
		orm_mode = True


class Product(ProductInDB):
	pass
