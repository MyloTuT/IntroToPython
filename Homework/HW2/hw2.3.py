#!/usr/bin/env python3

#Homework2.3
sample_text = """And since you know you cannot see yourself,
so well as by reflection, I, your glass,
will modestly discover to yourself,
that of yourself which you yet know not of."""

search_text = input('please enter a word to search: ')
replacement_text = input('please enter a replacement word: ')
counter = 0
while sample_text.find(search_text) > -1:
    counter +=1
    text_replaced = sample_text.replace(search_text, replacement_text, 1)
    sample_text = text_replaced
print(text_replaced)
print(counter, 'replacements made.')
=======
if user_num < 1: #check if the users input is a number and greater than 0
    print('sorry, "{badinput}" is not a valid positive integer'.format(badinput=user_num_request))
    continue
else:
    break
while num_storage < user_num:
    user_num_addition = user_num / user_num
    num_storage = user_num_addition + num_storage #store users number and increase by one
    results = num_storage + user_num    #add loop storage to users origiinal number to get the answer we are looking for
print('the sum from 1 to {userint} is {result}'.format(userint=user_num, result=results))  #print results'

if results > user_num:  #break to prevent infinite loop

# # #Homework2.3
# sample_text = """And since you know you cannot see yourself,
# so well as by reflection, I, your glass,
# will modestly discover to yourself,
# that of yourself which you yet know not of."""
#
# search_text = 'yourself' #input('please enter search text: ')
# replacement_text = 'corgi' #input('please enter replace text: ')
#
# counter = 0
# while sample_text.find(search_text) > -1:
#     counter +=1
#     text_replaced = sample_text.replace(search_text, replacement_text, 1)  #search the sample text for the users input and replace it with it's second input
#     sample_text = text_replaced
# print(text_replaced)    #print the sample text with the replaced replacement text requested by the users
# print(counter)
>>>>>>> 3fe934a3f39b3fa16a8a7bba03078796b2ea7b04
