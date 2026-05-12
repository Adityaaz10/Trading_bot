import logging
import sys

def setup_logger():
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)
    
    # Avoid duplicate logs if instantiated multiple times
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Log to file
        file_handler = logging.FileHandler("trading_bot.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Log to console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger