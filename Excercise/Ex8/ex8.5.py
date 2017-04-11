#!/usr/bin/env python3
import sys
import os

try:
    user_directory = sys.argv[1]
except (IndexError):
    exit('error:  please provide an argument')

try:
    files = os.listdir(user_directory)
except OSError:
    exit('error: directory does not exist or is not readable')

for items in files:
    item_path = os.path.join(user_directory, items)

    if os.path.isfile(item_path):
        this_type = 'file'
    else:
        this_type = 'dir'
    print('{} ({})'.format(items, this_type))
