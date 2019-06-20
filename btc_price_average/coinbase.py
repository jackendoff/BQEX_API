#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:zhihoudeMoon
@file: coinbase.py
@time: 2019/01/03
"""
import requests
import json
class Coinbase:
    def __init__(self):
        self.url = "https://api.pro.coinbase.com"

    def get_trades(self):
        url = self.url + "/products/BTC-USD/trades"
        try:
            req = requests.get(url)
            data = json.loads(req.content.decode("utf-8"))
            return float(data[0]["price"])
        except Exception as error:
            print(error)
            return None
if __name__ == '__main__':
    bit = Coinbase()
    print(bit.get_trades())