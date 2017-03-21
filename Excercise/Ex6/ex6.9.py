#!/usr/bin/env python3
fo = open('../python_data/pyku.txt')

def line_length(lines):
    line_split = lines.split()
    line_length = len(line_split)
    return line_length

fo_read = fo.readlines()
for line in sorted(fo_read, key=line_length):
    print(line.rstrip())
