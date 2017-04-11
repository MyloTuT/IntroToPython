#!/usr/bin/env python3

import sys
import os

user_file = sys.argv[1]

if os.path.isfile(user_file):
    print('{}: {} bytes'.format(user_file, os.path.getsize(user_file)))

else:
    exit('error:  {} is not a file in this directory'.format(user_file))
