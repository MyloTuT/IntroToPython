#!/usr/bin/env python3

t_file = open('../python_data/FF_abbreviated.txt')
nineteen_twenty_eight = '1928'

for tr in t_file:
    year = tr[0:4]

    if year == nineteen_twenty_eight:
        print(tr)

t_file.close()
