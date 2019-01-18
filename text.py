# import time
# import random
# import base64
# import hashlib
# import hmac
# import requests
# from content_safe import *
# from urllib import parse
#
#
# # from content_safe import AppKey,AppSecret
#
# base_url = 'http://testexapi.bqopen.com/open/v1'
# comment_params = {
#     'Action':'pay',
#     # 'AppKey':AppKey,
#     'Timestamp':int(time.time())*1000,
#     'Nonce':123456,
#     'SignatureMethod':'HmacSHA256'
# }
#
# params = {
#     'diallingCode':86,
#     'phone':17630636381,
#     'amount':1,
#     'note':'note'
# }
#
# sort_params = {
#     "Action" : "pay",
#     "AppKey" : "AKIDcZVSyyl8O2nzsFrKNsyj5sD1eCfJlRCI",
#     "Nonce" : 123456,
#     "SignatureMethod" : "HmacSHA256",
#     "Timestamp" : 1465185768,
#     "amount": 1,
#     "diallingCode": "86",
#     "phone": "17630636381"
# }
# # https://api.bqex.pro/open/v1/pay/receipt/order
# url_str = parse.urlencode(sort_params,'utf-8')
# print(url_str)
# url_str = parse.quote_plus('GET'+'/accound/vcode'+'?'+url_str)
# print(url_str)
#
# # AppSecret = 'ASIDZwO4MejWZK81boBTqEU6hy3Ad6D4JFHbRm4HjugGMoQe2a2HgcZ7CJJkxTy7DBjS'
# # url_str = 'POST%2Fopen%2Fv1%2Fpay%2Freceipt%2Forder%3FAction%3Dpay%26AppKey%AKIDcZVSyyl8O2nzsFrKNsyj5sD1eCfJlRCI%26Nonce%3D123456%26SignatureMethod%3DHmacSHA256%26Timestamp%3D1465185768000%26amount%3D1%26diallingCode%3D86%26note%3Dnote%26phone%3D18180980860'
# print(url_str)
# no_base64 = (hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.sha256).hexdigest())
# print(no_base64)
# sign = base64.b64encode(no_base64.encode())
# print(sign)
# url = 'https://api.bqex.pro/open/v1/accound/vcode'+'?'+parse.urlencode(sort_params)
# print(url)
# headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#             "Cookie": "Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036",
#             "Authorization": sign
#         }
# data = requests.get(url=url,headers=headers,params=sort_params)
# data = data.content.decode()
# print(data)
#
#
# # def sign_in(self, method, url, params):
# #     # url_str = parse.urlencode(params, 'utf-8')
# #     url_str = 'api_key=' + AppKey + '&uid=' + str(UID) + '&secret_key=' + AppSecret
# #     print(url_str)
# #
# #     # url_str = parse.quote_plus(method.upper() + str(url) + '?' + url_str)
# #     # print(url_str)
# #     # no_base64 = (hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.md5).hexdigest())
# #     no_base64 = hashlib.md5(url_str.encode("utf-8")).hexdigest()
# #     print(no_base64)
# #     # data = base64.b64encode((hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.sha256).hexdigest()).encode())
# #     return no_base64.upper()

params_data = {
            'uid': 1,
            'api_key': 2,
            'buy_or_sell':1,
            'price':3,
            'num':4,
            'source':'web',
            'sign': 6,
            'symbol': 'usdt_eth',
            'type':1,
        }

sort_dict = sorted(params_data.keys())

print(sort_dict)