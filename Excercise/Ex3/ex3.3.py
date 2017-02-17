#!/usr/bin/env python3
counter = 0

t_file = open('../python_data/FF_abbreviated.txt')

for my_tr in t_file:
    counter +=1
    print('{rowNumber} {data}'.format(rowNumber=counter, data=my_tr))
t_file.close()

print(counter)
