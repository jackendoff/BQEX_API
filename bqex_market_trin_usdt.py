from bqex_api import BqexApi
from content_safe import *
import sys
import threading
import numpy as np
import time
import random


class BqexMarket(object):

    def __init__(self,start_price):
        self.Bqex = BqexApi('usdt_trin')
        # 初始价格
        self.start_price = start_price
        # 上一分钟时间
        self.old_time_data_min = 0
        # 下一分钟内中心价
        self.next_center_price = 0
        # 分钟内价格震荡列表
        self.price_list = []
        # 分钟内价格列表索引
        self.price_list_index = 0

    def get_next_start_price(self):
        print('重新计算分钟内中心价格')
        x0 = float(np.random.normal(0, 0.005, 1))
        x0 = max(min(0.005,x0),-0.005)
        self.start_price = round(float(self.start_price)*(1+x0),5)
        return self.start_price

    def get_asks_bids(self):
        null = 0
        data = eval(self.Bqex.trade_depth())
        try:
            asks_one = data['attachment']['asks'][0]
            bids_one = data['attachment']['bids'][0]
        except Exception as err:
            print(err)
            self.get_asks_bids()
        print('买一卖一：', [asks_one[0], bids_one[0]])
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
            self.price_list = []
            self.old_time_data_min = new_time_data_min
            for i in range(10):
                price = round(random.uniform(-0.00003,0.00003),5)
                self.price_list.append(price)
        if self.start_price >= asks_one_price:
            self.start_price = asks_one_price-0.00001
        if self.start_price <= bids_one_price:
            self.start_price = bids_one_price + 0.00001
        next_price = self.start_price+self.price_list[self.price_list_index]
        next_price = min(max(bids_one_price+0.00001,next_price),asks_one_price-0.00001)
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
        print('一分钟中心价：',self.start_price,time.localtime(time.time()))
        print('分钟内列表：',self.price_list,self.price_list[self.price_list_index-1])
        #　下单
        amount = random.randint(1000,10000)
        print('下单价格:',price,amount)

        buy = threading.Thread(target=self.buy_order,args=(price,amount,))
        sell = threading.Thread(target=self.sell_order,args=(price,amount,))
        buy.start()
        sell.start()
        buy.join()
        sell.join()
        # 撤单
        time_sleep = random.randint(5,10)
        bilian = threading.Timer(time_sleep,self.run_threading,)
        bilian.start()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        input_price = input('请输入初始价格_trin_usdt：')
    elif len(sys.argv) == 2:
        input_price = sys.argv[1]
    market = BqexMarket(input_price)
    market.run_threading()





