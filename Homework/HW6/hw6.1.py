#!/usr/bin/env python3

stock_price_file = '../python_data/stock_prices.csv'        #assigning stock_prices.csv file to a variable
lines = open(stock_price_file).readlines()[1:]              #assigning stock_price_file to lines. Calling readlines on the file and access everything from line 1 to the end

def by_closelessopen(value):    #this function should subtract the open value from the close value and report the difference
    line = value.split(',')
    results = float(line[5]) - float(line[2])
    return results

for line in sorted(lines, key=by_closelessopen, reverse=True)[0:5]: #iterating over lines and sorting by 'by_closelessopen' and reversing the file
    line = line.rstrip()    #removing \n from line
    ticker, date, open, high, low, close, volume = line.split(',')  #splitting the lines on a ','
    print('{} ({}): {} ({}->{})'.format(ticker,     #printing the file
                                        date,
                                        (round(float(close)-float(open), 2)),
                                        open,
                                        close))
