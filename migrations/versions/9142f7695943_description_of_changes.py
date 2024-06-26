"""Description of changes

Revision ID: 9142f7695943
Revises: 
Create Date: 2024-04-23 20:04:37.732613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9142f7695943'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('date_changes', sa.DateTime(), nullable=True),
    sa.Column('task', sa.String(length=1000), nullable=True),
    sa.Column('is_complite', sa.Boolean(), server_default='False', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exchange',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('rate', sa.Float(), server_default='100.0', nullable=False),
    sa.Column('currency', sa.String(length=10), server_default='USDT', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_id',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.Column('full_name', sa.String(length=1000), nullable=True),
    sa.Column('first_name', sa.String(length=1000), nullable=True),
    sa.Column('last_name', sa.String(length=1000), nullable=True),
    sa.Column('currency', sa.String(length=100), server_default='RUB', nullable=False),
    sa.Column('lang', sa.String(length=100), server_default='RUS', nullable=False),
    sa.Column('show_balance', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('cash', sa.Float(), server_default='0', nullable=False),
    sa.Column('cards', sa.Float(), server_default='0', nullable=False),
    sa.Column('money_currency', sa.String(length=10), server_default='RUB', nullable=False),
    sa.Column('crypto', sa.Float(), server_default='0', nullable=False),
    sa.Column('crypto_currency', sa.String(length=10), server_default='USDT', nullable=False),
    sa.Column('is_admin', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('is_block', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('did_you_donate', sa.Float(), server_default='0', nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id_id'), 'user_id', ['id'], unique=True)
    op.create_table('sessions',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('category', sa.String(length=1000), server_default='is no category', nullable=False),
    sa.Column('ml_category', sa.String(length=1000), server_default='is no category', nullable=False),
    sa.Column('flow', sa.String(length=50), server_default='-', nullable=False),
    sa.Column('amount', sa.Float(), server_default='0', nullable=False),
    sa.Column('is_cash', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('is_cards', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('is_crypto', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('users_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['user_id.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('date_changes', sa.DateTime(), nullable=True),
    sa.Column('task', sa.String(length=1000), nullable=True),
    sa.Column('is_complite', sa.Boolean(), server_default='False', nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user_id.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_table('sessions')
    op.drop_index(op.f('ix_user_id_id'), table_name='user_id')
    op.drop_table('user_id')
    op.drop_table('exchange')
    op.drop_table('backup')
    # ### end Alembic commands ###
