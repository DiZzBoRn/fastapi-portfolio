"""create post table

Revision ID: fc462bcbf1ce
Revises: 
Create Date: 2022-11-29 17:19:49.588072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc462bcbf1ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', 
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
