"""create initial tables

Revision ID: 1d431efc41e8
Revises: 
Create Date: 2025-05-20 03:19:17.618338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d431efc41e8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_keys',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('key_value', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('last_used_at', sa.DateTime(), nullable=True),
    sa.Column('usage_count', sa.Integer(), nullable=True),
    sa.Column('failed_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_api_keys_id'), 'api_keys', ['id'], unique=False)
    op.create_index(op.f('ix_api_keys_key_value'), 'api_keys', ['key_value'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('config',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_by_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['updated_by_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_config_id'), 'config', ['id'], unique=False)
    op.create_index(op.f('ix_config_key'), 'config', ['key'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_config_key'), table_name='config')
    op.drop_index(op.f('ix_config_id'), table_name='config')
    op.drop_table('config')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_api_keys_key_value'), table_name='api_keys')
    op.drop_index(op.f('ix_api_keys_id'), table_name='api_keys')
    op.drop_table('api_keys')
    # ### end Alembic commands ###
