#!/usr/bin/env python3

import sys
import os

# print(sys.argv)
# print(type(sys.argv))

mydirectory = '/Users/mrayfield'

# for item in os.listdir(mydirectory):
#     item_path = os.path.join(mydirectory, item) #you have to join the listing and the directory to get the path
#     print(item_path)

for item in os.listdir('/'):
    if os.path.isfile(item):
        print(os.path.getsize(item))

try:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
except (IndexError, ValueError):
    exit('please enter 2 args')
# except ValueError:
#     exit('both args must be ints')
