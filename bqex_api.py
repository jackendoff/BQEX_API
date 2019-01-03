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
        # url_str = parse.urlencode(params, 'utf-8')
        url_str = 'api_key='+AppKey+'&uid='+str(UID)+'&secret_key='+AppSecret
        print(url_str)

        # url_str = parse.quote_plus(method.upper() + str(url) + '?' + url_str)
        # print(url_str)
        # no_base64 = (hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.md5).hexdigest())
        no_base64 = hashlib.md5(url_str.encode("utf-8")).hexdigest()
        print(no_base64)
        # data = base64.b64encode((hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.sha256).hexdigest()).encode())
        return no_base64.upper()

    # 下单
    def order(self):
        pass
    # 撤单

    # 获取深度
    def authlib_deepin(self):
        path = '/authlib/account'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key': AppSecret,
            'symbol': 'eth_ltc',

        }
        # sign = self.sign_in(method=method, url=path, params=params)
        url_str = 'api_key=' + AppKey + '&uid=' + str(UID) + '&symbol=eth_ltc&secret_key=' + AppSecret
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest()

        # print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'api_key': AppKey,
            'sign': sign,
            'symbol': 'eth_ltc',

        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
            "Authorization": sign
        }

        # url = API_BASE+path+'?'+parse.urlencode(params_data)
        # url = API_BASE+path+'?'+'api_key='+AppKey+'&uid='+str(UID)+'&sign='+sign
        url = API_BASE + path
        # print(url)
        data = requests.post(url=url, data=params_data, headers=headers)
        # print(data)
        data = data.content.decode()
        return data


    # 获取深度

    # 获取账号
    def get_auth(self):
        path = '/authlib/account'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key':AppSecret
        }
        sign = self.sign_in(method=method,url=path,params=params)
        print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'api_key':AppKey,
            'sign':sign,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
            "Authorization": sign
        }

        # url = API_BASE+path+'?'+parse.urlencode(params_data)
        # url = API_BASE+path+'?'+'api_key='+AppKey+'&uid='+str(UID)+'&sign='+sign
        url = API_BASE+path
        print(url)
        data = requests.post(url=url,data=params_data,headers=headers)
        print(data)
        data = data.content.decode()
        return data
    # 获取未成交单
    # 交易单成状态

    # 成交记录
    def trade_order(self):
        path = '/authlib/tradeOrder'
        url_str = 'api_key='+AppKey+'&uid='+str(UID)+'&symbol=eth_ltc&secret_key='+AppSecret
        print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()
        params = {
            'uid': UID,
            'api_key': AppKey,
            'sign': sign,
            'symbol':'FCC'
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
            "Authorization": sign
        }
        url = API_BASE+path
        data = requests.post(url=url,data=params,headers=headers)
        data = data.content.decode()
        return data


    # 获取所有交易对
    def authlib_pairs(self):
        path = '/authlib/pairs'
        url_str = 'api_key='+AppKey+'&uid='+str(UID)+'&secret_key='+AppSecret
        # print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()
        params = {
            'uid':UID,
            'api_key':AppKey,
            'sign':sign
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
            # "Authorization": sign
        }
        url = API_BASE+path
        print(url)
        data = requests.post(url=url,data=params,headers=headers)
        data = data.content.decode()
        return data

    # 获取所有币种
    def coin_coins(self):
        url = 'https://www.bqex.pro/polarisex/coin/coins'
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
            # "Authorization": sign
        }
        data = requests.post(url,headers=headers)
        data = data.content.decode()
        return data


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