#!/usr/bin/env python3

ff = open('../python_data/pyku.txt')

xx = ff.read()
xx_separate = xx.splitlines()
xx_first = xx_separate[0]
xx_last = xx_separate[-1]
print(type(xx_separate))
print(xx_first)
print(xx_last)
