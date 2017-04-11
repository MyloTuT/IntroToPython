#!/usr/bin/env python3
import pprint   #import Module pprint

fh = open('../python_data/student_db.txt')  #open student_db file

lines = fh.readlines()[1:]  #organize the student_db file into readable lines starting at line 1 and assign this to 'lines'

state_count = dict()    #initilize an empty dict
for line in lines:  #iterate over 'lines'
    id, street, city, state, zip = line.split(':')  #split 'lines' by ':' and assign each row to a var

    if state not in state_count: #check the membership for 'state' in the dict state_count
        state_count[state] = []     #if the membership does not exist for the state assign an empty list
    state_count[state].append(id)   #append id to the dict 'state_count' and assign a key (variable state)

pprint.pprint(state_count)  #print the complex structure state_count

for id in state_count['NJ']:    #iterate over NJ to print both all of the associated ID's
    print(id)
