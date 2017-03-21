#!/usr/bin/env python3

mydict = {}

fo = open('../python_data/revenue.txt')

#fo_read = fo.read()
for key in fo.readlines():
    print(key[0])
