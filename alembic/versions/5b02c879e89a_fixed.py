"""fixed

Revision ID: 5b02c879e89a
Revises: 61dc82fdd8a4
Create Date: 2022-08-30 15:49:16.126282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b02c879e89a'
down_revision = '61dc82fdd8a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('days', schema=None) as batch_op:
        batch_op.drop_index('ix_days_id')

    op.drop_table('days')
    with op.batch_alter_table('requester', schema=None) as batch_op:
        batch_op.drop_index('ix_requester_id')

    op.drop_table('requester')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.drop_index('ix_users_id')
        batch_op.drop_index('ix_users_username')

    op.drop_table('users')
    with op.batch_alter_table('kitchen', schema=None) as batch_op:
        batch_op.drop_index('ix_kitchen_id')

    op.drop_table('kitchen')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kitchen',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('menu', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('kitchen', schema=None) as batch_op:
        batch_op.create_index('ix_kitchen_id', ['id'], unique=False)

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

    op.create_table('requester',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('days', sa.INTEGER(), nullable=True),
    sa.Column('attendance', sa.BOOLEAN(), nullable=True),
    sa.Column('owner_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('requester', schema=None) as batch_op:
        batch_op.create_index('ix_requester_id', ['id'], unique=False)

    op.create_table('days',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('dow', sa.DATE(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('days', schema=None) as batch_op:
        batch_op.create_index('ix_days_id', ['id'], unique=False)

    # ### end Alembic commands ###
