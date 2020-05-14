from pydantic import BaseModel


class CategoryBase(BaseModel):
	name: str


class CategoryInDB(CategoryBase):
	id: int
	name: str

	class Config:
		orm_mode = True


class CategoryUpdate(CategoryBase):
	name: str = None


class Category(CategoryInDB):
	pass
