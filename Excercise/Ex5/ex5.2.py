#!/usr/bin/python3

mylist = ['Hey', 'there', 'I', 'am', 'amazing!']

mydict = {}

for word in mylist:
    mydict[word] = len(word)

print(mydict)
