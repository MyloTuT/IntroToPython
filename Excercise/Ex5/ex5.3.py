#!/usr/bin/env python3

mylist = ['Hey', 'there', 'I', 'am', 'amazing!']

mydict = {}

for word in mylist:
    mydict[word] = len(word)

for key in mydict:
    print('{} is len {}'.format(key, mydict[key]))
