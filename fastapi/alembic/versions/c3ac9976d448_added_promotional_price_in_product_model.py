"""Added promotional price in Product model

Revision ID: c3ac9976d448
Revises: 43edede32146
Create Date: 2020-05-14 21:30:27.243663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3ac9976d448'
down_revision = '43edede32146'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('product', sa.Column('promotional_price', sa.Float(), nullable=False))


def downgrade():
    op.drop_column('product', 'promotional_price')
