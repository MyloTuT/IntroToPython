#!/usr/bin/env python3

import sys
import os
import time

try:
    user_input = sys.argv[1]
except (IndexError):
    exit('please provide 1 input')

try:
    users_directory = os.listdir(user_input)
except (OSError):
    exit('please input a directory')

users_old_files = set()
for files in users_directory:
    items_path = os.path.join(user_input, files)
    users_old_files.add(items_path)

while True:
    time.sleep(5)
    users_new_files = set()

    for files in users_directory:
        items_path = os.path.join(user_input, files)
        users_new_files.add(items_path)

    for items in sorted(users_new_files):
        if items in users_new_files:
            True
        else:
            print(users_old_files.difference(users_new_files))
