import requests
import json
import time
import hmac
import hashlib
import base64
from urllib import parse

from .content_safe import *


class BqexApi(object):
    def __init__(self,coin_name='usdt_trin'):
        self.secret_key = AppKey
        self.api_key = AppSecret
        self.uid = UID
        self.coin_name = coin_name


    # 获取所有市场的报价
    def all_market_price(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        url = API_BASE+'/polarisex/quote/public'
        data = requests.get(url, headers=headers)
        # print(data)
        if data.status_code != 200:
            data = self.all_market_price()
            return data
        data = data.content.decode()
        return data

    # 获取公共交易历史{"date":"1551153449689","price":137.84,"amount":638.75,"number"下单数量:4.634,"coinCode":3,"baseCurrencyId":4,"tid":"15511534496891280901281000396104","type":"buy","buyOrSellTrade":1}
    def trade_history(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'coins': self.coin_name,
            'limit': 50
        }
        # data_json = json.dumps(params)
        url = API_BASE+'/polarisex/quote/tradeHistory'
        data = requests.get(url, headers=headers, params=params)
        if data.status_code != 200:
            data = self.trade_history()
            return data
        data = data.content.decode()
        return data

    # 获取交易深度
    def trade_depth(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'coins': self.coin_name,
            'limit': 100
        }
        # data_json = json.dumps(params)
        url = API_BASE+'/polarisex/quote/tradeDeepin'
        data = requests.get(url, headers=headers, params=params)
        if data.status_code != 200:
            data = self.trade_depth()
            return data
        data = data.content.decode()
        return data

    # 获取k线数据
    def trade_kline(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'coins': self.coin_name,
            'type':1,
            'limit': 2000,
            'startTime': int(time.time() - 1) * 1000,
            'endTime': int(time.time()) * 1000

        }
        # data_json = json.dumps(params)
        url = API_BASE+'/polarisex/quote/tradeDeepin'
        data = requests.get(url, headers=headers, params=params)
        # print(data)
        if data.status_code != 200:
            data = self.trade_kline()
            return data
        data = data.content.decode()
        return data

    # 获取实时交易信息
    def trade_real(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        params = {
            'coins': self.coin_name
        }
        # data_json = json.dumps(params)
        url = API_BASE+'/polarisex/quote/realTime'
        data = requests.get(url, headers=headers, params=params)
        if data.status_code != 200:
            data = self.trade_real()
            return data
        data = data.content.decode()
        return data

    # 获取交易对信息
    def trade_pairs(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
        # data_json = json.dumps(params)
        url = API_BASE+'/polarisex/quote/public'
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
        # print(url_str)

        # url_str = parse.quote_plus(method.upper() + str(url) + '?' + url_str)
        # print(url_str)
        # no_base64 = (hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.md5).hexdigest())
        no_base64 = hashlib.md5(url_str.encode("utf-8")).hexdigest()
        # print(no_base64)
        # data = base64.b64encode((hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.sha256).hexdigest()).encode())
        return no_base64.upper()

    # 下买单 buy
    def order_buy(self,price,amount):
        path = '/authlib/order'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key': AppSecret
        }
        # sign = self.sign_in(method=method,url=path,params=params)
        # ['api_key', 'buy_or_sell', 'num', 'price', 'sign', 'source', 'symbol', 'type', 'uid']
        url_str = 'api_key=' + AppKey + '&buy_or_sell=1'+'&num='+str(amount)+'&price='+str(price)+'&source=1&symbol='+self.coin_name+'&type=1&uid='+str(UID)+'&secret_key=' + AppSecret
        # print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()

        # print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'api_key': AppKey,
            'buy_or_sell':1,
            'price':price,
            'num':amount,
            'source':1,
            'sign': sign,
            'symbol': self.coin_name,
            'type':1,
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

    # 挂卖单
    def order_sell(self,price,amount):
        path = '/authlib/order'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key': AppSecret
        }
        # sign = self.sign_in(method=method,url=path,params=params)
        # ['api_key', 'buy_or_sell', 'num', 'price', 'sign', 'source', 'symbol', 'type', 'uid']
        url_str = 'api_key=' + AppKey + '&buy_or_sell=2'+'&num='+str(amount)+'&price='+str(price)+'&source=1&symbol='+self.coin_name+'&type=1&uid='+str(UID)+'&secret_key=' + AppSecret
        # print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()

        # print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'api_key': AppKey,
            'buy_or_sell':2,
            'price':price,
            'num':amount,
            'source':1,
            'sign': sign,
            'symbol': self.coin_name,
            'type':1,
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


    # 撤单
    def cancel_order(self,order_no):
        path = '/authlib/cancelOrder'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key': AppSecret
        }
        # sign = self.sign_in(method=method,url=path,params=params)
        # ['api_key', 'buy_or_sell', 'num', 'price', 'sign', 'source', 'symbol', 'type', 'uid']
        url_str = 'api_key=' + AppKey +'&order_no='+str(order_no)+'&uid='+str(UID)+'&secret_key=' + AppSecret
        # print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()

        # print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'order_no':order_no,
            'api_key': AppKey,
            'sign': sign,
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
    def authlib_quote(self):
        path = '/authlib/quote'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key': AppSecret
        }
        # sign = self.sign_in(method=method,url=path,params=params)
        url_str = 'api_key=' + AppKey + '&symbol='+self.coin_name+'&uid=' + str(UID) + '&secret_key=' + AppSecret
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()

        # print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'api_key': AppKey,
            'sign': sign,
            'symbol':self.coin_name
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
        # sign = self.sign_in(method=method,url=path,params=params)
        url_str = 'api_key='+AppKey+'&uid='+str(UID)+'&secret_key='+AppSecret
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()

        # print(sign)
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
        # print(url)
        data = requests.post(url=url,data=params_data,headers=headers)
        # print(data)
        data = data.content.decode()
        return data

    # 获取未成交单
    def untrade_order(self):
        path = '/authlib/unTradeOrder'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key': AppSecret
        }
        # sign = self.sign_in(method=method,url=path,params=params)
        # ['api_key', 'buy_or_sell', 'num', 'price', 'sign', 'source', 'symbol', 'type', 'uid']
        url_str = 'api_key=' + AppKey + '&size=1000&symbol='+self.coin_name+'&uid='+str(UID)+'&secret_key=' + AppSecret
        # print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()

        # print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'size':1000,
            'api_key': AppKey,
            'sign': sign,
            'symbol': self.coin_name,
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

    # 交易单状态
    def order_status(self,order_no):
        path = '/authlib/orderStatus'
        method = 'get'
        params = {
            'api_key': AppKey,
            'uid': UID,
            'secret_key': AppSecret
        }
        # sign = self.sign_in(method=method,url=path,params=params)
        # ['api_key', 'buy_or_sell', 'num', 'price', 'sign', 'source', 'symbol', 'type', 'uid']
        url_str = 'api_key=' + AppKey +'&order_no='+order_no+'&uid='+str(UID)+'&secret_key=' + AppSecret
        # print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()

        # print(sign)
        # app_key = parse.urlencode(AppKey)
        # print(app_key)
        params_data = {
            'uid': UID,
            'api_key': AppKey,
            'order_no':order_no,
            'sign': sign,
            'symbol': 'usdt_eth',
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

    # 成交记录
    def trade_order(self):
        path = '/authlib/tradeOrder'
        url_str = 'api_key=' + AppKey +'&symbol=ada_eth'+'&uid=' + str(UID)+ '&secret_key=' + AppSecret
        # print(url_str)
        sign = hashlib.md5(url_str.encode("utf-8")).hexdigest().upper()
        params = {
            'uid': UID,
            'api_key': AppKey,
            'symbol':self.coin_name,
            'sign': sign
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
            # "Authorization": sign
        }
        url = API_BASE + path
        # print(url)
        data = requests.post(url=url, data=params, headers=headers)
        data = data.content.decode()
        return data

    # 获取所有交易对 right
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
        }
        url = API_BASE+path
        # print(url)
        data = requests.post(url=url,data=params,headers=headers)
        data = data.content.decode()
        return data

    # 获取所有币种 right
    def coin_coins(self):
        url = API_BASE+'/polarisex/coin/coins'
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
            # "Authorization": sign
        }
        data = requests.post(url,headers=headers)
        data = data.content.decode()
        return data


