"""empty message

迁移 ID: 70f7d8846114
父迁移: f5a0425a1baf
创建时间: 2025-01-19 15:28:05.843908

"""

from __future__ import annotations

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision: str = "70f7d8846114"
down_revision: str | Sequence[str] | None = "f5a0425a1baf"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_openai_gptuser",
        sa.Column("user_id", sa.String(length=128), nullable=False),
        sa.Column("session_id", sa.Integer(), nullable=True),
        sa.Column("used_token", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_nonebot_plugin_openai_gptuser")),
        info={"bind_key": "nonebot_plugin_openai"},
    )
    op.create_table(
        "nonebot_plugin_openai_sessionmessage",
        sa.Column("message_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("session_id", sa.Integer(), nullable=False),
        sa.Column("content", sa.LargeBinary(), nullable=False),
        sa.Column("role", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("message_id", name=op.f("pk_nonebot_plugin_openai_sessionmessage")),
        info={"bind_key": "nonebot_plugin_openai"},
    )
    op.drop_table("nonebot_plugin_openai_user")
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_openai_user",
        sa.Column("user_id", mysql.VARCHAR(length=128), nullable=False),
        sa.Column("tokens", mysql.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("free_count", mysql.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("plus", mysql.DATETIME(), nullable=True),
        sa.PrimaryKeyConstraint("user_id"),
        mysql_collate="utf8mb4_0900_ai_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    op.drop_table("nonebot_plugin_openai_sessionmessage")
    op.drop_table("nonebot_plugin_openai_gptuser")
    # ### end Alembic commands ###
