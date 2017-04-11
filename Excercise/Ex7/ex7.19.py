#!/usr/bin/env python3
import pprint

outer_dict = {}
fh = open('../python_data/revenue.txt')
for line in fh:
    company, state, revenue = line.split(',')

    if state not in outer_dict:
        outer_dict[state] = 0.0
    outer_dict[state] = outer_dict[state] + float(revenue)

print(outer_dict)
print(outer_dict['NJ'])
