import sys
import requests
import json

"""
read documentation from here 
https://requests.readthedocs.io/en/latest/
"""

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

while True:
    try:
        n = float(sys.argv[1])
        break
    except ValueError:
        sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # print(json.dumps(response.json(), indent = 2))
    price = []
    bitcoin_price = response.json()
    usd = bitcoin_price["bpi"].keys()
    for valuta in bitcoin_price["bpi"].keys():
        if valuta == "USD":
            for value in bitcoin_price["bpi"][valuta].values():
                price.append(value)

            price = price[-1]
            tot = price * n
            print(f"${tot:,.4f}")

except requests.RequestException:
    sys.exit("Error http")
