#!/usr/bin/env python3

line_list = [
'the value on this line is 3',
'the value on this line is 1',
'the value on this line is 4',
'the value on this line is 2',
]
# def by_end_num(line):
#     words = line.split()
#     return words[-1]
#
# for line in sorted(line_list, key=by_end_num):
# print(line)

by_end_num = lambda line: line.split()[-1]


for line in sorted(line_list, key=by_end_num):
    print(line)
