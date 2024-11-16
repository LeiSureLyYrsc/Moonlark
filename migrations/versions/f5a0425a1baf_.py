"""empty message

迁移 ID: f5a0425a1baf
父迁移: e9746d85ff25
创建时间: 2024-11-16 00:37:34.684805

"""

from __future__ import annotations

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision: str = "f5a0425a1baf"
down_revision: str | Sequence[str] | None = "e9746d85ff25"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("nonebot_plugin_larklang_languagekeycache", schema=None) as batch_op:
        batch_op.alter_column(
            "plugin", existing_type=mysql.VARCHAR(length=20), type_=sa.String(length=32), existing_nullable=False
        )
        batch_op.alter_column(
            "key", existing_type=mysql.VARCHAR(length=32), type_=sa.String(length=64), existing_nullable=False
        )

    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("nonebot_plugin_larklang_languagekeycache", schema=None) as batch_op:
        batch_op.alter_column(
            "key", existing_type=sa.String(length=64), type_=mysql.VARCHAR(length=32), existing_nullable=False
        )
        batch_op.alter_column(
            "plugin", existing_type=sa.String(length=32), type_=mysql.VARCHAR(length=20), existing_nullable=False
        )

    # ### end Alembic commands ###
