#!/usr/bin/env python3

counter = 0
t_file = open('../python_data/FF_abbreviated.txt')

for line in t_file:
    year = line[0:4]

    if year == '1928':
        lines = line.split()
        ymd = lines[1]
        counter += 1
        convert_ymd = float(ymd)
        double_ymd = convert_ymd * 2
        print(counter, convert_ymd, double_ymd)

t_file.close()
