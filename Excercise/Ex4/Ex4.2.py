#!/usr/bin/env python3

fo = open("../python_data/passwords.txt")

text = fo.readlines()

first_three = text[0:3]
print(first_three)
