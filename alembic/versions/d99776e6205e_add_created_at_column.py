"""add created at column

Revision ID: d99776e6205e
Revises: 8cbe32036263
Create Date: 2025-06-18 16:29:09.064090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd99776e6205e'
down_revision: Union[str, Sequence[str], None] = '8cbe32036263'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_posts_created_at', 'posts', ['created_at'], unique=False)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_posts_created_at', table_name='posts')
    op.drop_column('posts', 'created_at')
    pass
