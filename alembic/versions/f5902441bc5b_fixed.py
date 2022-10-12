"""fixed

Revision ID: f5902441bc5b
Revises: a4a93d9d5362
Create Date: 2022-08-30 13:35:00.716526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5902441bc5b'
down_revision = 'a4a93d9d5362'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('days', schema=None) as batch_op:
        batch_op.drop_index('ix_days_id')

    op.drop_table('days')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.drop_index('ix_users_id')
        batch_op.drop_index('ix_users_username')

    op.drop_table('users')
    with op.batch_alter_table('requester', schema=None) as batch_op:
        batch_op.drop_index('ix_requester_id')

    op.drop_table('requester')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requester',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('menu', sa.VARCHAR(), nullable=True),
    sa.Column('days', sa.INTEGER(), nullable=True),
    sa.Column('attendance', sa.BOOLEAN(), nullable=True),
    sa.Column('owner_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('requester', schema=None) as batch_op:
        batch_op.create_index('ix_requester_id', ['id'], unique=False)

    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('first_name', sa.VARCHAR(), nullable=True),
    sa.Column('last_name', sa.VARCHAR(), nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_users_username', ['username'], unique=False)
        batch_op.create_index('ix_users_id', ['id'], unique=False)
        batch_op.create_index('ix_users_email', ['email'], unique=False)

    op.create_table('days',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('days', schema=None) as batch_op:
        batch_op.create_index('ix_days_id', ['id'], unique=False)

    # ### end Alembic commands ###
