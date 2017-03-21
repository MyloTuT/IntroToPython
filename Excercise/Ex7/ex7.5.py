#!/usr/bin/env python3

pyku = '../python_data/pyku.txt'

by_num_words = lambda line: len(line.split())


for line in sorted(open(pyku).readlines(), key=by_num_words):
    line = line.rstrip()
    print(line)
