"""Initial user migration

Revision ID: 6ae66dcc2956
Revises: 
Create Date: 2023-08-01 14:58:56.701015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ae66dcc2956'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table('user',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('email', sa.String, nullable=False, unique=True),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('name', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('user')
    pass