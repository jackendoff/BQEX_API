import requests
import json
import time
import hmac
import hashlib
import base64
from urllib import parse

from content_safe import *


class BqexApi(object):
    def __init__(self):
        self.secret_key = AppKey
        self.api_key = AppSecret
        self.uid = UID


    # 获取所有市场的报价
    def all_market_price(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        url = 'https://www.bqex.pro/polarisex/quote/public'
        data = requests.get(url, headers=headers)
        if data.status_code != 200:
            data = self.all_market_price()
            return data
        data = data.content.decode()
        return data

    # 获取公共交易历史
    def trade_history(self,coin_name):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'coins': coin_name,
            'limit': 50
        }
        # data_json = json.dumps(params)
        url = 'https://www.bqex.pro/polarisex/quote/tradeHistory'
        data = requests.get(url, headers=headers, params=params)
        if data.status_code != 200:
            data = self.trade_history(coin_name)
            return data
        data = data.content.decode()
        return data

    # 获取交易深度
    def trade_depth(self,coin_name):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'coins': coin_name,
            'limit': 50
        }
        # data_json = json.dumps(params)
        url = 'https://www.bqex.pro/polarisex/quote/tradeDeepin'
        data = requests.get(url, headers=headers, params=params)
        if data.status_code != 200:
            data = self.trade_depth(coin_name)
            return data
        data = data.content.decode()
        return data

    # 获取k线数据
    def trade_kline(self,coin_name):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'symbol': coin_name,
            'type':1,
            'limit': 2000,
            'startTime': int(time.time() - 1) * 1000,
            'endTime': int(time.time()) * 1000

        }
        # data_json = json.dumps(params)
        url = 'https://www.bqex.pro/polarisex/quote/tradeDeepin'
        data = requests.get(url, headers=headers, params=params)
        if data.status_code != 200:
            data = self.trade_kline(coin_name)
            return data
        data = data.content.decode()
        return data

    # 获取实时交易信息
    def trade_real(self,coin_name):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'coins': coin_name
        }
        # data_json = json.dumps(params)
        url = 'https://www.bqex.pro/polarisex/quote/realTime'
        data = requests.get(url, headers=headers, params=params)
        if data.status_code != 200:
            data = self.trade_real(coin_name)
            return data
        data = data.content.decode()
        return data

    # 获取交易对信息
    def trade_pairs(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        # data_json = json.dumps(params)
        url = 'https://www.bqex.pro/polarisex/quote/public'
        data = requests.get(url, headers=headers)
        # print(data.status_code,type(data.status_code))
        if data.status_code != 200:
            data = self.trade_pairs()
            return data
        data = data.content.decode()
        return data


    # 获取签名,请求方式，排序参数
    def sign_in(self,method,url,params):
        url_str = parse.urlencode(params, 'utf-8')
        url_str = parse.quote_plus(method.upper() + str(url) + '?' + url_str)
        no_base64 = (hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.sha256).hexdigest())
        data = base64.b64encode(no_base64.encode())

        return data

    # 下单
    # 撤单
    # 获取深度
    def auth_deepin(self):
        url = 'https://www.bqex.pro/polarisex/authlib/deepin'
        secret = 'GET/authlib/deepin?Action=pay&AppKey='+self.api_key +'&secret_key=' + self.secret_key+'&symbol=ethltc'+'&uid=' + self.uid
        sign = self.sign_in(secret)
        params = {
            'uid': self.uid,
            'api_key': self.api_key,
            'sign': sign,
            'symbol':'ethltc'
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}

        data = requests.get(url, params=params, headers=headers)
        data = data.content.decode()
        return data
    # 获取深度

    # 获取账号
    def get_auth(self):
        pass
    # 获取未成交单
    # 交易单成状态
    # 成交记录
    # 获取所有交易对
    # 获取所有币种


if __name__ == '__main__':
    bqex = BqexApi()
    # 获取所有市场的报价
    # data = bqex.all_market_price()

    # 获取交易历史
    # data = bqex.trade_history("usdt_btc")

    # 获取交易深度
    # data = bqex.trade_depth('usdt_btc')

    # 获取k线数据
    # data = bqex.trade_depth('usdt_btc')

    # 获取实时交易信息
    # data = bqex.trade_real('usdt_btc')

    # 获取交易对信息
    data = bqex.get_auth()

    print(data)