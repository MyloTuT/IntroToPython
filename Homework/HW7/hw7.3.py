#!/usr/bin/env python3
ticker_prices = {}

for lines in open('../python_data/stock_prices.csv').readlines()[1:]:
    ticker, date, opening, high, low, close, volume = lines.split(',')

    if ticker not in ticker_prices:
        ticker_prices[ticker] = []

    ticker_prices[ticker].append(float(close))

by_difference = lambda x: min(ticker_prices[x]) - max(ticker_prices[x])

for keys in sorted(ticker_prices, key=by_difference, reverse=False):
    close_max = max(ticker_prices[keys])
    close_min = min(ticker_prices[keys])
    difference = close_max - close_min
    print('{key}: {difference} difference ({close_max} - {close_min})'.format(key=keys,
                                                                              difference=round(difference, 2),
                                                                              close_max=round(close_max, 2),
                                                                              close_min=round(close_min, 2)))
