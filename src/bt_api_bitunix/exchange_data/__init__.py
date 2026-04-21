from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class BitunixExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "BITUNIX"
        self.rest_url = "https://fapi.bitunix.com"
        self.wss_url = "wss://fapi.bitunix.com/public"
        self.kline_periods = {
            "1m": "1m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1h": "1h",
            "4h": "4h",
            "1d": "1d",
            "1w": "1w",
        }
        self.legal_currency = ["USDT", "USD"]
        self.rest_paths = {}
        self.wss_paths = {}


class BitunixExchangeDataSpot(BitunixExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "spot"
