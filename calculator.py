#https://github.com/Ironarjun/lab11-AS-IM.git
#Arjun Suresh
#Luliana Mashchenko
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a, base):
    if a <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(a, base)

def exp(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(a)







