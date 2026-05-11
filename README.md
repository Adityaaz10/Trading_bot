# 🚀 Binance Futures Testnet Trading Bot

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Binance](https://img.shields.io/badge/Binance-Testnet-F3BA2F?logo=binance&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight, secure, and robust Command-Line Interface (CLI) trading bot for the **Binance Futures Testnet**. Designed for developers and algorithmic traders, this bot allows you to easily execute `MARKET` and `LIMIT` orders using HMAC-SHA256 secured API requests.

---

## ✨ Key Features

- **CLI-Driven Execution:** Fast and easy order execution directly from your terminal.
- **USDT-M Futures Support:** Specifically tailored for the Binance Futures Testnet (`https://testnet.binancefuture.com`).
- **Secure Authentication:** Implements industry-standard HMAC-SHA256 cryptographic signatures for all API requests.
- **Strict Input Validation:** Pre-execution checks ensure valid symbols, positive quantities, proper order types, and limit pricing to prevent API errors.
- **Comprehensive Logging:** Dual-stream logging (console and `trading_bot.log`) keeps a permanent record of all API requests, responses, and errors.
- **Environment Management:** Uses `.env` files for secure handling of API keys and secrets.

---

## 📂 Project Structure

```text
├── bot/
│   ├── __init__.py
│   ├── client.py         # Handles API HTTP requests & HMAC signatures
│   ├── logging_config.py # Configures dual-stream logger (file & console)
│   ├── orders.py         # Manages the core order payload and execution logic
│   └── validators.py     # Ensures strict validation of CLI inputs
├── cli.py                # Main entry point / argument parser
├── requirements.txt      # Python dependencies (requests, python-dotenv)
└── trading_bot.log       # Auto-generated execution logs
