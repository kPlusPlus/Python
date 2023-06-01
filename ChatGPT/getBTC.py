import requests

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    bitcoin_price = data["bitcoin"]["usd"]
    return bitcoin_price

def getBTC():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"
    response = requests.get(url)
    data = response.json()
    getBTC = data["bitcoin"]["eur"]
    return getBTC

# ETH
def get_ethereum_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    ethereum_price = data["ethereum"]["usd"]
    return ethereum_price

def getETH():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur"
    response = requests.get(url)
    data = response.json()
    ethereum_price = data["ethereum"]["eur"]
    return ethereum_price


eth_price = get_ethereum_price()
print("Cijena Ethereuma (ETH) u USD:", eth_price)

eth_cijena = getETH()
print("Cijena Ethereuma (ETH) u EUR:", eth_cijena)


btc_price = get_bitcoin_price()
print("Cijena Bitcoina (BTC) u EURO:", btc_price)

btc_cijena = getBTC()
print("Cijena Bitcoina (BTC) u EURO:", btc_cijena)
