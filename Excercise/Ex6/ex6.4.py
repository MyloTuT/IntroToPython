#!/usr/bin/env python3

charList = ['F', 'e', 'c', 'a', 'B', 'D']

def charListLower(str_lower):
    print('now setting sor criteria for', str_lower)
    return str_lower.lower()

print(sorted(charList, key=charListLower))
