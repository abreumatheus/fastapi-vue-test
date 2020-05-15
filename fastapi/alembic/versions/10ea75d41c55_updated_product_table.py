"""Updated Product table

Revision ID: 10ea75d41c55
Revises: c3ac9976d448
Create Date: 2020-05-15 13:50:19.519054

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '10ea75d41c55'
down_revision = 'c3ac9976d448'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('product', 'promotional_price')
    op.drop_column('product', 'photos')
    op.add_column('product', sa.Column('promotional_price', sa.Float(), nullable=True, default=None))
    op.add_column('product', sa.Column('photos', postgresql.ARRAY(sa.String()), nullable=True, default=['default']))


def downgrade():
    op.drop_column('product', 'promotional_price')
    op.drop_column('product', 'photos')
    op.add_column('product', sa.Column('promotional_price', sa.Float(), nullable=False))
    op.add_column('product', sa.Column('photos', postgresql.ARRAY(sa.String()), nullable=True, default=['default.jpǵ']))
