# Bitunix Exchange Plugin for bt_api

## Bitunix | 比特统一

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_bitunix.svg)](https://pypi.org/project/bt_api_bitunix/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_bitunix.svg)](https://pypi.org/project/bt_api_bitunix/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_bitunix/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_bitunix/actions)
[![Docs](https://readthedocs.org/projects/bt-api-bitunix/badge/?version=latest)](https://bt-api-bitunix.readthedocs.io/)

---

## English | [中文](#中文)

### Overview

This package provides **Bitunix exchange plugin** for the [bt_api](https://github.com/cloudQuant/bt_api_py) framework. It offers a unified interface for interacting with **Bitunix**, a cryptocurrency exchange offering futures trading.

Bitunix provides trading in USDT and USD with various cryptocurrency pairs. This plugin integrates Bitunix's REST API into the bt_api unified trading framework.

### Key Features

- **Complete REST API Coverage**: Ticker, order book, klines, orders, balances
- **HMAC-SHA256 Authentication**: Secure double SHA256 signature authentication
- **Unified Interface**: Compatible with bt_api's BtApi, EventBus, and data containers
- **Async Support**: Full async/await support for concurrent operations

### Exchange Information

| Item | Value |
|------|-------|
| Exchange Name | Bitunix |
| Trading Code | `BITUNIX___SPOT` |
| REST API URL | `https://fapi.bitunix.com` |
| WebSocket URL | `wss://fapi.bitunix.com/public` |
| Asset Type | SPOT |
| Supported Currencies | USDT, USD |
| Authentication | HMAC-SHA256 (double hash) |

### Installation

#### From PyPI (Recommended)

```bash
pip install bt_api_bitunix
```

#### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_bitunix
cd bt_api_bitunix
pip install -e .
```

### Quick Start

#### Initialize the Exchange

```python
from bt_api_py import BtApi

# Configure Bitunix exchange
exchange_config = {
    "BITUNIX___SPOT": {
        "api_key": "your_api_key",
        "secret_key": "your_secret_key",
    }
}

# Initialize BtApi
api = BtApi(exchange_kwargs=exchange_config)
```

#### Get Market Data

```python
# Get ticker
ticker = api.get_tick("BITUNIX___SPOT", "BTCUSDT")
print(ticker)

# Get order book depth
depth = api.get_depth("BITUNIX___SPOT", "BTCUSDT", limit=20)
print(depth)

# Get kline/candlestick data
klines = api.get_kline("BITUNIX___SPOT", "BTCUSDT", period="1h", count=100)
print(klines)

# Get exchange info (available trading pairs)
exchange_info = api.get_exchange_info("BITUNIX___SPOT")
print(exchange_info)
```

#### Trading Operations

```python
# Place an order
order = api.make_order(
    exchange_name="BITUNIX___SPOT",
    symbol="BTCUSDT",
    volume=0.01,
    price=50000,
    order_type="limit",
)
print(order)

# Cancel an order
cancel_result = api.cancel_order(
    exchange_name="BITUNIX___SPOT",
    symbol="BTCUSDT",
    order_id="your_order_id",
)
print(cancel_result)

# Query order status
order_info = api.query_order(
    exchange_name="BITUNIX___SPOT",
    symbol="BTCUSDT",
    order_id="your_order_id",
)
print(order_info)

# Get open orders
open_orders = api.get_open_orders("BITUNIX___SPOT", "BTCUSDT")
print(open_orders)

# Get account balance
balance = api.get_balance("BITUNIX___SPOT")
print(balance)

# Get account info
account = api.get_account("BITUNIX___SPOT")
print(account)
```

#### Asynchronous Operations

```python
import asyncio
from bt_api_py import BtApi

async def main():
    api = BtApi(exchange_kwargs={
        "BITUNIX___SPOT": {
            "api_key": "your_api_key",
            "secret_key": "your_secret_key",
        }
    })

    # Async get ticker
    ticker = await api.async_get_tick("BITUNIX___SPOT", "BTCUSDT")
    print(ticker)

    # Async place order
    order = await api.async_make_order(
        exchange_name="BITUNIX___SPOT",
        symbol="BTCUSDT",
        volume=0.01,
        price=50000,
        order_type="limit",
    )
    print(order)

asyncio.run(main())
```

### Supported Operations

| Operation | REST API | Description |
|-----------|----------|-------------|
| `get_tick` | GET /api/v1/futures/market/tickers | Get ticker data |
| `get_depth` | GET /api/v1/futures/market/depth | Get order book depth |
| `get_kline` | GET /api/v1/futures/market/klines | Get candlestick/kline data |
| `get_exchange_info` | GET /api/v1/futures/market/symbols | Get available trading pairs |
| `make_order` | POST /api/v1/futures/trade/place_order | Place a new order |
| `cancel_order` | POST /api/v1/futures/trade/cancel_order | Cancel an order |
| `query_order` | GET /api/v1/futures/trade/get_order | Query order status |
| `get_open_orders` | GET /api/v1/futures/trade/get_open_orders | Get all open orders |
| `get_balance` | GET /api/v1/futures/account/balance | Get account balance |
| `get_account` | GET /api/v1/futures/account | Get account information |

### Symbol Format

Bitunix uses standard symbol format:

| bt_api Symbol | Bitunix Symbol |
|---------------|----------------|
| `BTCUSDT` | `BTCUSDT` |
| `ETHUSDT` | `ETHUSDT` |
| `XRPUSDT` | `XRPUSDT` |

The plugin automatically handles symbol formatting.

### Authentication

Bitunix API uses HMAC-SHA256 double hash authentication:

```
Step 1: hash1 = SHA256(nonce + timestamp + api_key + query_params + body)
Step 2: signature = SHA256(hash1 + api_secret)
```

Required headers:
- `api-key` — API key
- `nonce` — UUID (32 characters)
- `timestamp` — Unix timestamp in milliseconds
- `sign` — HMAC-SHA256 signature

### Kline Periods

| Period | Bitunix Code |
|--------|--------------|
| 1 minute | 1m |
| 5 minutes | 5m |
| 15 minutes | 15m |
| 30 minutes | 30m |
| 1 hour | 1h |
| 4 hours | 4h |
| 1 day | 1d |
| 1 week | 1w |

### Error Handling

All API errors are translated to bt_api's standard error types:

```python
from bt_api_py.errors import (
    RateLimitError,
    AuthenticationError,
    OrderNotFoundError,
    InsufficientBalanceError,
)
```

### Online Documentation

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-bitunix.readthedocs.io/ |
| Chinese Docs | https://bt-api-bitunix.readthedocs.io/zh/latest/ |
| GitHub Repository | https://github.com/cloudQuant/bt_api_bitunix |
| Issue Tracker | https://github.com/cloudQuant/bt_api_bitunix/issues |

### Architecture

```
bt_api_bitunix/
├── src/bt_api_bitunix/           # Source code
│   ├── containers/              # Data containers
│   │   ├── balances/           # Balance data containers
│   │   ├── orders/             # Order data containers
│   │   ├── tickers/            # Ticker data containers
│   │   ├── bars/               # Bar data containers
│   │   ├── orderbooks/         # OrderBook data containers
│   │   └── accounts/           # Account data containers
│   ├── exchange_data/           # Exchange configuration
│   │   └── __init__.py        # BitunixExchangeData class
│   ├── feeds/                  # API feeds
│   │   └── live_bitunix/      # Live trading feed
│   │       ├── __init__.py    # BitunixRequestData base class
│   │       ├── spot.py         # Spot trading feed
│   │       └── request_base.py # Request base with signature logic
│   ├── errors/                  # Error translations
│   └── plugin.py              # Plugin registration
├── tests/                      # Unit tests
└── docs/                      # Documentation
```

### Requirements

| Dependency | Version | Description |
|------------|---------|-------------|
| Python | >= 3.9 | Programming language |
| bt_api_base | >= 0.15 | Core framework |

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

MIT License - see [LICENSE](LICENSE) for details.

### Support

- Report bugs via [GitHub Issues](https://github.com/cloudQuant/bt_api_bitunix/issues)
- Email: yunjinqi@gmail.com

---

## 中文

### 概述

本包为 [bt_api](https://github.com/cloudQuant/bt_api_py) 框架提供 **Bitunix（比特统一）交易所插件**。Bitunix 是一家提供期货交易的加密货币交易所。

Bitunix 提供 USDT 和 USD 交易，以及各种加密货币交易对。本插件将 Bitunix 的 REST API 集成到 bt_api 统一交易框架中。

### 核心功能

- **完整 REST API 覆盖**：行情、订单簿、K线、订单、余额
- **HMAC-SHA256 认证**：安全的双重 SHA256 签名认证
- **统一接口**：与 bt_api 的 BtApi、EventBus 和数据容器完全兼容
- **异步支持**：完整的 async/await 支持并发操作

### 交易所信息

| 项目 | 值 |
|------|-------|
| 交易所名称 | Bitunix（比特统一） |
| 交易代码 | `BITUNIX___SPOT` |
| REST API 地址 | `https://fapi.bitunix.com` |
| WebSocket 地址 | `wss://fapi.bitunix.com/public` |
| 资产类型 | 现货（SPOT） |
| 支持法币 | USDT, USD |
| 认证方式 | HMAC-SHA256（双重哈希） |

### 安装

#### 从 PyPI 安装（推荐）

```bash
pip install bt_api_bitunix
```

#### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_bitunix
cd bt_api_bitunix
pip install -e .
```

### 快速开始

#### 初始化交易所

```python
from bt_api_py import BtApi

# 配置 Bitunix 交易所
exchange_config = {
    "BITUNIX___SPOT": {
        "api_key": "your_api_key",
        "secret_key": "your_secret_key",
    }
}

# 初始化 BtApi
api = BtApi(exchange_kwargs=exchange_config)
```

#### 获取市场数据

```python
# 获取行情
ticker = api.get_tick("BITUNIX___SPOT", "BTCUSDT")
print(ticker)

# 获取订单簿深度
depth = api.get_depth("BITUNIX___SPOT", "BTCUSDT", limit=20)
print(depth)

# 获取 K 线数据
klines = api.get_kline("BITUNIX___SPOT", "BTCUSDT", period="1h", count=100)
print(klines)

# 获取交易所信息（可用交易对）
exchange_info = api.get_exchange_info("BITUNIX___SPOT")
print(exchange_info)
```

#### 交易操作

```python
# 下单
order = api.make_order(
    exchange_name="BITUNIX___SPOT",
    symbol="BTCUSDT",
    volume=0.01,
    price=50000,
    order_type="limit",
)
print(order)

# 取消订单
cancel_result = api.cancel_order(
    exchange_name="BITUNIX___SPOT",
    symbol="BTCUSDT",
    order_id="your_order_id",
)
print(cancel_result)

# 查询订单状态
order_info = api.query_order(
    exchange_name="BITUNIX___SPOT",
    symbol="BTCUSDT",
    order_id="your_order_id",
)
print(order_info)

# 获取挂单
open_orders = api.get_open_orders("BITUNIX___SPOT", "BTCUSDT")
print(open_orders)

# 获取账户余额
balance = api.get_balance("BITUNIX___SPOT")
print(balance)

# 获取账户信息
account = api.get_account("BITUNIX___SPOT")
print(account)
```

#### 异步操作

```python
import asyncio
from bt_api_py import BtApi

async def main():
    api = BtApi(exchange_kwargs={
        "BITUNIX___SPOT": {
            "api_key": "your_api_key",
            "secret_key": "your_secret_key",
        }
    })

    # 异步获取行情
    ticker = await api.async_get_tick("BITUNIX___SPOT", "BTCUSDT")
    print(ticker)

    # 异步下单
    order = await api.async_make_order(
        exchange_name="BITUNIX___SPOT",
        symbol="BTCUSDT",
        volume=0.01,
        price=50000,
        order_type="limit",
    )
    print(order)

asyncio.run(main())
```

### 支持的操作

| 操作 | REST API | 说明 |
|------|----------|------|
| `get_tick` | GET /api/v1/futures/market/tickers | 获取行情数据 |
| `get_depth` | GET /api/v1/futures/market/depth | 获取订单簿深度 |
| `get_kline` | GET /api/v1/futures/market/klines | 获取 K 线/蜡烛图数据 |
| `get_exchange_info` | GET /api/v1/futures/market/symbols | 获取可用交易对 |
| `make_order` | POST /api/v1/futures/trade/place_order | 下新订单 |
| `cancel_order` | POST /api/v1/futures/trade/cancel_order | 取消订单 |
| `query_order` | GET /api/v1/futures/trade/get_order | 查询订单状态 |
| `get_open_orders` | GET /api/v1/futures/trade/get_open_orders | 获取所有挂单 |
| `get_balance` | GET /api/v1/futures/account/balance | 获取账户余额 |
| `get_account` | GET /api/v1/futures/account | 获取账户信息 |

### 交易对格式

Bitunix 使用标准交易对格式：

| bt_api 交易对 | Bitunix 交易对 |
|----------------|----------------|
| `BTCUSDT` | `BTCUSDT` |
| `ETHUSDT` | `ETHUSDT` |
| `XRPUSDT` | `XRPUSDT` |

插件自动处理交易对格式。

### 认证方式

Bitunix API 使用 HMAC-SHA256 双重哈希认证：

```
第一步: hash1 = SHA256(nonce + timestamp + api_key + query_params + body)
第二步: signature = SHA256(hash1 + api_secret)
```

必需请求头：
- `api-key` — API 密钥
- `nonce` — UUID（32 个字符）
- `timestamp` — 毫秒级 Unix 时间戳
- `sign` — HMAC-SHA256 签名

### K 线周期

| 周期 | Bitunix 代码 |
|------|--------------|
| 1 分钟 | 1m |
| 5 分钟 | 5m |
| 15 分钟 | 15m |
| 30 分钟 | 30m |
| 1 小时 | 1h |
| 4 小时 | 4h |
| 1 天 | 1d |
| 1 周 | 1w |

### 错误处理

所有 API 错误都会转换为 bt_api 的标准错误类型：

```python
from bt_api_py.errors import (
    RateLimitError,          # 速率限制错误
    AuthenticationError,     # 认证错误
    OrderNotFoundError,      # 订单未找到
    InsufficientBalanceError,  # 余额不足
)
```

### 在线文档

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-bitunix.readthedocs.io/ |
| 中文文档 | https://bt-api-bitunix.readthedocs.io/zh/latest/ |
| GitHub 仓库 | https://github.com/cloudQuant/bt_api_bitunix |
| 问题反馈 | https://github.com/cloudQuant/bt_api_bitunix/issues |

### 系统要求

| 依赖 | 版本 | 说明 |
|------|------|------|
| Python | >= 3.9 | 编程语言 |
| bt_api_base | >= 0.15 | 核心框架 |

### 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

### 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE)。

### 技术支持

- 通过 [GitHub Issues](https://github.com/cloudQuant/bt_api_bitunix/issues) 反馈问题
- 邮箱: yunjinqi@gmail.com

---

如果这个项目对您有帮助，请给我们一个 Star！

[![Star History Chart](https://api.star-history.com/svg?repos=cloudQuant/bt_api_bitunix&type=Date)](https://star-history.com/#cloudQuant/bt_api_bitunix&Type=Date)
