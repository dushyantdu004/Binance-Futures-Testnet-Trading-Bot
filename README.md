# Binance Futures Testnet Trading Bot

A Python CLI application to execute Market and Limit orders on Binance Futures Testnet (USDT-M).

## 📋 Features

- ✅ Market and Limit order placement
- ✅ Buy and Sell order sides
- ✅ Structured logging to file (`logs/bot.log`)
- ✅ Input validation and error handling
- ✅ Modular architecture (API/CLI/Logging layers)

## 🚀 Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
Get Testnet Credentials
Go to Binance Futures Testnet
Log in or register an account
Navigate to API Key management
Create a new API Key (Enable "Futures" permissions)
Copy your API Key and API Secret
💻 How to Run
1. Place a Market Order (BUY)
bash

Copy code
python -m trading_bot.cli \
  --api-key YOUR_API_KEY \
  --api-secret YOUR_API_SECRET \
  --symbol BTCUSDT \
  --side BUY \
  --type MARKET \
  --quantity 0.01
2. Place a Limit Order (SELL)
bash

Copy code
python -m trading_bot.cli \
  --api-key YOUR_API_KEY \
  --api-secret YOUR_API_SECRET \
  --symbol BTCUSDT \
  --side SELL \
  --type LIMIT \
  --quantity 0.01 \
  --price 65000.0
📖 CLI Arguments
Argument

Required

Description

Example

--api-key

Yes

Binance API Key

your_key_here

--api-secret

Yes

Binance API Secret

your_secret_here

--symbol

Yes

Trading pair

BTCUSDT, ETHUSDT

--side

Yes

Order side

BUY, SELL

--type

Yes

Order type

MARKET, LIMIT

--quantity

Yes

Order quantity

0.01, 1.5

--price

Only for LIMIT

Limit price

65000.0

📂 Logs
Logs are saved in logs/bot.log with timestamps, requests, responses, and errors.

Sample Log Output
text

Copy code
2023-10-27 10:30:15,456 - trading_bot - INFO: Initialized Binance Testnet Client
2023-10-27 10:30:20,123 - trading_bot - INFO: Processing Order: BUY MARKET on BTCUSDT
2023-10-27 10:30:20,125 - trading_bot - INFO: REQUEST: Placing MARKET BUY order for BTCUSDT. Qty: 0.01
2023-10-27 10:30:20,456 - trading_bot - INFO: RESPONSE: Order ID 98239321 | Status NEW
🏗️ Architecture

Copy code
trading_bot/
├── binance_client.py   # API Layer - Handles Binance connection and order execution
├── logger.py         # Logging Layer - Handles file and console logging
└── cli.py           # CLI Layer - Handles input parsing and validation
🔧 Error Handling
The bot handles the following:

Invalid input (missing required arguments)
Network failures
API errors (insufficient balance, invalid symbol, etc.)
📝 License
MIT License


Copy code

---

### 📄 File 3: `trading_bot/__init__.py`

```python
# trading_bot/__init__.py
"""Binance Futures Testnet Trading Bot"""

__version__ = "1.0.0"
