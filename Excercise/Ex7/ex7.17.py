#!/usr/bin/env python3

import pprint

outer_dict = {}
fh = open('../python_data/student_db.txt')

lines = fh.readlines()[1:]

state_count = dict()
for line in lines:
    id, street, city, state, zip = line.split(':')
    if state not in state_count:
        state_count[state] = 0
    state_count[state] = state_count[state] + 1

print(state_count['NY'])
