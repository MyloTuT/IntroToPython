#!/usr/bin/env python3

t_file = open('../python_data/FF_abbreviated.txt')

for line in t_file:
    year = line[0:4]

    if year == '1928':
        lines = line.split()
        ymd = lines[1]
        print(ymd)

t_file.close()
