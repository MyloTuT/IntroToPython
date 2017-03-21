#!/usr/bin/env python3
# 1. Don't forget about double subscript

Question/Steps to complex sorting
1.) What is one item to be sorted
    ... this will be the arg to your sort function
2.) What is the value by which that item should be sorted?
    ... this will be the return value from your sort function
3.) Can you write a function that takes the one item and returns the value by
    ... which you'd like it sorted

example:
from config import conf

def by port(thisdict):
    return thisdict['database']['port']
