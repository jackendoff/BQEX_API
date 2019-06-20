from .binance import Binance
from .coinbase import Coinbase
from .mybitfinex import Bitfinex


def get_average_price():
    sum_btc_usdt_list = []
    bitfinex = Bitfinex()
    Bitfinex_data = bitfinex.get_hist()
    if Bitfinex_data is not None:
        sum_btc_usdt_list.append(Bitfinex_data)

    coinbase = Coinbase()
    Coinbase_data = coinbase.get_trades()
    if Coinbase_data is not None:
        sum_btc_usdt_list.append(Coinbase_data)

    binance = Binance()
    Binance_data = binance.get_trades()
    if Binance_data is not None:
        sum_btc_usdt_list.append(Binance_data)
    nsum = 0
    for i in range(len(sum_btc_usdt_list)):
        nsum += sum_btc_usdt_list[i]
    averrage_data = nsum/len(sum_btc_usdt_list)
    print(sum_btc_usdt_list)
    return averrage_data


if __name__ == '__main__':
    data = get_average_price()
    print(data)

