#!/usr/bin/env python3
counter = 0
line_sum = 0

while True:
    user_year = input('please enter a 4 digit year: ')

    if user_year.isdigit():
        break
    else:
        print('not 4 digits')

fo = open("../python_data/Fama-French_data.txt")

for lines in fo:
    line = lines[12:16]
    lines_year = lines[0:4]

    if user_year == lines_year:
        counter += 1
        line_num = float(line)
        line_sum = line_sum + line_num


line_av = line_sum / counter
fo.close()

print('count {}, sum {}, average {}'.format(counter, line_sum, line_av))