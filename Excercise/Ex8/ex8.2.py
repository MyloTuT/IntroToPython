#!/usr/bin/env python3

import sys

try:
    firstarg = sys.argv[1]
    secondarg = sys.argv[2]

    firstint = int(sys.argv[1])
    secondint = int(sys.argv[2])
except (IndexError, ValueError):
    exit('Usage: {} [int1] [int2]'.format(sys.argv[0]))

print('{} + {} = {}'.format(sys.argv[1], sys.argv[2], int(sys.argv[1]) + int(sys.argv[2])))
