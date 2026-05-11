import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from bot.logging_config import setup_logger

logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://testnet.binancefuture.com"

    def _generate_signature(self, query_string):
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def send_signed_request(self, method, endpoint, payload=None):
        if payload is None:
            payload = {}
        
        # Binance requires a timestamp for security
        payload['timestamp'] = int(time.time() * 1000)
        query_string = urlencode(payload)
        signature = self._generate_signature(query_string)
        
        url = f"{self.base_url}{endpoint}?{query_string}&signature={signature}"
        headers = {'X-MBX-APIKEY': self.api_key}

        logger.info(f"Sending {method} request to {endpoint}")
        
        try:
            response = requests.request(method, url, headers=headers)
            response.raise_for_status() # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP Error: {err.response.status_code} - {err.response.text}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Network Failure: {str(e)}")
            raise