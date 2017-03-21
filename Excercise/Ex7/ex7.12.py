#!/usr/bin/env python3

import pprint

outer_list = []
fh = open('../python_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    id, street, city, state, zip = line.split(':')
