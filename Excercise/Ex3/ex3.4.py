#!/usr/bin/env python3

t_file = open('../python_data/FF_abbreviated.txt')

for tr in t_file:
    year = tr[0:4]
    print(year)
    
t_file.close()
