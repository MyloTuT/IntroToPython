#!/usr/bin/env python3

#Ex1.1
x = 2    #assign first to variable
y = 4    #assign second to variable
z = 6.0  #assign float to variable
vsum = x + y + z
print(vsum)

#Ex1.2
a = 10
b = 20
mSum = 10 * 20
print(mSum)

#Ex1.3
var = '5'
var2 = '10'
convert_one = int(var)      #convert var into an int and assign to a variable
convert_two = int(var2)     #convert var2 into an int and assign to a variable
var_total = convert_one + convert_two
print(var_total)        #print the total of var and var2 as converted integers

#Ex1.4
user_var = input('Please enter an integer: ')   #request a integer from a user
user_doubled = int(user_var) * 2
print(user_doubled)

#Ex1.5
user_place = input('Name your favorite place: ')
print('Hello,' + ' ' + user_place + '!')

#Ex1.6
multi_exclamation = input('Please enter your excitement level: ')
print('Hello,' + ' ' + user_place + '!' * int(multi_exclamation))

#Ex1.7
thirty_five = 35.30
tf_output = round(thirty_five)
print(tf_output)

#Ex1.8
tf_super_float = 35.359958
tf_rounded_two = round(tf_super_float, 2)
print(tf_rounded_two)

#Ex1.9
var = "5"
var2 = "4"
var_conversion = int(var)
var2_conversion = int(var2)
var_sum = var_conversion / var2_conversion
print(var_sum)
