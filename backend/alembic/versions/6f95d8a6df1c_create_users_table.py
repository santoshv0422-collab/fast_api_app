"""create users table

Revision ID: 6f95d8a6df1c
Revises: 21668c0de9b4
Create Date: 2026-07-02 10:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


revision: str = "6f95d8a6df1c"
down_revision: Union[str, Sequence[str], None] = "21668c0de9b4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = inspect(bind)

    if inspector.has_table("users"):
        columns = {column["name"] for column in inspector.get_columns("users")}
        if "name" not in columns:
            op.add_column("users", sa.Column("name", sa.String(length=255), nullable=False))
        if "email" not in columns:
            op.add_column("users", sa.Column("email", sa.String(length=255), nullable=False))
        if "password" not in columns:
            op.add_column("users", sa.Column("password", sa.String(length=255), nullable=False))
        if "role" not in columns:
            op.add_column(
                "users",
                sa.Column("role", sa.String(length=255), nullable=False, server_default="user"),
            )
        return

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("role", sa.String(length=255), nullable=False, server_default="user"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)


def downgrade() -> None:
    bind = op.get_bind()
    inspector = inspect(bind)

    if inspector.has_table("users"):
        op.drop_index(op.f("ix_users_id"), table_name="users")
        op.drop_table("users")
