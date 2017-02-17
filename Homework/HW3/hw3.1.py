#!/usr/bin/env python3
users_year = 0

while True:
    user_input = input('please enter a 4 digit year: ')

    if user_input.isdigit():
        break
    else:
        print('not 4 digits')

user_convert = int(user_input)
users_year = user_convert
print(users_year)
