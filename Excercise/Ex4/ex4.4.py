#!/usr/bin/env python3

var = []

fo = open("../python_data/student_db.txt")

for line in fo:
    breakdown = line.split(':')
    var.append(breakdown[3])

states = var

print(states[1:])

fo.close()
