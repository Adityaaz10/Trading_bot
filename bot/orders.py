from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger

logger = setup_logger()

class OrderManager:
    def __init__(self, api_key, api_secret):
        self.client = BinanceFuturesClient(api_key, api_secret)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"
        
        # Core parameters required by Binance Futures (USDT-M)
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        # Additional parameters required for LIMIT orders
        if order_type.upper() == "LIMIT":
            params["timeInForce"] = "GTC" # Good Till Canceled
            params["price"] = price

        logger.info(f"Summary: Requesting {order_type.upper()} order. {side.upper()} {quantity} {symbol.upper()}.")

        try:
            response = self.client.send_signed_request("POST", endpoint, params)
            
            # Extract details for terminal output
            order_id = response.get('orderId')
            status = response.get('status')
            executed_qty = response.get('executedQty')
            avg_price = response.get('avgPrice', 'N/A')
            
            logger.info("SUCCESS: Order successfully placed!")
            logger.info(f"Order Details -> ID: {order_id} | Status: {status} | Executed Qty: {executed_qty} | Avg Price: {avg_price}")
            
            return response
            
        except Exception as e:
            logger.error("FAILURE: Order placement failed. See logs above for details.")
            # We catch it here to print a clean failure message, but allow the app to exit cleanly