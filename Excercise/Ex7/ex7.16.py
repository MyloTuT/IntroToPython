#!/usr/bin/env python3

import pprint

outer_dict = {}
fh = open('../python_data/student_db.txt')

lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')
    inner_dict = {}
    inner_dict['street'] = street
    inner_dict['city'] = city
    inner_dict['state'] = state
    inner_dict['zip'] = zip
    outer_dict[id] = inner_dict

print(outer_dict['ak9']['state'])
