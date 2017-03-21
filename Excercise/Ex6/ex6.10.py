#!/usr/bin/env python3

def by_num_value(value):
    lines_split = value.split(',')
    return float(lines_split[-1])

fo = open('../python_data/revenue.txt').readlines()

for line in sorted(fo, key=by_num_value):
    print(line.rstrip())
