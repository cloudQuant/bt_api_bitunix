from __future__ import annotations

from bt_api_base.registry import ExchangeRegistry

from bt_api_bitunix.feeds.live_bitunix.spot import BitunixRequestDataSpot
from bt_api_bitunix.plugin import BitunixPlugin


def register_bitunix():
    plugin = BitunixPlugin()
    info = plugin.get_plugin_info()
    exchange_data = plugin.get_exchange_data("SPOT")
    ExchangeRegistry.register(
        exchange_name="BITUNIX___SPOT",
        exchange_data=exchange_data,
        feed_class=BitunixRequestDataSpot,
        plugin_info=info,
    )


__all__ = ["register_bitunix"]
