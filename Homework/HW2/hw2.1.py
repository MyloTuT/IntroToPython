#!/usr/bin/env python3

# Homework 2.1
results = 0
while True:
    user_num_request = input('please enter an integer: ')
    if user_num_request.isalpha():
        print('Sorry, "{badinput}" is not a valid integer'.format(badinput=user_num_request))
        continue
    else:
        break

print('counting from 0 to 100 by "{user_num_request}"'.format(user_num_request=user_num_request))
user_num = int(user_num_request)
counter = 0
while counter <= user_num:
    print(counter)
    results = results + counter
    counter = counter + 1
print(results)
