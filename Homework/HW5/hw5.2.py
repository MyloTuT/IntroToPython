#!/usr/bin/env python3

market_value = {}

fo = open('../python_data/F-F_Research_Data_Factors_daily.txt').readlines()
fo_slice = fo[1:-1]

for lines in fo_slice:
    year = lines[0:4]
    date, mkt_rf, smb, hml, rf = lines.split(' ')

#     mkt_line = split_line[1]#[0][11:16]
#     if years not in market_value:
#         market_value[years] = []
#     market_value[years] = market_value[years] + mkt_line
# print(market_value[years])


# open the file and read into a list of lines
# slice the lines to exclude the header and footer lines
#
# initialize an empty dictionary
#
# for each line in the file lines:
#     slice out the year
#     split out the mkt-rf value and convert to float
#     if the year is not in the dicti:
#         set the year key and value 0.0 in the dict
#     add the mkt-rf float to the current value for the year in this dict
#
# store the integer length of the dict (so we can see the max value allowed)
#
# start a while True loop
#     ask the user for the number of results desired
#     ask the user for direction value "highest" or "lowest"
#     if the number of results is not all digits,
#         print an error message
#         continue to top of while loop
#     if the direction value is not "highest" or "lowest",
#         print an error message
#         continue to top of while loop
#     convert the number of results to an integer
#     if the number of results requested is greater than the dict length,
#         print an error message
#         continue to top of while loop
#     break out of the loop (no errors detected)
#
# set the "this_reverse" variable to True or False based on the value of the "direction" choice:
# if "direction" == 'highest', set "this_reverse" to True.  if "direction" == 'lowest', set
# "this_reverse" to False
#
# sort the keys of the dict based on value (using the key= value dict.get (see slides)).  also
# include the reverse=True or reverse=False depending on the value of the "reverse" variable.
