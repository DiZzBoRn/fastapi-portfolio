"""add new column

Revision ID: ba231239ac57
Revises: fc462bcbf1ce
Create Date: 2022-11-29 17:27:53.457803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba231239ac57'
down_revision = 'fc462bcbf1ce'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
