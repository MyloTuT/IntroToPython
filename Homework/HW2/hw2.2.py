#!/usr/bin/env python3

# Homework2.2
results = 0 #initiate results
counter = 0 #initiate number storage
while True:
    user_num_request = input('please enter a positive integer: ') #request the users number input
    if user_num_request.isalpha() or int(user_num_request) < 1: #check if the users input is a number and greater than 0
        print('sorry, "{badinput}" is not a valid positive integer'.format(badinput=user_num_request))
        continue
    else:
        break

user_num = int(user_num_request) #convert the users number to an integer
user_num_addition = 0

<<<<<<< HEAD
while counter <= user_num:
    results = results + counter
    counter += 1
print('the sum from 1 to {userint} is {result}'.format(userint=user_num, result=results))  #print results'
