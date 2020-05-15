"""Updated both tables (Product and Category)

Revision ID: 43edede32146
Revises: 27616deaf743
Create Date: 2020-05-14 20:16:21.152544

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '43edede32146'
down_revision = '27616deaf743'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('products')
    op.drop_table('categories')
    op.create_table('category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('product',
                    sa.Column('id', sa.String(length=255), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('photos', postgresql.ARRAY(sa.String()), nullable=True),
                    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_products_category_id'), 'product', ['category_id'], unique=False)


def downgrade():
    op.drop_table('products')
    op.drop_table('categories')
    op.create_table('categories',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('products',
                    sa.Column('id', sa.String(length=255), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('photos', postgresql.ARRAY(sa.String()), nullable=True),
                    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_products_category_id'), 'products', ['category_id'], unique=False)
