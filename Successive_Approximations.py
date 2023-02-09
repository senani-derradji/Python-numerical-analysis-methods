import math

def g(x):
    '''    f(x) =  x³ + 4x² - 10  / g(x) = x  '''
    g = math.sqrt(10/(x+4))
    return round(g,6)

a = int(input("a : "))
b = int(input("b : "))
e = float(input("e : "))

def Fixed_Point(a,b,e=0.001):
    x0 = (a+b)/2
    i = 1
    condition = True
    
    while condition:
        x1 = g(x0)
        print(f'iterations-{i}- ,g(X{i}:{x0}) = {g(x0)} ')
        if abs(x1-x0) < e: condition = False

        x0 = x1
        i = i+1
    
Fixed_Point(a,b,e)
