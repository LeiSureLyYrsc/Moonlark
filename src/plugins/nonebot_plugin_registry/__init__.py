from nonebot import require
from nonebot.plugin import PluginMetadata


__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_registry",
    description="",
    usage="",
)

require("nonebot_plugin_orm")
require("nonebot_plugin_larklang")
require("nonebot_plugin_larkutils")
require("nonebot_plugin_larkuser")
require("nonebot_plugin_preview")
require("nonebot_plugin_alconna")

from . import __main__
