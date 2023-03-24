"""empty message

Revision ID: 96e0eb836a5d
Revises: ec5500eca8c0
Create Date: 2023-03-23 21:35:28.289733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96e0eb836a5d'
down_revision = 'ec5500eca8c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calls', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_calls_user_name'), ['user_name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calls', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_calls_user_name'))

    # ### end Alembic commands ###
