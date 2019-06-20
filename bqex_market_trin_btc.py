from bqex_api import BqexApi
from content_safe import *
import sys
import threading
import numpy as np
import time
import random

from btc_price_average.btc_usdt_average import get_average_price


class BqexMarket(object):

    def __init__(self):
        self.Bqex = BqexApi('btc_trin')
        # 初始价格
        self.start_price = 0
        # 上一分钟时间
        self.old_time_data_min = 0
        # 下一分钟内中心价
        self.next_center_price = 0
        # 分钟内价格震荡列表
        self.price_list = []
        # 分钟内价格列表索引
        self.price_list_index = 0

        self.trin_usdt_price = 0

    def get_next_start_price(self):
        print('==========重新计算分钟内中心价格',time.localtime(time.time()))
        x0 = float(np.random.normal(0, 0.014, 1))
        x0 = max(min(0.014,x0),-0.014)
        try:
            btc_average_price = get_average_price()
        except Exception as err:
            print(err)
            btc_average_price = 3808.00
        print('btc平均价格：',btc_average_price)
        data = self.Bqex.all_market_price()
        null = 0
        data = eval(data)
        try:
            self.trin_usdt_price = data["attachment"]['USDT_TRIN']['last']
        except Exception as err:
            print(err)
            self.get_next_start_price()
        print('trin_usdt最新价格：',self.trin_usdt_price)
        self.start_price = round(float(self.trin_usdt_price)/btc_average_price,8)

        # self.start_price = round(float(0.00000092),8)
        return self.start_price

    def get_asks_bids(self):
        null = 0
        data = eval(self.Bqex.trade_depth())
        asks_one = data['attachment']['asks'][0]
        bids_one = data['attachment']['bids'][0]
        print('买一卖一：',[asks_one[0],bids_one[0]])
        return [asks_one,bids_one]

    def get_next_price(self):
        asks_one,bids_one = self.get_asks_bids()
        asks_one_price = float(asks_one[0])
        bids_one_price = float(bids_one[0])

        time_data = time.localtime(time.time())
        new_time_data_min = time_data.tm_min
        if new_time_data_min != self.old_time_data_min:
            self.get_next_start_price()
            self.price_list_index = 0
            self.price_list = [0]
            self.old_time_data_min = new_time_data_min
            for i in range(10):
                price = round(random.uniform(-0.00000002,0.00000002),8)
                self.price_list.append(price)
        if self.start_price >= asks_one_price:
            self.start_price = asks_one_price-0.00000001
        if self.start_price <= bids_one_price:
            self.start_price = bids_one_price + 0.00000001
        next_price = self.start_price+self.price_list[self.price_list_index]
        next_price = round(min(max(bids_one_price+0.00000001,next_price),asks_one_price-0.00000001),8)
        if self.price_list_index >= 8:
            self.price_list_index = 0
        self.price_list_index += 1
        return next_price

    def buy_order(self,price,amount):
        buy_id = self.Bqex.order_buy(price, amount)
        time.sleep(2)
        self.Bqex.cancel_order(buy_id)

    def sell_order(self,price,amount):
        sell_id = self.Bqex.order_sell(price,amount)
        time.sleep(2)
        self.Bqex.cancel_order(sell_id)

    def run_threading(self):
        price = self.get_next_price()
        print('一分钟中心价：',self.start_price)
        print('分钟内列表：',self.price_list,self.price_list[self.price_list_index-1])
        amount = random.randint(1000,10000)
        print('下单价格:',price,amount)
        #　下单
        buy = threading.Thread(target=self.buy_order,args=(price,amount,))
        sell = threading.Thread(target=self.sell_order,args=(price,amount,))
        buy.start()
        sell.start()
        buy.join()
        sell.join()
        # 撤单
        time_sleep = random.randint(6,10)
        bilian = threading.Timer(time_sleep,self.run_threading,)
        bilian.start()


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     input_price = input('请输入初始价格_trin_btc：')
    # elif len(sys.argv) == 2:
    #     input_price = sys.argv[1]
    market = BqexMarket()
    market.run_threading()





