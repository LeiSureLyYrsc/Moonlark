"""empty message

迁移 ID: 8536e8703b40
父迁移: 2496bf44d32c
创建时间: 2024-11-10 03:18:39.371736

"""

from __future__ import annotations

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "8536e8703b40"
down_revision: str | Sequence[str] | None = "2496bf44d32c"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_wakatime_user",
        sa.Column("user_id", sa.String(length=128), nullable=False),
        sa.Column("access_token", sa.String(length=256), nullable=False),
        sa.Column("expired_at", sa.Double(), nullable=False),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_nonebot_plugin_wakatime_user")),
        info={"bind_key": "nonebot_plugin_wakatime"},
    )
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_wakatime_user")
    # ### end Alembic commands ###
