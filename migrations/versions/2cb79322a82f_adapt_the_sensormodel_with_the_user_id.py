"""Adapt the SensorModel with the user_id

Revision ID: 2cb79322a82f
Revises: 368fb3bbfddc
Create Date: 2024-11-03 09:24:39.359638

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2cb79322a82f"
down_revision = "368fb3bbfddc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("sensor", schema=None) as batch_op:
        batch_op.add_column(sa.Column("user_id", sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, "users", ["user_id"], ["id"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("sensor", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("user_id")

    # ### end Alembic commands ###
