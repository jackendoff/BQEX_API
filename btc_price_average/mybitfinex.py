#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:zhihoudeMoon
@file: mybitfinex.py
@time: 2019/01/03
"""
import json
import requests
import datetime

class Bitfinex:
    def __init__(self):
        # 获取最新价格的url
        self.hist_url = "https://api.bitfinex.com/v2/ticker/{}"

    def get_hist(self):
        url = self.hist_url.format("tBTCUSD")
        url = url
        try:
            req = requests.get(url)
            data = json.loads(req.content.decode("utf-8"))
            return float(data[-4])
        except Exception as error:
            print(error)
            return None


if __name__ == '__main__':
    bit = Bitfinex()
    data = bit.get_hist()
    print(data)
