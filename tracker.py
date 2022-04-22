
import requests
import json
import copy

SUPPORT_COINS = {
    "weth":"weth",
    "near":"near",
    "brl" : "borealis"
}

class Tracker:
    def __init__(self, coins):
        url = ''
        for c in coins:
            url += SUPPORT_COINS[c] + '%2C'
        url = url[:-3]

        self.base_url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={url}'
        self.data = {}

        r = json.loads(requests.get(self.base_url).text)

        for i in r:
            self.data.update({i['symbol']:i['current_price']})

    def get_prices(self):
        save = copy.deepcopy(self.data)

        try:
            r = json.loads(requests.get(self.base_url).text)
            for i in r:
                self.data.update({i['symbol']:i['current_price']})
            return self.data
        except:
            return save