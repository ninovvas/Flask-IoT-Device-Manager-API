"""Add SensorDataModel

Revision ID: 83290f1c35ee
Revises: a39562fdfade
Create Date: 2024-11-02 10:58:10.438942

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "83290f1c35ee"
down_revision = "a39562fdfade"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sensor_data",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("sensor_id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["sensor_id"],
            ["sensor.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sensor_data")
    # ### end Alembic commands ###
