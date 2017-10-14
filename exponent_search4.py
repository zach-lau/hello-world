# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:00:02 2017

@author: zlau2
"""


from math import log, floor
from decimal import *

base1 = Decimal(3)
base2 = Decimal(2)
goal = Decimal(17.4513)

getcontext().prec = 1000

c1 = base2.ln()/base1.ln()
c2 = goal.ln()/base1.ln()

en = c1 - floor(c1)
e = c2 - floor(c2)

steps = 60

n = 1

for i in range(0,steps):
    
    count = 0
    #print(en)
    
    count = floor(1/en) + 1
    
    n *= count
    en = count*en - 1
    #print(count)

n *= round((1-e)/en)
m = round(c1*n + c2)
print('\n')
print("m:", m)
print('\n')
print("n:", n)

l = Decimal(m*base1.ln() - n*base2.ln())

print('\n')
print(l.exp())