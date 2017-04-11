#!/usr/bin/env python3

import sys
import os

try:
    users_directory = sys.argv[1]
    users_word = sys.argv[2]
except (IndexError):
    exit('please provide two arguments')

try:
    file_directory = os.listdir(users_directory)
except (OSError):
    exit('please provide a directory')


for files in file_directory:

    files_path = os.path.join(users_directory, files)

    line_count = 0
    for lines in open(files_path):
        line_count = line_count + 1

        if users_word in lines:
            print('{} (line {}): {}'.format(files, line_count, lines))
        else:
            continue
