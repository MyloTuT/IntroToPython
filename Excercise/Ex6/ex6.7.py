#! /usr/bin/env python3

def my_element_modifier(arg):
    print('now modifying', arg)
    lower_arg = arg.lower()
    return lower_arg

sorted_list = sorted(['e', 'c', 'D', 'B', 'a'], key=my_element_modifier)
print(sorted_list)
