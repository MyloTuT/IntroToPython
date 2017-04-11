#!/usr/bin/env python3

student_ids = [ id.split(':')[0] for id in open('../python_data/student_db.txt').readlines()[1:]  ]
print(student_ids)
