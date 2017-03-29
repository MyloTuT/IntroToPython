#!/usr/bin/env python3

import pprint

outer_dict = {}
fh = open('../python_data/student_db.txt')

inner_dict = {}
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')
    inner_dict[id] = state

print(inner_dict['ak9'])
