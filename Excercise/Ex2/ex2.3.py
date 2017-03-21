#!/usr/bin/env python3

while True:
    user_int_request = input('please enter an integer: ')

    if user_int_request.isdigit() == True:
        print('Thanks for the integer')
        break
    else:
        print('that was NOT an integer:')
