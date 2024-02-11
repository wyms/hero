import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

def get_stock_price(stock_symbol):
    api_key = os.getenv('IEX_API_KEY')  # Get API key from environment variable
    url = f'https://cloud.iexapis.com/stable/stock/{stock_symbol}/quote?token={api_key}'
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol: ")
    print(get_stock_price(stock_symbol))