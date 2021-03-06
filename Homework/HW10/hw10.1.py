#!/usr/bin/env python3

class Square(object):

    def __init__(self):
        self.num = 2

    def squareme(self):
        self.num = self.num * self.num
        return self.num


    def getme(self):
        return self.num

n1 = Square()
n2 = Square()
n3 = Square()

n1.squareme()
val1 = n1.getme()
print(val1)               # 4

n2.squareme()
n2.squareme()
val2 = n2.getme()
print(val2)               # 16
print(n1.getme())         # 4

n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
val3 = n3.getme()
print(val3)               # 4294967296

print(n1.getme())         # 4
print(n2.getme())         # 16
print(n3.getme())         # 4294967296
