import time
from alpaca_trade_api.rest import REST, TimeFrame

# Alpaca Paper Trading API credentials
API_KEY = 'PK5FB0T7LNOW70YQ12XM'
API_SECRET = 'y8YfqQNf0EpXwVwzYFhvB3BPy8ZErCqQClBRLpe1'
BASE_URL = 'https://paper-api.alpaca.markets'

# Initialize the Alpaca API
api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Get our account information.
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

def buy_stock(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"Bought {qty} shares of {symbol}")

def sell_stock(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    print(f"Sold {qty} shares of {symbol}")

def display_positions():
    positions = api.list_positions()
    print("\nCurrent Positions:")
    for position in positions:
        latest_trade = api.get_latest_trade(position.symbol)
        current_price = latest_trade.price
        change = ((current_price - float(position.avg_entry_price)) / float(position.avg_entry_price)) * 100
        print(f"{position.qty} shares of {position.symbol} at ${current_price:.2f} each ({change:.2f}%)")

def main():
    while True:
        print("\nOptions Menu:")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. Display Positions")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter the stock symbol to buy: ")
            qty = int(input("Enter the quantity to buy: "))
            buy_stock(symbol, qty)
        elif choice == '2':
            symbol = input("Enter the stock symbol to sell: ")
            qty = int(input("Enter the quantity to sell: "))
            sell_stock(symbol, qty)
        elif choice == '3':
            while True:
                display_positions()
                time.sleep(5)
                exit_choice = input("Type 'exit' to stop displaying positions: ")
                if exit_choice.lower() == 'exit':
                    break
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()