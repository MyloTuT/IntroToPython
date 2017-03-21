#!/urs/bin/env python3
student_data = {}

for line in open('../python_data/student_db.txt'):
    line_items = line.split(':')
    ids = line_items[0]
    ids_data = line_items[1:]
    student_data[ids] = ids_data

print('{} records loaded.'.format(len(student_data)-1) )

while True:

    user_input = input('Please enter an id (\'q\' for quit): ')

    if user_input == 'q':
        exit()
        break

    if user_input in student_data:
        student_address = student_data[user_input]
        print('address for {user_input}:'.format(user_input=user_input))
        print('{street} \n{city}, {state} {zip_code}'.format(street=student_address[0], city=student_address[1], state=student_address[2],zip_code=student_address[3]) )
    else:
        print('sorry, that id does not exist')
