#!/usr/bin/env python3

#Ex2.1
user_text = input('please enter some text: ')
print('you just wrote: ', user_text)

Ex2.2
user_int_request = input('please enter an integer: ')

if user_int_request.isdigit() == True:
    print('Thanks for the integer')
else:
    print('that was NOT an integer:')


#Ex2.3
while True:
    user_int_request = input('please enter an integer: ')

    if user_int_request.isdigit() == True:
        print('Thanks for the integer')
        break
    else:
        print('that was NOT an integer:')

#Ex2.4
count = 1
while count <= 10:
    print(count)
    count = count + 1

#Ex2.5, 2.6, 2.7
bday = "Happy Birthday to you!"
a = 1
while a <= 10:
    print(bday)
    a = a + 1

how_many = input("How many times should I greet you?: ")

if how_many.isdigit() == False:
    exit('error202: not a digit')

times = int(how_many)
b = 1

while b <= times:
    print(bday)
    b = b + 1

#Ex2.8
msg = 'I am happy or sad or angry or mad or generous or stingy'
msg_count = msg.count('or')
print(msg_count)

#Ex2.9
some_input = input('please enter a string to search: ')
some_found = msg.count(some_input)
print(some_found)

#Ex2.10
user_replace_request = input('please enter a character to replace: ')
character_replace = msg.replace(user_replace_request, 'x')
print(character_replace)



# Homework 2.1
results = 0
while True:
    user_num_request = input('please enter an integer: ')
    if user_num_request.isalpha():
        print('Sorry, "{badinput}" is not a valid integer'.format(badinput=user_num_request))
        continue
    else:
        break

print('counting from 0 to 100 by "{user_num_request}"'.format(user_num_request=user_num_request))
user_num = int(user_num_request)
counter = 0
while counter <= user_num:
    print(counter)
    results = results + counter
    counter = counter + 1
print(results)


# # Homework2.2
results = 0 #initiate results
counter = 0 #initiate number storage
while True:
    user_num_request = input('please enter a positive integer: ') #request the users number input
    if user_num_request.isalpha() or int(user_num_request) < 1: #check if the users input is a number and greater than 0
        print('sorry, "{badinput}" is not a valid positive integer'.format(badinput=user_num_request))
        continue
    else:
        break

user_num = int(user_num_request) #convert the users number to an integer
user_num_addition = 0

<<<<<<< HEAD
while counter <= user_num:
    results = results + counter
    counter += 1
print('the sum from 1 to {userint} is {result}'.format(userint=user_num, result=results))  #print results'


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
