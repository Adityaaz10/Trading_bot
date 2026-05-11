def validate_inputs(symbol, side, order_type, quantity, price):
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be exactly 'BUY' or 'SELL'.")
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be exactly 'MARKET' or 'LIMIT'.")
    if float(quantity) <= 0:
        raise ValueError("Quantity must be a positive number.")
    if order_type.upper() == 'LIMIT' and price is None:
        raise ValueError("A price must be provided for LIMIT orders.")
    if price is not None and float(price) <= 0:
        raise ValueError("Price must be a positive number.")
    return True