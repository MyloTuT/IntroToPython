#!/usr/bin/env python3
counter = 0
nineteen_twenty_eight = '1928'

t_file = open('../python_data/FF_abbreviated.txt')

for line in t_file:
    year = line[0:4]

    if year == nineteen_twenty_eight:
        print(line)
        counter += 1
print(counter)
t_file.close()
