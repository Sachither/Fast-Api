"""add foreign key to post table

Revision ID: 8cbe32036263
Revises: 9f8e8a093d44
Create Date: 2025-06-18 16:22:27.427855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cbe32036263'
down_revision: Union[str, Sequence[str], None] = '9f8e8a093d44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False),
        
    )
    op.create_foreign_key(
        'fk_posts_owner_id_users_id',
        'posts',
        'users',
        ['owner_id'],
        ['id'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_posts_owner_id_users_id', 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    
    pass
