import yfinance as yf
from datetime import datetime, time
import time as tm

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data['Close'].iloc[-1]

def get_btc_price():
    btc = yf.Ticker("BTC-USD")
    data = btc.history(period="1d")
    return data['Close'].iloc[-1]

def is_market_open():
    now = datetime.now()
    market_open = time(9, 30)
    market_close = time(16, 0)
    return now.time() >= market_open and now.time() <= market_close

def main():
    tesla_ticker = "TSLA"
    siemens_ticker = "SIEGY"

    reference_price_btc = float(input("Bitte geben Sie den Referenzpreis für BTC ein: "))
    reference_price_tesla = float(input("Bitte geben Sie den Referenzpreis für Tesla ein: "))
    reference_price_siemens = float(input("Bitte geben Sie den Referenzpreis für Siemens ein: "))

    while True:
        tesla_price = get_stock_info(tesla_ticker)
        siemens_price = get_stock_info(siemens_ticker)
        btc_price = get_btc_price()

        tesla_exchange = "Dow Jones"
        siemens_exchange = "DAX"

        btc_percentage_change = ((btc_price - reference_price_btc) / reference_price_btc) * 100
        tesla_percentage_change = ((tesla_price - reference_price_tesla) / reference_price_tesla) * 100
        siemens_percentage_change = ((siemens_price - reference_price_siemens) / reference_price_siemens) * 100

        def format_percentage_change(percentage):
            if percentage > 0:
                return f"\033[92m{percentage:.2f}%\033[0m"  # Green for positive
            else:
                return f"\033[91m{percentage:.2f}%\033[0m"  # Red for negative

        if is_market_open():
            print(f"\033[97mTesla ({tesla_exchange}): {tesla_price:.2f} ({format_percentage_change(tesla_percentage_change)})\033[0m")
            print(f"\033[97mSiemens ({siemens_exchange}): {siemens_price:.2f} ({format_percentage_change(siemens_percentage_change)})\033[0m")
        else:
            print(f"\033[91mTesla ({tesla_exchange}): {tesla_price:.2f} ({format_percentage_change(tesla_percentage_change)})\033[0m")
            print(f"\033[91mSiemens ({siemens_exchange}): {siemens_price:.2f} ({format_percentage_change(siemens_percentage_change)})\033[0m")

        print(f"Bitcoin (BTC-USD): {btc_price:.2f} ({format_percentage_change(btc_percentage_change)})")

        tm.sleep(5)

if __name__ == "__main__":
    main()


##Enviroment erstellen
##python3 -m venv .venv
##source .venv/bin/activate
##pip install yfinance
##python stocks.py