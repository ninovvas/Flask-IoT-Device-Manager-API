"""Add user_id in Sensor Schedule model

Revision ID: 47d3f4666acd
Revises: a416e2842885
Create Date: 2024-11-03 15:57:49.353267

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '47d3f4666acd'
down_revision = 'a416e2842885'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sensor_schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sensor_schedule', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
