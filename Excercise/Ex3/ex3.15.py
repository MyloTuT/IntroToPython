#!/usr/bin/env python3

ff = open('../python_data/pyku.txt')

xx = ff.read()
spam_count = xx.count('spam')
print(spam_count)
