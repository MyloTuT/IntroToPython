#!/usr/bin/env python3
from datetime import time
# Flask web development
#.nexus

#Homework

# def dothis():
#     #something goes wrong
#     try:
#         raise ValueError
#     except ValueError:
#         exit('something went wrong')
#
# exit()

#Classes
#Notes

#object: an unit of data of a particular type that has characterist functionality
# each object is it's own floating dictionary

#'class' statement defines a new object type
# calling the class (the 'constructor') produces a new object of that type
    # new object of that type (we call this an 'instance')
    # (any number of instances can be created)
# each instance has its own "attribute dictionary"
    # (setting an attribute updates the dictionary)
# when accessing an attribute, python looks for it in the instance

# if Python can't find the attribute in the instance it looks for it in the class (i.e., a variable defined in the class)

# the class also has an attribute dictionary
#   these attributes can be accessed in the class itself

#when a method is called on a object, the object is implicitly passed as the first argument



# class Addit():
#     def _add_(self, arg):
#         return 5
#     def doubleit(self):
#         print('called!!!!!!!!')
#
# x = Addit()
# y = x + 90
# print(y)
# x.doubleit()
# exit()

# class MyClass():
#     """ MyClass is a demonstration class """
#     def greet(self):
#         print(self)
#         print('hello!')
#     def getDict():
#         return(self)
#     myvar = 'This This This'
#
#
# y = MyClass() #call the class to produce a new instance
#               # a new 'MyClass' object
# z = MyClass()
# z.x = 'YO'
#
# y.x = 5
# y.z = 10
# y.myname = 'Mylo'
#
# print(y.x)
# print(y.myname)
# print(y.__dict__)
# z.greet()
# print(z.x)
# print(MyClass.__dict__)
# print(MyClass.myvar)
# MyClass.greet(5)


print('************************************* \n')
class MyInt():
    def __init__(self):
        self.num = 0
    def increment(self):
        if self.num == 10:
            raise ValueError('max val must be <= 10')
        self.num = self.num + 1

x = MyInt()
y = MyInt()

x.num = 0
y.num = 0

for counter in range(10):
    print(x.num)
    x.increment()

exit()
