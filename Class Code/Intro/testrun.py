#!/usr/bin/env python3

#1.2
bill_total = input('Please enter the total bill amount: ')
bill_number = int(bill_total)
print(bill_number)
party_people = input('Please enter the number of people in your party: ')
party_number = int(party_people)
tip_entered = input('Please enter the desired tip percentage: ')
tip = float(tip_entered)
tip_percentage = tip * .01
print(tip_percentage)
tip_amount = bill_number * tip_percentage
total = bill_number + tip_amount
total_per_person = total / party_number
print(total_per_person)

print('A ' + str(tip) + '% ($' +  str(tip_amount) + ') was added to the bill, for a total of $' + str(total))
print('With ' + party_people + ' in your party, each person must pay $' + str(total))
