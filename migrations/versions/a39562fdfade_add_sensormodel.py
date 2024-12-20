"""Add SensorModel

Revision ID: a39562fdfade
Revises: ca6b72978c5e
Create Date: 2024-11-02 10:50:47.857559

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a39562fdfade"
down_revision = "ca6b72978c5e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sensor",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("sensor_type", sa.String(length=100), nullable=False),
        sa.Column("producer", sa.String(length=150), nullable=False),
        sa.Column("interface", sa.String(length=150), nullable=False),
        sa.Column("room_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["room_id"],
            ["room.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sensor")
    # ### end Alembic commands ###
