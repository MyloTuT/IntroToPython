#!/usr/bin/env python3
# # set a sum FLOAT value to 0.0
# sumvalue = 0.0
#
# # open the file, a FILE object is returned
# fhxx = open('../python_data/FF_abbreviated.txt')
# # loop through the file object with 'for'
# for myline in fhxx:
#   # each line of the file (a STRING)
#   # is retrieved in the loop
#   # split the line into a LIST of strings
#   items = myline.split()
#   # select the 2nd element of the list of strings
#   # (a STRING)
#   strval = items[1]
#   # convert the string to an FLOAT
#   floatval = float(strval)
#   # add the integer to a sum
#   sumvalue = sumvalue + floatval
# # report the sum
# print sumvalue

# THE SUMMARY ALGORITHM
# start a summary variable

# loop through some data

    # "normalize" (separate out and convert)
    #the data you need

    # add the data to the summary variable

# report the summary variable value

uinput = '1927'
x = '19270101'
lineyear = x[0:5]

if uinput == lineyear:
    print('you got it')
else:
    print('sorry')

num = x[3:6]
print(num)
