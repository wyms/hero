import requests

def get_stock_price(stock_symbol):
    api_key = 'pk_67c74fd41add40beb5c71e4f785877ee'  # Replace with your API key
    url = f'https://cloud.iexapis.com/stable/stock/{stock_symbol}/quote?token={api_key}'
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol: ")
    print(get_stock_price(stock_symbol))