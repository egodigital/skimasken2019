"""empty message

Revision ID: 6c87bed46efa
Revises: 8893cffdd418
Create Date: 2019-10-17 17:47:13.993738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c87bed46efa'
down_revision = '8893cffdd418'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('environment_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.Column('user_name', sa.VARCHAR(), nullable=False),
    sa.Column('environment_id', sa.VARCHAR(), nullable=False),
    sa.Column('points', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    op.drop_table('user_model')
    # ### end Alembic commands ###
