#!/usr/bin/env python3

from config import conf

for lines in conf:
    print('domain: {}'.format(lines['domain']))
    print('db_host: {}'.format(lines['database']['host']))
    print('db_port: {}'.format(lines['database']['port']))
    print('plugins:')
    for plugin in lines['plugins']:
        print('  {}'.format(plugin))
    print()
    print()
