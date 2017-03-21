#!/usr/bin/env python3

market_value = {}

for line in open('../python_data/F-F_Research_Data_Factors_daily.txt'):
    split_line = line.split()
    years = split_line[0][0:4]
    mkt_line = split_line[1]#[0][11:16]
    if years not in market_value:
        market_value[years] = []
    market_value[years] = market_value[years] + mkt_line
print(market_value[years])
