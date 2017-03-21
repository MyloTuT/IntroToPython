#! /usr/bin/env python3

mystrs = ['I', 'was', 'hanging', 'on', 'a', 'rock']

def str_length(mystr):
    print('now setting sor criteria for', mystr)
    return len(mystr)

print(sorted(mystrs, key=str_length))
