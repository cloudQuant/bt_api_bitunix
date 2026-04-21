"""Tests for BitunixExchangeData container."""

from __future__ import annotations

from bt_api_bitunix.exchange_data import BitunixExchangeData


class TestBitunixExchangeData:
    """Tests for BitunixExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = BitunixExchangeData()

        assert exchange.exchange_name == "BITUNIX"
