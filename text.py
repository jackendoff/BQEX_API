import time
import random
import base64
import hashlib
import hmac
from urllib import parse


# from content_safe import AppKey,AppSecret

base_url = 'http://testexapi.bqopen.com/open/v1'
comment_params = {
    'Action':'pay',
    # 'AppKey':AppKey,
    'Timestamp':int(time.time())*1000,
    'Nonce':123456,
    'SignatureMethod':'HmacSHA256'
}

params = {
    'diallingCode':86,
    'phone':17630636381,
    'amount':1,
    'note':'note'
}

sort_params = {
    "Action" : "pay",
    "AppKey" : "AKIDcZVSyyl8O2nzsFrKNsyj5sD1eCfJlRCI",
    "Nonce" : 123456,
    "SignatureMethod" : "HmacSHA256",
    "Timestamp" : 1465185768,
    "amount": 1,
    "diallingCode": "86",
    "note": "note",
    "phone": "18180980860"
}

url_str = parse.urlencode(sort_params,'utf-8')
print(url_str)
url_str = parse.quote_plus('POST'+'/open/v1/pay/receipt/order'+'?'+url_str)
print(url_str)

AppSecret = 'ASIDZwO4MejWZK81boBTqEU6hy3Ad6D4JFHbRm4HjugGMoQe2a2HgcZ7CJJkxTy7DBjS'
url_str = 'POST%2Fopen%2Fv1%2Fpay%2Freceipt%2Forder%3FAction%3Dpay%26AppKey%AKIDcZVSyyl8O2nzsFrKNsyj5sD1eCfJlRCI%26Nonce%3D123456%26SignatureMethod%3DHmacSHA256%26Timestamp%3D1465185768000%26amount%3D1%26diallingCode%3D86%26note%3Dnote%26phone%3D18180980860'
print(url_str)
no_base64 = (hmac.new(AppSecret.encode("UTF-8"), url_str.encode("utf-8"), hashlib.sha256).hexdigest())
print(no_base64)
data = base64.b64encode(no_base64.encode())
print(data)
