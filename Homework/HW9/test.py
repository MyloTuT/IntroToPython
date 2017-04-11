#!/usr/bin/env python

import filelib

data_file = '../python_data/student_db.txt'

lines = filelib.getlines(data_file, newlines=True)
print(len(lines))

text = filelib.gettext(data_file)
print(len(text))


# when the below line is uncommented, your module should raise a ValueError
# exception and, in the raised error, explain that the delimiter does not
# appear to be in one of the line of the file.  See the slide on raise for
# details on raising an exception with a message.

list_of_lists = filelib.getfields(data_file, delimiter='baddelimeter')


list_of_lists = filelib.getfields(data_file, delimiter=':')
print(list_of_lists)
