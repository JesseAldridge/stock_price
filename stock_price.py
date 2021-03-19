import os, json
from datetime import datetime

import requests


class PriceProvider:
  def __init__(self):
    with open(os.path.expanduser(f'~/polygon_config.json')) as f:
      text = f.read()
    self.api_token = json.loads(text)['api_token']
    self.session = requests.Session()

  def pull_current_price(self, symbol):
    url = f'https://api.polygon.io/v1/last_quote/stocks/{symbol}?apiKey={self.api_token}'
    quote_dict = self.session.get(url).json()
    last_quote = quote_dict.get('last')
    if not last_quote:
      return None
    return (last_quote['bidprice'] + last_quote['askprice']) / 2

def test():
  provider = PriceProvider()
  print('price:', provider.pull_current_price('AAPL'))
  provider.session.close()

if __name__ == '__main__':
  test()
