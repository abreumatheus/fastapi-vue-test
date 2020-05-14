from app.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column
from app.domains.products.models import Product


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    products = relationship('Product', primaryjoin='Category.id == Product.category_id',
                            backref='category')