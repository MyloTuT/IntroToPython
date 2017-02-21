#!/usr/bin/env python3
users_year = 0

while True:
    user_input = input('please enter a 4 digit year: ')
    users_year = user_input

    if user_input.isdigit():
        break
    else:
        print('not 4 digits')

fo = open("../python_data/FF_abbreviated.txt")
print(len(fo))


for lines in fo:
    line = lines[0:4]
    if users_year == line:
        continue
