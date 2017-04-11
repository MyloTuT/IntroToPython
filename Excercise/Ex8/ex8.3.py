#!/usr/bin/env python3

import sys
import os

filename = '../python_data/student_db.txt'

file_path = os.path.join(filename)
item_size = os.path.getsize(file_path)

print('{}: {} bytes'.format(file_path, item_size))
