from sqlalchemy import String, Integer, Float, ForeignKey, Column, Text
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from app.db import Base


class Products(Base):
    __tablename__ = 'products'

    id = Column(String(255), primary_key=True)
    category_id = Column(ForeignKey('categories.id', ondelete='CASCADE'), index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    photos = Column(postgresql.ARRAY(String), nullable=True, default=['default.jpg'])


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    products = relationship('Products', primaryjoin='Categories.id == Products.category_id',
                            backref='categories')
