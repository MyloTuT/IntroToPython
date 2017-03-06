#!/usr/bin/env python3
market_value = []

fo = open('../python_data/F-F_Research_Data_Factors_daily.txt')

while True:
    user_input = input('please provide a year: ')

    if user_input.isdigit() and len(user_input) == 4:
        break
    else:
        print('ERROR: arg must be 4-digit year')
        continue

for lines in fo:
    years = lines[0:4]
    market_value_column= lines[11:16]

    if user_input == years:
        market_value.append(float(market_value_column))

fo.close()
market_value_sum = sum(market_value)
market_value_average = (market_value_sum / len(market_value))
market_value_order = sorted(market_value)

print('"{user_input}" (Mkt-RF): "{market_values}" values, max "{max_value}", min "{min_value}", avg "{average_value}"'.format(user_input=user_input, market_values=len(market_value), max_value=max(market_value), min_value=min(market_value), average_value=market_value_average))

#find the mean Extra credit
# x = [1, 3, 5, 6, 7, 12.5, 15]
#
# yy = sorted(x)
# yy_length = len(yy)
# print(yy_length)
# xx_divide = yy_length / 2
#
# xx = [xx_divide]
# print(xx)
# market_value_median = market_value_order[len(market_value) / 2]
#
