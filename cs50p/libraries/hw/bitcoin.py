import requests
import json
import sys

while True:
    if len(sys.argv) == 2:
        try:
            num_bitcoin = float(sys.argv[1])
            break
        except ValueError:
            sys.exit("Cannot convert to float")
    else:
        sys.exit("Insufficient arguments")

try:
    bitcoin_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = bitcoin_data.json()
    price_usd = response["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("request Exception")

total_price = price_usd * num_bitcoin
print(f"${total_price:,.4f}")
