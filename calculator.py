git
add
calculator.py
git
commit - m
"added GitHub link to line 1 of calculator.py"
git
push
#https://github.com/Ironarjun/lab11-AS-IM.git
#Arjun Suresh
#Luliana Mashchenko
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or b<=0 or b ==1:
        raise ValueError
    return math.log(a,b)

def exp(a, b):
    return a**b








