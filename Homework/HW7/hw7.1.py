#!/usr/bin/env python3

import pprint

stock_price_file = '../python_data/stock_prices.csv'
lines = open(stock_price_file).readlines()[1:]

by_closelessopen = lambda line: float(line.split(',')[5]) - float(line.split(',')[2])

for line in sorted(lines, key=by_closelessopen , reverse=True)[0:5]:
    line = line.rstrip()
    ticker, date, open, high, low, close, volume = line.split(',')
    print('{} ({}): {} ({}->{})'.format(ticker,
                                        date,
                                        (round(float(close)-float(open), 2)),
                                        open,
                                        close))
