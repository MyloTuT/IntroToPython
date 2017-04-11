#!/usr/bin/env python3

var_1 = input('Please enter an integer: ')      #request an int from the user
var_2 = input('Please enter another integer: ') #request another int

var_conversion = int(var_1)     #cast var_1 into an int
var_2_conversion = int (var_2)  #cast var_2 into an int
var_output = var_conversion ** var_2_conversion    #multiply var_1 & var_2

output_conversion = str(var_output)     #cast output into a string
output_length = len(output_conversion)  #get the length of the output variable
print(output_length)
print("=" * output_length)
print(var_output)
print("=" * output_length)
