# https://github.com/saco-03/lab10-IO-JY
# Partner 1: Isaac Osorio
# Partner 2: Jerry Yao
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def square_root(a):
   if a < 0:
       raise ValueError
   else:
       return math.sqrt(a)

def hypotenuse(a, b):
   return math.hypot(a, b)

def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def logarithm(a, b):
   if (b <= 0) or (a == 1) or (a<=0):
       raise ValueError
   else:
    return math.log(b, a)   # use math library/raise ValueError

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return math.pow(a, b)