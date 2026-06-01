from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging

logger = logging.getLogger("trading_bot")

class BinanceFuturesClient:
    """
    Wrapper class for Binance Futures Testnet API.
    Handles order placement and error handling.
    """
    
    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize the Binance client with testnet=True.
        
        Args:
            api_key: Binance API Key
            api_secret: Binance API Secret
        """
        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("Initialized Binance Testnet Client")

    def place_order(self, symbol: str, side: str, order_type: str, 
                   quantity: float, price: float = None):
        """
        Place an order on Binance Futures Testnet.
        
        Args:
            symbol: Trading pair (e.g., BTCUSDT)
            side: BUY or SELL
            order_type: MARKET or LIMIT
            quantity: Order quantity
            price: Limit price (required for LIMIT orders)
            
        Returns:
            Dictionary with success status and data/error
        """
        try:
            # Build order payload
            payload = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            # Add limit-specific parameters
            if order_type == "LIMIT":
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                payload["price"] = price
                payload["timeInForce"] = "GTC"  # Good Till Cancel
            
            # Log Request
            logger.info(f"REQUEST: Placing {order_type} {side} order for {symbol}. Qty: {quantity}")
            if price:
                logger.info(f"REQUEST: Limit Price: {price}")

            # Execute Order
            response = self.client.futures_create_order(**payload)
            
            # Log Response
            logger.info(f"RESPONSE: Order ID {response.get('orderId')} | Status {response.get('status')}")
            
            return {
                "success": True,
                "data": response
            }

        except BinanceAPIException as e:
            logger.error(f"API ERROR: {e.status_code} - {e.message}")
            return {"success": False, "error": e.message}
        except Exception as e:
            logger.error(f"SYSTEM ERROR: {str(e)}")
            return {"success": False, "error": str(e)}
