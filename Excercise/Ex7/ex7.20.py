#!/usr/bin/env python3

import pprint

#!/usr/bin/env python3
import pprint

outer_dict = {}
fh = open('../python_data/revenue.txt')
for line in fh:
    company, state, revenue = line.split(',')

    if state not in outer_dict:
        outer_dict[state] = []
    outer_dict[state].append(float(revenue))

print(outer_dict)

count = 0
revenue_addition = 0
for revenue in outer_dict['NY']:
    revenue_addition = revenue + revenue_addition
    count = count + 1
print(revenue_addition / count)
