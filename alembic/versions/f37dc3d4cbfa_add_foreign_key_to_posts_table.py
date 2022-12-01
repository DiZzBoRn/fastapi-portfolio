"""add foreign key to posts table

Revision ID: f37dc3d4cbfa
Revises: 067078154fc8
Create Date: 2022-11-29 17:41:06.434663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f37dc3d4cbfa'
down_revision = '067078154fc8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', 
        source_table='posts', 
        referent_table='users',
        local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE' 
        )
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fkey', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
