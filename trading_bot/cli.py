import argparse
import sys
import os

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from trading_bot.binance_client import BinanceFuturesClient
from trading_bot.logger import setup_logger

logger = setup_logger()

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Market Order: python -m trading_bot.cli --api-key KEY --api-secret SECRET --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
  Limit Order:  python -m trading_bot.cli --api-key KEY --api-secret SECRET --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000.0
        """
    )
    
    # Required arguments
    parser.add_argument("--api-key", required=True, help="Binance API Key")
    parser.add_argument("--api-secret", required=True, help="Binance API Secret")
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], 
                        help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], 
                        help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", type=float, required=True, 
                        help="Order quantity")
    parser.add_argument("--price", type=float, 
                        help="Limit price (required for LIMIT orders)")

    args = parser.parse_args()

    # ==========================================
    # Input Validation
    # ==========================================
    if args.type == "LIMIT" and args.price is None:
        logger.error("Validation Failed: --price is required for LIMIT orders.")
        print("\n❌ Error: --price is required for LIMIT orders.")
        sys.exit(1)
    
    if args.quantity <= 0:
        logger.error("Validation Failed: Quantity must be positive.")
        print("\n❌ Error: Quantity must be positive.")
        sys.exit(1)

    client = BinanceFuturesClient(args.api_key, args.api_secret)
    logger.info(f"Processing Order: {args.side} {args.type} on {args.symbol}")

    result = client.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    if result["success"]:
        data = result["data"]
        print("\n" + "="*35)
        print("ORDER EXECUTED SUCCESSFULLY")
        print("="*35)
        print(f"Order ID:    {data.get('orderId')}")
        print(f"Symbol:     {data.get('symbol')}")
        print(f"Side:       {data.get('side')}")
        print(f"Type:       {data.get('type')}")
        print(f"Status:     {data.get('status')}")
        print(f"Executed:   {data.get('executedQty')}")
        print(f"Avg Price:  {data.get('avgPrice', 'N/A')}")
        print("="*35)
    else:
        print("\n" + "="*35)
        print("ORDER FAILED")
        print("="*35)
        print(f"Error: {result['error']}")
        print("="*35)
        sys.exit(1)

if __name__ == "__main__":
    main()
