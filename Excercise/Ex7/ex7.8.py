#!/usr/bin/env python3

words = [ 'Hello', 'my', 'dear', 'the', 'heart', 'is', 'a', 'child.' ]

print([ var.upper() for var in words if len(var) >= 4 ])
