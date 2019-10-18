"""empty message

Revision ID: 10d2929983a3
Revises: 967808d5a85c
Create Date: 2019-10-18 10:30:17.137865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d2929983a3'
down_revision = '967808d5a85c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('destination', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('distance', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('environment_id', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('public', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('vehicle_id', sa.String(), nullable=False))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String())
        batch_op.drop_column('end_time_fuzzy')
        batch_op.drop_column('start_time_fuzzy')
        batch_op.drop_column('duration')
        batch_op.drop_column('car_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('car_id', sa.VARCHAR(), nullable=False))
        batch_op.add_column(sa.Column('duration', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('start_time_fuzzy', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('end_time_fuzzy', sa.DATETIME(), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.String(),
               type_=sa.INTEGER())
        batch_op.drop_column('vehicle_id')
        batch_op.drop_column('public')
        batch_op.drop_column('environment_id')
        batch_op.drop_column('email')
        batch_op.drop_column('distance')
        batch_op.drop_column('destination')

    # ### end Alembic commands ###