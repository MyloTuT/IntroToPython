#!/usr/bin/python3

revenue = '../python_data/revenue.txt'

by_last_float = lambda line: float(line.split(',')[-1])

for line in sorted(open(revenue).readlines(), key=by_last_float):
    line = line.rstrip()
    print(line)
