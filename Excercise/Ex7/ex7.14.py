#!/usr/bin/env python3

import pprint

outer_list = []
fh = open('../python_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')
    inner_dict = {'id': id, 'city': city, 'state': state }
    outer_list.append(inner_dict)

print(outer_list[3]['city'])
