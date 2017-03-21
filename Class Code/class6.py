#!/usr/bin/env python3
#
myl = ['1', '11', '10', '100', '20']

yy = sorted(myl, key=int)
print(yy)

mydict = {'1927': 3.9, '1928': 0.2}

skeys = sorted(mydict, key=mydict.get)
# print(skeys)



# The Way complex sorting works
# 1. We pass an interable (list, dict, etc) as arg to sorted()
# 2. We specify a 'sort function' with the key= parameter
# 3. sorted() sends each item as argument to the function
# 4. the value that comes back from the function is the value by which that item will be sorted

# Functions
def myfunc(x):
    x = x * 2
    return # XXX:

y = myfunc(5)
z = myfunc(10)
zz = myfunc(100)

# Steps to sorting
# 1. what is an item to be sorted?
# 2. what value would you like the item to be sorted by?
# 3. can you write a function that takes one item and returns the 'by' value

#
# value_table = [
#                 { 'date': '19260701', 'MktRF': 0.09, 'SMB': -0.22, 'HML': -0.30, 'RF': 0.009 },
#                 { 'date': '19260702', 'MktRF': 0.44, 'SMB': -0.35, 'HML': -0.08, 'RF': 0.009 },
#                 { 'date': '19260706', 'MktRF': 0.17, 'SMB': 0.26,  'HML': -0.37, 'RF': 0.009 }
#               ]
#
# for mydict in value_table:
#     print(mydict['MktRF'])
