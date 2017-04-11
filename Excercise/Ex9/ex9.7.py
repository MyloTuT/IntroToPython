#!/usr/bin/env python3

def getLines(filename):
    file_name = open(filename)

    file_list = []
    for lines in file_name.readlines():
        file_list.append(lines)
    return file_list

lines = getLines('../python_data/student_db.txt')

for line in lines:
    print(line)
