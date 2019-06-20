#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:zhihoudeMoon
@file: binance.py
@time: 2019/01/03
"""
import requests
import json
class Binance:
    def __init__(self):
        self.API_url = "https://api.binance.com"

    def get_trades(self):
        url = self.API_url + "/api/v1/trades"
        url = url + "?symbol=" + "BTCUSDT" + "&limit=" + "1"
        try:
            req = requests.get(url)
            data = json.loads(req.content.decode("utf-8"))
            return float(data[0]["price"])
        except Exception as error:
            print(error)
            return None
if __name__ == '__main__':
    bit = Binance()
    print(bit.get_trades())
