"""add last few columns

Revision ID: ca669b10264b
Revises: f37dc3d4cbfa
Create Date: 2022-11-29 17:48:50.540963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca669b10264b'
down_revision = 'f37dc3d4cbfa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', 
        sa.Column('published', 
        sa.Boolean(), 
        server_default='TRUE',
        nullable=False),
        )
    op.add_column('posts', 
        sa.Column('created_at', 
        sa.TIMESTAMP(timezone=True), 
        nullable=False, 
        server_default=sa.text('now()')
        ))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
