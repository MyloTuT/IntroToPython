#!/usr/bin/env python3

bday = "Happy Birthday to you!"
a = 1
while a <= 10:
    print(bday)
    a = a + 1

how_many = input("How many times should I greet you?: ")

if how_many.isdigit() == False:
    exit('error202: not a digit')
