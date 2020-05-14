from app.db import Base
from sqlalchemy.dialects import postgresql
from sqlalchemy import String, Float, ForeignKey, Column, Text


class Product(Base):
    __tablename__ = 'product'

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