if __name__ == '__main__':
    bqex = BqexApi('usdt_trin')

    # 获取所有市场的报价
    # data = bqex.all_market_price()

    # 获取交易历史
    # data = bqex.trade_history()

    # 获取交易深度
    # data = bqex.trade_depth()

    # 获取k线数据 失败
    # data = bqex.trade_kline()

    # 获取实时交易信息
    # data = bqex.trade_real()

    # 获取交易对信息
    # data = bqex.trade_pairs()

    # 获取账号
    # data = bqex.get_auth()

    # 获取深度quote 没用
    # data = bqex.authlib_quote()

    # 下买单
    # data = bqex.order_buy(price=325,amount=1)

    # 下卖单{"attachment":"15511547188257080902781100334975","status":200,"message":null}
    #{"attachment":"15518362164932170908681107396772","status":200,"message":null}未撤单**
    data = bqex.order_sell(price=0.00463,amount=1000)

    # 撤单
    # data = bqex.cancel_order('15513434477835380908671107312315')

    # 获取未成交单
    # data = bqex.untrade_order()

    # 获取交易单状态{"attachment":{"tradeNum":0.0,"status":4},"status":200,"message":null}status:0未成交，1部分成交，2已成交，4已撤单，5部分撤单, 404无此单
    # data = bqex.order_status('15511547188257080902781100334975')
    # null = 0
    # data = eval(data)
    # data = data["attachment"]['USDT_TRIN']['last']
    print(data)
