from __future__ import annotations

from bt_api_base.plugins.protocol import PluginInfo
from bt_api_bitunix.exchange_data import BitunixExchangeDataSpot


class BitunixPlugin:
    @staticmethod
    def get_plugin_info() -> PluginInfo:
        return PluginInfo(
            name="bitunix",
            display_name="Bitunix",
            version="0.1.0",
            supported_asset_types=["SPOT"],
        )

    @staticmethod
    def get_exchange_data(asset_type: str = "SPOT"):
        if asset_type == "SPOT":
            return BitunixExchangeDataSpot()
        raise ValueError(f"Unsupported asset type: {asset_type}")
