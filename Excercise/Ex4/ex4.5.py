#!/usr/bin/env python3

var_key = []

fo = open("../python_data/student_db.txt")

for line in fo:
    breakdown = line.split(':')
    var_states.append(breakdown[3])
    var_key.append(breakdown[0])

    if var_state == 'NY':
        print(var_key)
fo.close()
