import argparse
import os
from dotenv import load_dotenv
from bot.orders import OrderManager
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=['BUY', 'SELL'], help="Order side (BUY or SELL)")
    parser.add_argument("--type", required=True, choices=['MARKET', 'LIMIT'], help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", required=True, type=float, help="Amount to trade")
    parser.add_argument("--price", type=float, help="Limit price (Required if type is LIMIT)")

    args = parser.parse_args()

    # Load credentials
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("System Error: API credentials missing. Please set BINANCE_API_KEY and BINANCE_API_SECRET in the .env file.")
        return

    try:
        # 1. Validate Input
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
        
        # 2. Execute Order
        manager = OrderManager(api_key, api_secret)
        manager.place_order(args.symbol, args.side, args.type, args.quantity, args.price)

    except ValueError as ve:
        logger.error(f"Input Validation Error: {ve}")
    except Exception:
        # Exception is already handled and logged in the deeper layers
        pass

if __name__ == "__main__":
    main()