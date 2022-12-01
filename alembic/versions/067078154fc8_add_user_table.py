"""add user table

Revision ID: 067078154fc8
Revises: ba231239ac57
Create Date: 2022-11-29 17:32:23.992400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '067078154fc8'
down_revision = 'ba231239ac57'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True),  
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
