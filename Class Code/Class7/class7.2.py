#!/usr/bin/env python3

#lambdas - a function written in one line

def bythird(mylist):
    return mylist[2]
#lambda mylist: mylist[2]   #this says the samething as the function 'bythird'

def bylastname(name):
    items = name.split()
    return items[1]
#lambda name: name.split()[1]

def addthese(x, y):
    return x + y
#lambda x,y: x + y










#In order to get to the inner structures you must go through the outer structure first
#In ordert to get to the inner structures you must loop through the outer structure first

x = { 'a': [], 'b': [1, 2, 3], 'c': [1,2] }

print(x['b'])   #prints [1, 2, 3]
print(len(x['b']))  #prints 3
print(x['c'][-1])   #prints 2

x['c'].append(3)
print(x['c'])

#
# ticker_close = {
# 'AAPL': [ 125.03, 126.10, 129.3, 128.5],
# 'GOOG': [ 125.03, 126.10, 129.3, 128.5],
# 'FB': [125.03, 126.10, 129.3, 128.5],
# }
#
# #HW5
# yearsumdict = {}
#
# for line in fh:
#     items = line.split()
#     year = items[0][0:4]
#     value = items[1]
#
#     if year not in yearsumdict:
#         yearsumdict[year] = []
#
#     yearsumdict[year] = yearsumdict[year] + value
