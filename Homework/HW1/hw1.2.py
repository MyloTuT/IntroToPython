#!/usr/bin/env python3

bill_total = input('Please enter the total bill amount: ')
bill_number = int(bill_total)       #convert bill total to an int
party_people = input('Please enter the number of people in your party: ')
party_number = int(party_people)    #convert the number of people into an int
tip_entered = input('Please enter the desired tip percentage: ')
tip = float(tip_entered)        #convert the tip percentage to a float
tip_percentage = tip * .01      #convert the tip number into a percentage
tip_amount = bill_number * tip_percentage       #do the math to get the tip dollar amount from the bill amount
total = bill_number + tip_amount            #add the tip to the bill amount
total_per_person = total / party_number     #divide the bill based on the number of people

print('A ' + str(tip) + '% ($' +  str(tip_amount) + ') was added to the bill, for a total of $' + str(total))
print('With ' + party_people + ' in your party, each person must pay $' + str(total_per_person))
