"""empty message

Revision ID: f950c9d090eb
Revises: dc101cdc124c
Create Date: 2019-10-17 20:48:35.631537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f950c9d090eb'
down_revision = 'dc101cdc124c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking_model', schema=None) as batch_op:
        batch_op.alter_column('Fuzzy',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking_model', schema=None) as batch_op:
        batch_op.alter_column('Fuzzy',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    # ### end Alembic commands ###
