"""Changed column birthday to birthdate

Revision ID: 7ea1ea99a41b
Revises: 65bc55481047
Create Date: 2025-05-24 08:35:37.543473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ea1ea99a41b'
down_revision = '65bc55481047'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students", "birthday", new_column_name="birthdate")


def downgrade() -> None:
    op.alter_column("students", "birthdate", new_column_name="birthday")
    