#!/bin/bash

# Create directory structure
mkdir -p trading_bot
mkdir -p logs

# Install dependencies
pip install -r requirements.txt

echo "✅ Setup complete! Run the bot with:"
echo "python -m trading_bot.cli --api-key YOUR_KEY --api-secret YOUR_SECRET --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01"
