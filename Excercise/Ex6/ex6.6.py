#! /usr/bin/env python3

mynums = ['5', '101', '10', '1', '3']

def str_num(mynums):
    print('now setting sor criteria for', mynums)
    return int(mynums)

print(sorted(mynums, key=str_num))
