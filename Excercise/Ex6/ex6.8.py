#!/usr/bin/env python3

line_list = [
'the value on this line is 3',
'the value on this line is 1',
'the value on this line is 4',
'the value on this line is 2',
]

def line_sort(line_value):
    split_line = line_value.split()
    return split_line[-1]

for line in sorted(line_list, key=line_sort):
    print(line)
