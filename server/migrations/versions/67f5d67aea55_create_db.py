"""create db

Revision ID: 67f5d67aea55
Revises: 
Create Date: 2023-01-13 11:03:18.230084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f5d67aea55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('plants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('image', sa.String(), nullable=True),
        sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('plants')
