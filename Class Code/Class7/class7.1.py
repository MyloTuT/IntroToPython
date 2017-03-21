#!/usr/bin/env python3

# for each structure, print out the first (and last) name

# start with students2, then students3, students1
# next, sort the structures by last name
# again start with students2, then students3, then students1

def bylname(dictkey):   #argument is a key
    return students1[dictkey]['lname']

students1 = {
   'jw3':  { 'fname': 'Joe',   'lname': 'Wilson' },
   'ma2':  { 'fname': 'Mike',  'lname': 'Apple' },
   'mx99': { 'fname': 'Marie', 'lname':'Xander' }
}

for idkey in sorted(students1, key=bylname):
    print(students1[idkey]['lname'])

# for name in students1:
#     print(students1[name]['fname'], students1[name]['lname'])

print('\n')


# def bythird(arg):
#     return(arg[2])
#
students2 = [
   ['jw3', 'Joe', 'Wilson'],
   ['jw3', 'Joe', 'Wilson'],
   ['jw3', 'Joe', 'Wilson']
]

print('\n')

for inlist in sorted(students2, key=bythird):
    print('{}: {}, {}',format(inlist[0], inlist[2], inlist[1]))



for student in students2:
    print(student[1], student[2])

print('\n')

#
# students3 = [
#    { 'id': 'jw3', 'fname': 'Joe',   'lname': 'Wilson' },
#    { 'id': 'ma2', 'fname': 'Mike',  'lname': 'Apple' },
#    { 'id': 'mx99', 'fname': 'Marie', 'lname':'Xander' }
# ]
#
# def bylname(this_dict):
#     return this_dict['lname']
#
# for name in sorted(students3, key=bylname):
#     print(name['lname'])
#

# for name in students3:
#     print(name['fname'], name['lname'])
