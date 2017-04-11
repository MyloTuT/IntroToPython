#!/usr/bin/env python3

market_value = {}

fo = open('../python_data/F-F_Research_Data_Factors_daily.txt').readlines()[6:-2]

for line in fo:
    year = line[0:4]
    date, mkt_rf, smb, hml, rf = line.split()
    if year not in market_value:
        market_value[year] = 0.0
    market_value[year] = market_value[year] + float(mkt_rf)

length_dict = len(market_value)

while True:
    user_input = input('please enter number of results desired: ')
    high_low = input('select "highest" or "lowest" results: ')

    if user_input.isalpha():
        print('num results must be all digits')
        continue

    if high_low == "highest" or "lowest":
        True
    else:
        continue

    if length_dict < int(user_input):
        print('num results "{}" greater than max {}'.format(int(user_input), length_dict))
        continue
    break

if high_low == "highest":
    reverse_direction = True
else:
    reverse_direction = False

count = 1
for key in sorted(market_value, key=market_value.get, reverse=reverse_direction):

    if int(user_input) >= count:
        print('{}: {}'.format(key, round(market_value[key], 2)))
    count = count + 1
