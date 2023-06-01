import requests

def get_crypto_list():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    data = response.json()
    crypto_list = [crypto["id"] for crypto in data]
    return crypto_list

crypto_list = get_crypto_list()
print("Popis kriptovaluta:")
for crypto in crypto_list:
    print(crypto)
