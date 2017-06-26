#!/usr/bin/env python3
while True:
    user_input = input('please provide a year: ')

    if user_input.isdigit() and len(user_input) == 4:
        break
    else:
        print('ERROR: arg must be 4-digit year')
        continue


fo = open('/Users/mrayfield/git/IntroToPython/python_data/F-F_Research_Data_Factors_daily.txt')
market_value = []

fo_read = fo.readlines()[5:-1][0:-1]

for lines in fo_read:
    years = lines[0:4]
    if user_input == years:
        years, mkt_rf, smb, hml, rf = lines.split()
        mkt_rf_value = float(mkt_rf)
        market_value.append(mkt_rf_value)

if len(market_value) == 0:
    print('no values found')
    exit()

fo.close()
market_value_sum = sum(market_value)
market_value_average = (market_value_sum / len(market_value))
market_value_order = sorted(market_value)

print('{user_input} (Mkt-RF): {market_values} values, max {max_value}, min {min_value}, avg {average_value}'.format(user_input=user_input,
                                                                                                                    market_values=len(market_value),
                                                                                                                    max_value=max(market_value),
                                                                                                                    min_value=min(market_value),
                                                                                                                    average_value=market_value_average))
