from .bqex_api import BqexApi


# 获取trin_usdt买单和卖单
def get_trin_usdt_order():
    bqex = BqexApi('usdt_trin')
    null = 'null'
    data = eval(bqex.trade_depth())
    all_asks = data['attachment']['asks']
    all_bids = data['attachment']['bids']
    return all_asks,all_bids


# 获取trin_btc买单和卖单
def get_trin_btc_order():
    bqex = BqexApi('btc_trin')
    null = 'null'
    data = eval(bqex.trade_depth())
    all_asks = data['attachment']['asks']
    all_bids = data['attachment']['bids']
    return all_asks,all_bids


# 获取trin_usdt自己的买单和卖单
def get_self_trin_usdt_order():
    bqex = BqexApi('usdt_trin')
    null = 'null'
    data = eval(bqex.untrade_order())
    data = data['attachment']
    self_trin_usdt_buy_order = [[float(i['price']),float(i['remainNum'])] for i in data if i['buyOrSell']==1]
    self_trin_usdt_sell_order = [[float(i['price']),float(i['remainNum'])] for i in data if i['buyOrSell']==2]
    return self_trin_usdt_sell_order,self_trin_usdt_buy_order


# 获取trin_btc自己的买单和卖单
def get_self_trin_btc_order():
    bqex = BqexApi('btc_trin')
    null = 'null'
    data = eval(bqex.untrade_order())
    data = data['attachment']
    self_trin_btc_buy_order = [[float(i['price']), float(i['remainNum'])] for i in data if i['buyOrSell'] == 1]
    self_trin_btc_sell_order = [[float(i['price']), float(i['remainNum'])] for i in data if i['buyOrSell'] == 2]
    return self_trin_btc_sell_order,self_trin_btc_buy_order


# 获取trin_usdt，订单薄，场外数量，总数量
def get_self_trin_usdt_entrust():
    # 获取trin_usdt
    trin_usdt_orders_asks,trin_usdt_orders_bids = get_trin_usdt_order()
    self_trin_usdt_sell_order, self_trin_usdt_buy_order = get_self_trin_usdt_order()

    # 计算trin_usdt卖单
    print('trin_usdt总卖单:',trin_usdt_orders_asks)
    print('trin_usdt自己卖单',self_trin_usdt_sell_order)
    [i.extend([i[1],0]) for i in trin_usdt_orders_asks]
    for i in self_trin_usdt_sell_order:
        for j in trin_usdt_orders_asks:
            if float(i[0])==float(j[0]):
                j[2] = float(j[2])-float(i[1])
                j[3] = float(j[3])+float(i[1])
                break
    print('trin_usdt格式化卖单信息',trin_usdt_orders_asks[::-1])

    # 计算trin_usdt买单
    print('trin_usdt总买单:', trin_usdt_orders_bids)
    print('trin_usdt自己买单', self_trin_usdt_buy_order)
    [i.extend([i[1], 0]) for i in trin_usdt_orders_bids]
    for i in self_trin_usdt_buy_order:
        for j in trin_usdt_orders_bids:
            if float(i[0]) == float(j[0]):
                j[2] = float(j[2]) - float(i[1])
                j[3] = float(j[3]) + float(i[1])
                break
    print('trin_usdt格式化买单信息',trin_usdt_orders_bids)

    return [trin_usdt_orders_asks[::-1],trin_usdt_orders_bids]


# 获取trin_btc，订单薄，场外数量，总数量
def get_self_trin_btc_entrust():
    # 获取trin_usdt
    trin_btc_orders_asks,trin_btc_orders_bids = get_trin_btc_order()
    self_trin_btc_sell_order, self_trin_btc_buy_order = get_self_trin_btc_order()

    # 计算trin_usdt卖单
    print('trin_btc总卖单:',trin_btc_orders_asks)
    print('trin_btc自己卖单',self_trin_btc_sell_order)
    [i.extend([i[1],0]) for i in trin_btc_orders_asks]
    for i in self_trin_btc_sell_order:
        for j in trin_btc_orders_asks:
            if float(i[0])==float(j[0]):
                j[2] = float(j[2])-float(i[1])
                j[3] = float(j[3])+float(i[1])
                break
    print('trin_btc格式化卖单信息',trin_btc_orders_asks[::-1])

    # 计算trin_usdt买单
    print('trin_btc总买单:', trin_btc_orders_bids)
    print('trin_btc自己买单', self_trin_btc_buy_order)
    [i.extend([i[1], 0]) for i in trin_btc_orders_bids]
    for i in self_trin_btc_buy_order:
        for j in trin_btc_orders_bids:
            if float(i[0]) == float(j[0]):
                j[2] = float(j[2]) - float(i[1])
                j[3] = float(j[3]) + float(i[1])
                break
    print('trin_btc格式化买单信息',trin_btc_orders_bids)

    return [trin_btc_orders_asks[::-1],trin_btc_orders_bids]


if __name__ == '__main__':
    data = get_self_trin_usdt_entrust()
    data_btc = get_self_trin_btc_entrust()
    # print(data,type(data))