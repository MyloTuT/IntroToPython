#!/usr/bin/env python3

mylist = ['Hey', 'there', 'I', 'am', 'amazing!']

mydict = {}

for word in mylist:
    mydict[word] = len(word)

user_input = input('please enter a word: ')

if user_input in mydict:
    print('The word "{}" is len {}'.format(user_input, mydict[user_input]))
else:
    print('That word is not in the dictionary')
