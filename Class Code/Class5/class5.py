#!/usr/bin/env python3

#dict indexes with keys

# x = {'acme': 1.3,
#      'beta': 0.7} #acme and beta are the key and the numbers are the values
#
# x['conway'] = 1.1   #setting key/values
# print(x)
# zz = x['conway']    #getting val from key
#
# key = x['acme'] + 1
# x['acme'] = key
# print(x['acme'])

# fh = open('../python_data/student_db.txt')
# mydict = {}
#
# for line in fh.readlines()[1:]:
#     items = line.split(':')
#     state = items[3]
#
#     mydict[state] = mydict[state] + 1
# print(mydict)


# print(x['beta'])    #0.7
# print(x['acme'])

# for line in x:
#     print(line, x[line])

# exit()

y = {'c': 1,
    'b': 55,
    'a': 0.9}

change = sorted(y, key=y.get, reverse=True)
print(change)
print(y.get('a'))
