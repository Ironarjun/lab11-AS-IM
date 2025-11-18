#https://github.com/Ironarjun/lab11-AS-IM.git
#Arjun Suresh
#Luliana Mashchenko
import math

# Basic arithmetic
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def exp(a, b):
    return a ** b

def log(a, base):
    if a <= 0:
        raise ValueError("Logarithm input must be positive.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(a, base)


def square_root(x):
    if x < 0:
        return None
    return math.sqrt(x)

def hypotenuse(a, b):
    try:
        return math.sqrt(a * a + b * b)
    except TypeError:
        return None







