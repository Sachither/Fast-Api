"""add more column to post table

Revision ID: cff73066c28f
Revises: e0434621ca81
Create Date: 2025-06-18 15:54:08.286881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cff73066c28f'
down_revision: Union[str, Sequence[str], None] = 'e0434621ca81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='true'))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    pass
